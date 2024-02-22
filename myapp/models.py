from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.db import models
from django.utils import timezone
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='icons/', null=True, blank=True)
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    location = models.CharField(max_length=255)
    
    def __str__(self):
        return self.user.username
   
class PetProfile(models.Model):
    GENDER_CHOICES = [
    ('male', 'オス'),
    ('female', 'メス'),
    ]

    VACCINATION_CHOICES = [
    ('yes', '接種済み'),
    ('no', '未接種'),
    ]

    NEUTERED_CHOICES = [
        ('yes', '去勢・避妊済み'),
        ('no', '未去勢・未避妊'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='pet_icons/', blank=True, null=True)
    species = models.CharField(max_length=255)
    breed = models.CharField(max_length=255)
    birthdate = models.DateField(null=True, blank=True, default=None)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    vaccination = models.CharField(max_length=3, choices=VACCINATION_CHOICES)
    neutered = models.CharField(max_length=3, choices=NEUTERED_CHOICES)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='followers', blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return self.user.username
    
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images', null=True, blank=True)

def __str__(self):
    return f"{self.title} by {self.author.get_full_name() or self.author.username}"
    
class ChatRoom(models.Model):
    name = models.CharField(max_length=255)  # チャットルームの名前フィールドを追加

    def __str__(self):
        return self.name
    
class ChatMessage(models.Model):
    room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'


class AdoptionPost(models.Model):
    pet_type = models.CharField(max_length=255)
    pet_breed = models.CharField(max_length=255, blank=True)
    gender = models.CharField(max_length=50)
    birth_date = models.DateField()
    vaccinated = models.BooleanField(default=False)
    neutered = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='pet_photos/', null=True, blank=True)
    address = models.CharField(max_length=255)  # 追加
    reason = models.TextField()  # 追加
    created_at = models.DateTimeField(auto_now_add=True)
    contact_info = models.TextField(verbose_name='問い合わせ先')  # 問い合わせ先のフィールドを追加


    def __str__(self):
        return self.pet_type


class NutritionItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    benefits = models.TextField()
    ingredients = models.TextField()

    def __str__(self):
        return self.name

class UserReview(models.Model):
    item = models.ForeignKey(NutritionItem, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s review of {self.item.name}"

class NutritionQuestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class NutritionAnswer(models.Model):
    question = models.ForeignKey(NutritionQuestion, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Answer to {self.question.title} by {self.user.username}"
    
SYMPTOM_CHOICES = [
    ('皮膚', '皮膚'),
    ('消化', '消化'),
    ('関節', '関節'),
    ('目と耳', '目と耳'),
    ('毛並み', '毛並み'),
    # その他の症状をここに追加
]    
   
class NutritionPost(models.Model):
    symptom = models.CharField(max_length=100, choices=SYMPTOM_CHOICES, blank=True)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='nutrition_photos/', null=True, blank=True)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)  # 投稿の日時

    def __str__(self):
        return self.product_name   