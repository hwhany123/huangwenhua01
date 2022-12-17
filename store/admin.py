

# Register your models here.
from django.contrib import admin
from store.models import Store, Category, Tag, Avatar

admin.site.register(Store)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Avatar)