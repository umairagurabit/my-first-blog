from django.contrib import admin
from .models import Post, Comment, CV_list

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CV_list)
# Register your models here.
