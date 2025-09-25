from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('' , views.home , name = 'home'),
    path('news/<int:id>' , views.news_details , name = 'news-details'),
    path('category/<int:id>' , views.category_details , name = 'category-details'),
    path('category-item/<int:id>' , views.category_item_details , name = 'category-item-details'),
    path('last-item/<int:id>' , views.last_item_details , name = 'last-item-details')
]