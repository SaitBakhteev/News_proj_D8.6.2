from django.contrib import admin
import news_portal.models as md

admin.site.register(md.Category)
admin.site.register(md.Post)
admin.site.register(md.PostCategory)
admin.site.register(md.Author)
admin.site.register(md.Comment)



# Register your models here.
