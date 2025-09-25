from django.utils.translation import gettext_lazy as _
from .models import Banner, Gallery, News , category, categoryItem , LastItem
from modeltranslation.translator import register, TranslationOptions


@register(Banner)
class BannerTranslation(TranslationOptions):
    fields = ('title', 'description')

@register(Gallery)
class GalleryTranslation(TranslationOptions):
    fields = ('title',)

@register(News)
class NewsTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(category)
class categoryTranslation(TranslationOptions):
    fields = ('name', 'about')


@register(categoryItem)
class categoryItemTranslation(TranslationOptions):
    fields = ('name', 'about')

@register(LastItem)
class LastItemTranslation(TranslationOptions):
    fields = ('name', 'about')



