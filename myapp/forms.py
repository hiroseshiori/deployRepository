
from django import forms
from tempus_dominus.widgets import DatePicker
from .models import PetProfile
from .models import BlogPost
from .models import ChatRoom
from .models import UserReview, NutritionQuestion
from .models import NutritionPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='ユーザー名',
        max_length=150,
        help_text='半角アルファベット、半角数字、@/./+/-/_ で150文字以下にしてください。',
        error_messages={
            'invalid': "半角アルファベット、半角数字、@/./+/-/_ で150文字以下にしてください。",
            'required': "ユーザー名は必須です。",
            'max_length': "ユーザー名は150文字以下にしてください。",
        }
    )

    def clean_username(self):
        username = self.cleaned_data.get('username', '')  # usernameがNoneの場合は空文字を返す
        pattern = r'^[\w@\.\+\-/_]+$'
        if not re.fullmatch(pattern, username):
            raise forms.ValidationError(
                "半角アルファベット、半角数字、@/./+/-/_ で150文字以下にしてください。"
            )
        return username

class OwnerInfoForm(forms.Form):
    name = forms.CharField(label='名前', max_length=100, required=True)
    icon = forms.ImageField(label='アイコン設定', required=False)
    location = forms.CharField(label='居住地', max_length=100, required=True)

class PetInfoForm(forms.ModelForm):
    class Meta:
        model = PetProfile
        fields = ['name', 'icon', 'species', 'breed', 'gender', 'birthdate', 'vaccination', 'neutered']
        widgets = {
            'gender': forms.Select(choices=PetProfile.GENDER_CHOICES),
            'vaccination': forms.Select(choices=PetProfile.VACCINATION_CHOICES),
            'neutered': forms.Select(choices=PetProfile.NEUTERED_CHOICES),
            'birthdate': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
        labels = {
            'name': '名前',
            'icon': 'アイコン設定',
            'species': '種別',
            'breed': '品種',
            'gender': '性別',
            'birthdate': '生年月日',
            'vaccination': 'ワクチン接種',
            'neutered': '不妊・去勢手術',
        }
        
    
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'image']

        
class ChatRoomForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ['name']
        labels = {
            'name': 'チャットルーム名',
        }
        
class NutritionPostForm(forms.ModelForm):
    class Meta:
        model = NutritionPost
        fields = ['symptom', 'product_name', 'description', 'photo', 'rating']