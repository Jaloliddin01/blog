from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_posted']
    list_editable = ['date_posted']
    list_per_page = 10

# admin.site.register(Post)
