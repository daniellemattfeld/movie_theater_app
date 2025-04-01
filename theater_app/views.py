from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, RegisterForm
from django.contrib import messages
from .models import ContactMessage, Movie, Showtime, Upcoming, Ticket


def home(request):
    movies = Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})


def coming_soon(request):
    upcoming_movies = Upcoming.objects.all()
    return render(request, 'coming_soon.html', {'upcoming_movies': upcoming_movies})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            ContactMessage.objects.create(
                name=name, email=email, subject=subject, message=message
            )

            messages.success(request, f'Thank you for contacting us! Your message has been sent.')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def login_register(request):
    next_url = request.GET.get('next', 'home')
    register_form = RegisterForm(request.POST or None)
    login_form = AuthenticationForm(request=request, data=request.POST)
    if request.method == 'POST':
        if register_form.is_valid():
            register_form.save()
            email = register_form.cleaned_data.get('email')
            password = register_form.cleaned_data.get('password1')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(next_url)
        elif 'login' in request.POST and login_form.is_valid():
            email = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(next_url)
            else:
                login_form.add_error(None, "Invalid credentials")
    else:
        register_form = RegisterForm()
        login_form = AuthenticationForm(request=request)

    return render(request, 'login_register.html', {'register_form': register_form, 'login_form': login_form, 'next_url': next_url})


def showtimes(request):
    movies = Movie.objects.all()
    playtime = Showtime.objects.all()
    return render(request, 'showtimes.html', {'movies': movies, 'playtime': playtime})


def movie_details(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movie_details.html', {'movie': movie})


@login_required(login_url='login_register')
def ticket_purchase(request, showtime_id):
    showtime = get_object_or_404(Showtime, id=showtime_id)
    movie = showtime.movie
    ticket_quantity = request.session.get('ticket_quantity', 0)

    if request.method == 'POST':
        step = request.POST.get('step')
        if step == 'select_tickets':
            ticket_quantity = int(request.POST.get('quantity', 0))
            if ticket_quantity > showtime.tickets_available:
                messages.error(request, 'Not enough tickets available.')
            else:
                request.session['ticket_quantity'] = ticket_quantity
                messages.success(request, 'Ticket quantity selected. Proceed to checkout.')
        elif step == 'confirm_purchase':
            if ticket_quantity > showtime.tickets_available:
                messages.error(request, 'Not enough tickets available.')
            else:
                Ticket.objects.create(user=request.user, showtime=showtime, quantity=ticket_quantity)
                showtime.tickets_available -= ticket_quantity
                showtime.save()
                del request.session['ticket_quantity']
                messages.success(request, 'Ticket purchased successfully!')
                return redirect('home')

    return render(request, 'ticket_purchase.html',
                  {'showtime': showtime, 'movie': movie, 'ticket_quantity': ticket_quantity})


def register(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()  # Save user
            return redirect('home')  # Redirect to login after registration
        else:
            print(register_form.errors)  # Log any errors for debugging
    else:
        register_form = RegisterForm()

    return render(request, 'register.html', {'register_form': register_form})
