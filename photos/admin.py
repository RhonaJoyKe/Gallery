from django.contrib import admin

# Register your models here.
from .models import Image,Category,Location


# Register your models here.
# class ArticleAdmin(admin.ModelAdmin):
#     filter_horizontal =('tags',)


admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)