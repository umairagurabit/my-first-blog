from django import forms

from .models import Post, Comment, CV_list

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class CV_Form(forms.ModelForm):

    class Meta:
        model = CV_list
        fields = ('title', 'researches', 'education', 'work_experience', 'reference', 'technical_skills',)
