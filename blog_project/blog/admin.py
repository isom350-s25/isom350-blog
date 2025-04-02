from django.contrib import admin
from .models import Post, Comment

class InlineComment(admin.StackedInline):
    model = Comment
    extra = 1

@admin.register(Post) # recommended way to register
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on', 'updated_on')
    list_filter = ("status", 'created_on')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}  
    inlines = [InlineComment,]
        
# Register your models here.
# one way to register
#admin.site.register(Post, PostAdmin)

#admin.site.register(Comment)
