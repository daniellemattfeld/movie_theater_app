from django.contrib import admin
from .models import TodoItem, ContactMessage
from .models import Showtime, Movie, Upcoming, Ticket

admin.site.register(TodoItem)
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('created_at',)

class ShowtimeInline(admin.TabularInline):
    model = Showtime
    extra = 1

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','image','homepage_image','description','runtime','rating')
    inlines = [ShowtimeInline]

class ShowtimeAdmin(admin.ModelAdmin):
    list_display = ('movie', 'time')
    list_filter = ('movie',)

admin.site.register(Movie, MovieAdmin)
admin.site.register(Showtime, ShowtimeAdmin)

class UpcomingAdmin(admin.ModelAdmin):
    list_display = ('upcoming_movie', 'description', 'director', 'image')
    list_filter = ('upcoming_movie',)

admin.site.register(Upcoming, UpcomingAdmin)
admin.site.register(Ticket)