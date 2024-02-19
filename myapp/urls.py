from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... other patterns ...
    path('', views.registration, name='registration'),
    path('registration/', views.registration, name='registration'),
    path('new_registration/', views.new_registration, name='new_registration'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('mypage/', views.my_page, name='mypage'),  
    path('blog/', views.blog, name='blog'),           
    path('chat/', views.chat, name='chat'),  
    path('chat/new/', views.new_chat_room, name='new_chat_room'),  
    path('new_chat_room/', views.new_chat_room, name='new_chat_room'), 
    path('chat_room/<int:room_id>/', views.chat_room, name='chat_room'),
    path('send_message/<int:room_id>/', views.send_chat_message, name='send_chat_message'),   
    path('adoption/', views.adoption, name='adoption'),
    path('adoption/post/', views.post_adoption, name='post_adoption'),  # 里親募集を投稿するページ
    path('adoption/new/', views.new_adoption, name='new_adoption'), # 新着里親情報を表示するページ
    path('adoption/post/submit/', views.post_adoption_submit, name='post_adoption_submit'),
    path('adoption/<int:post_id>/', views.adoption_post_detail, name='adoption_post_detail'),
    path('nutrition/', views.nutrition, name='nutrition'),
    path('nutrition/symptoms/', views.nutrition_symptoms, name='nutrition_symptoms'),
    path('nutrition/post/submit/', views.nutrition_post_submit, name='nutrition_post_submit'),
    path('nutrition/post/', views.nutrition_post, name='nutrition_post'),
    path('my_page/', views.my_page, name='my_page'),
    path('owner_info/', views.owner_info, name='owner_info'),
    path('pet_info/', views.pet_info, name='pet_info'),
    path('pet_info/', views.pet_info, name='pet_info'), 
    path('new_post/', views.new_post, name='new_post'),
    path('blog_posts/', views.blog_posts, name='blog_posts'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('send_message/<int:room_id>/', views.send_chat_message, name='send_chat_message'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)