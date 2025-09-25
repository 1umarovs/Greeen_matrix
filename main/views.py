from django.shortcuts import render
from .models import Banner, Gallery, News , category , categoryItem , ItemImage , LastItem
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    banners = Banner.objects.all()
    galleries = Gallery.objects.all()
    news = News.objects.defer('description' , 'description_uz' , 'description_ru' , 'description_en').all()
    categories = category.objects.defer('about' , 'about_uz' , 'about_ru' , 'about_en').all()
    context = {
        'banners': banners,
        'galleries': galleries,
        'news': news,
        'categories': categories
    }
    return render(request, 'index.html', context)

def news_details(request , id):
    news = News.objects.get(id = id)
    recent_news = News.objects.exclude(id = id).defer('description' , 'description_uz' , 'description_ru' , 'description_en').all()[:5]
    context = {
        'new': news,
        'recent_news': recent_news
    }
    return render(request, 'blog-details.html', context)


def category_details(request, id):
    category_obj = get_object_or_404(
        category.objects.prefetch_related('category_items'),
        id=id
    )
    category_items = category_obj.category_items.all()

    context = {
        'category': category_obj,
        'category_items_': category_items
    }
    return render(request, 'category-details.html', context)


def category_item_details(request, id):
    category_item = get_object_or_404(
        categoryItem.objects.prefetch_related('item_images'),
        id=id
    )
    if category_item.last_items.exists():
        last_items = category_item.last_items.all()
        context = {
            'category': category_item,
            'category_items': last_items
        }
        return render(request, 'category-details.html', context)
    elif not category_item.last_items.exists():
        if category_item.item_images.exists():
            item_images = category_item.item_images.all()
            context = {
                'category_item': category_item,
                'item_images': item_images
            }
            return render(request, 'category-item-details.html', context)
        else:
            recent_category_items = categoryItem.objects.exclude(id = id).defer('about' , 'about_uz' , 'about_ru' , 'about_en').all()
            item_images = category_item.item_images.all()
            context = {
            'category_item': category_item,
            'recent_category_items': recent_category_items,
            'item_images': item_images
        }
        print(context)
        return render(request, 'category-item-details.html', context)

def last_item_details(request, id):
    last_item = get_object_or_404(
        LastItem.objects.prefetch_related('last_item_images'),
        id=id
    )

    recent_last_items = LastItem.objects.exclude(id = id).defer('about' , 'about_uz' , 'about_ru' , 'about_en').all()
    item_images = last_item.last_item_images.all()
    context = {
        'category_item': last_item,
        'recent_category_items_': recent_last_items,
        'item_images': item_images
    }
    return render(request, 'category-item-details.html', context)