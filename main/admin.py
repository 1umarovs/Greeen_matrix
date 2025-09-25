from django.contrib import admin
from .models import Banner, Gallery, News, category, categoryItem , ItemImage , LastItem , LastItemImage

# Register your models here.
admin.site.register(Banner)
admin.site.register(Gallery)
admin.site.register(News)
admin.site.register(category)
admin.site.register(categoryItem)
admin.site.register(ItemImage)
admin.site.register(LastItem)
admin.site.register(LastItemImage)
