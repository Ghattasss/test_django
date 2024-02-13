from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title','slug','author','puplish','statues')
    list_filter=('statues','created','puplish','author')
    search_fields=('title','body')
    prepopulated_fields={'slug':('title',)}
    raw_id_fields=('author',)
    date_hierarchy='puplish'
    ordering=('statues','puplish')

# Register your models here.
