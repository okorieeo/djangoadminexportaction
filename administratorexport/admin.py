from django.contrib import admin
from admin_export_action.admin import export_selected_objects
from csvexport.actions import csvexport
from .models import Post

class PostAdmin(admin.ModelAdmin):
    #fields = ['title']
    actions = [export_selected_objects, csvexport]
    class Meta:
        model = Post
admin.site.register(Post, PostAdmin) 
