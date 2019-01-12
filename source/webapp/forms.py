from django import forms
from webapp.models import UserInfo, Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['author']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        exclude = ['friend', 'user']