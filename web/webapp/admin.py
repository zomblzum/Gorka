from django.contrib import admin
from webapp.models import Post, WarePost, FAQPost, ServicesPost

admin.site.register(Post)
admin.site.register(WarePost)
admin.site.register(FAQPost)
admin.site.register(ServicesPost)

# Register your models here.
