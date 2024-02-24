
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import OwnerInfoForm 
from .models import Profile
from .forms import PetInfoForm
from .models import PetProfile
from datetime import date
from .models import UserProfile
from django.contrib.auth.models import User  
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import Http404
from .models import BlogPost
from .forms import BlogPostForm
from django.shortcuts import render, get_object_or_404
from .forms import ChatRoomForm
from .models import ChatRoom, ChatMessage
from .forms import ChatRoomForm
from .models import AdoptionPost
from django.db.models import Q
from django.utils import timezone
from .models import NutritionItem, UserReview, NutritionQuestion, NutritionAnswer
from django.core.paginator import Paginator
from django.contrib import messages
from .models import NutritionPost
from .forms import NutritionPostForm
from .models import NutritionPost, SYMPTOM_CHOICES
from .forms import SignUpForm

def registration(request):
    # Your new registration view logic goes here
    return render(request, 'html/registration.html')  # Replace with the actual template name

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # 新規登録処理後のリダイレクト先を指定
            return redirect('home') # 例: ログインページへリダイレクト
    else:
        form = SignUpForm()
    return render(request, 'html/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Change 'home' to the name of your home URL
    else:
        form = AuthenticationForm()

    return render(request, 'html/login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'html/home.html')

@login_required
def my_page(request):
    user = request.user
    owner_info = None
    pet_info = None

    # 飼い主情報を安全に取得
    try:
        owner_info = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        owner_info = None

    # ペット情報を安全に取得
    try:
        pet_info = PetProfile.objects.get(user=user)
    except PetProfile.DoesNotExist:
        pet_info = None

    context = {
        'owner_info': owner_info,
        'pet_info': pet_info,
    }
    return render(request, 'html/mypage.html', context)


@login_required
def owner_info(request):
    # Check if the owner info is already registered
    profile = Profile.objects.get_or_create(user=request.user)[0]

    if request.method == 'POST':
        form = OwnerInfoForm(request.POST, request.FILES)
        if form.is_valid():
            # Update the profile with the form data
            profile.name = form.cleaned_data['name']
            profile.icon = form.cleaned_data['icon']
            profile.location = form.cleaned_data['location']
            profile.save()

            return redirect('mypage')  # Redirect to My Page after successful registration
    else:
        form = OwnerInfoForm()

    return render(request, 'html/owner_info.html', {'form': form})

@login_required
def pet_info(request):
    pet_profile, created = PetProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = PetInfoForm(request.POST, request.FILES, instance=pet_profile)
        if form.is_valid():
            form.save()  # フォームのデータをPetProfileに保存します。
            return redirect('mypage')  # マイページへリダイレクトします。
    else:
        form = PetInfoForm(instance=pet_profile)  # フォームを初期化します。
        
        # モデルインスタンスから表示用の値を取得
    gender_display = pet_profile.get_gender_display()
    vaccination_display = pet_profile.get_vaccination_display()
    neutered_display = pet_profile.get_neutered_display()

    context = {
        'form': form,
        'gender_display': gender_display,
        'vaccination_display': vaccination_display,
        'neutered_display': neutered_display,
    }

    return render(request, 'html/pet_info.html', {'form': form})

@login_required
def blog(request):
    return render(request, 'html/blog.html')

@login_required
def new_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # 投稿者を設定する場合
            post.save()
            return redirect('blog_posts')  # ブログ記事一覧ページへリダイレクト
    else:
        form = BlogPostForm()

    return render(request, 'html/new_post.html', {'form': form})

def blog_posts(request):
    post_list = BlogPost.objects.all()
    paginator = Paginator(post_list, 5) # 1ページに5項目を表示

    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'html/blog_posts.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'html/post_detail.html', {'post': post})

@login_required
def chat(request):
    chat_rooms = ChatRoom.objects.all()  # すべてのチャットルームを取得
    return render(request, 'html/chat.html', {'chat_rooms': chat_rooms})

@login_required
def new_chat_room(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            chat_room = form.save()
            return redirect('chat_room', chat_room.id)  # チャットルームの詳細ページへリダイレクト
    else:
        form = ChatRoomForm()

    return render(request, 'html/new_chat_room.html', {'form': form})

@login_required
def chat_room(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    # ここでのメッセージ取得順を変更
    messages = ChatMessage.objects.filter(room=room).order_by('timestamp')  # 古い順にする
    return render(request, 'html/chat_room.html', {'room': room, 'messages': messages})


@require_POST
def send_chat_message(request, room_id):
    room = get_object_or_404(ChatRoom, id=room_id)
    message = request.POST.get('message', '').strip()
    if message:
        ChatMessage.objects.create(room=room, user=request.user, message=message)
    return redirect('chat_room', room_id=room_id)

@login_required
def adoption(request):
    # `post_date`の代わりに`created_at`を使用してフィルタリング
    new_posts = AdoptionPost.objects.filter(created_at__gte=timezone.now()-timezone.timedelta(days=30)).order_by('-created_at')
    paginator = Paginator(new_posts, 4)  # 1ページあたり4つの投稿を表示
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'html/adoption.html', {'page_obj': page_obj})

@login_required
def new_adoption(request):
    query = request.GET.get('query', '')
    if query:
        # クエリがある場合、フィルタリングされた投稿を取得
        posts_list = AdoptionPost.objects.filter(
            Q(pet_type__icontains=query) | 
            Q(pet_breed__icontains=query) | 
            Q(address__icontains=query) | 
            Q(reason__icontains=query)
        ).distinct().order_by('-created_at')
    else:
        # クエリがない場合、全ての投稿を取得
        posts_list = AdoptionPost.objects.all().order_by('-created_at')

    paginator = Paginator(posts_list, 4)  # 1ページあたり4つの投稿を表示する設定
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    is_empty = not page_obj.object_list

    context = {
        'page_obj': page_obj,
        'is_empty': is_empty,
        'query': query
    }
    

    return render(request, 'html/new_adoption.html', {'page_obj': page_obj})

# 里親募集投稿ページを表示するビュー
def post_adoption(request):
    # POSTリクエストの場合、フォームのデータを処理
    if request.method == 'POST':
        return post_adoption_submit(request)
    # GETリクエストの場合、空のフォームを表示
    else:
        return render(request, 'html/post_adoption.html')

@login_required
def post_adoption_submit(request):
    if request.method == 'POST':
        pet_type = request.POST.get('pet_type')
        pet_breed = request.POST.get('pet_breed')
        gender = request.POST.get('pet_gender') 
        birth_date = request.POST.get('pet_birthday')
        vaccinated = request.POST.get('vaccination') == 'Yes'
        neutered = request.POST.get('neutering') == 'Yes'
        address = request.POST.get('address')
        reason = request.POST.get('adoption_reason')
        contact_info = request.POST.get('adoption_contact_info')
        photo = request.FILES.get('pet_photo')

        AdoptionPost.objects.create(
            pet_type=pet_type, pet_breed=pet_breed, gender=gender, birth_date=birth_date,
            vaccinated=vaccinated, neutered=neutered, address=address, reason=reason, contact_info=contact_info, photo=photo
        )

        return redirect('new_adoption')
    else:
        return redirect('post_adoption')
    
def adoption_post_detail(request, post_id):
    post = get_object_or_404(AdoptionPost, pk=post_id)
    return render(request, 'html/adoption_post_detail.html', {'post': post})

    
@login_required
def nutrition(request):
    return render(request, 'html/nutrition.html')

@login_required
def nutrition_symptoms(request):
    symptom_query = request.GET.get('symptom', '')
    if symptom_query:
        # Assuming 'symptom' is saved in the database as the first element of the tuple in SYMPTOM_CHOICES
        symptom_value = next((value for value, name in SYMPTOM_CHOICES if name == symptom_query), None)
        if symptom_value:
            nutrition_posts = NutritionPost.objects.filter(symptom=symptom_value)
        else:
            nutrition_posts = NutritionPost.objects.none()
    else:
        nutrition_posts = NutritionPost.objects.none()

    return render(request, 'html/nutrition_symptoms.html', {
        'symptom': symptom_query,
        'nutrition_posts': nutrition_posts,
    })
@login_required
def nutrition_post_submit(request):
    if request.method == 'POST':
        form = NutritionPostForm(request.POST, request.FILES)
        if form.is_valid():
            nutrition_post = form.save(commit=False)
            nutrition_post.user = request.user
            nutrition_post.save()
            messages.success(request, '栄養管理情報を投稿しました。')
            return redirect('nutrition')
        else:
            messages.error(request, '投稿に失敗しました。入力内容を確認してください。')
    else:
        form = NutritionPostForm()

    return render(request, 'html/nutrition_post.html', {'form': form})

@login_required
def nutrition_post(request):
    form = NutritionPostForm()
    return render(request, 'html/nutrition_post.html', {'form': form})