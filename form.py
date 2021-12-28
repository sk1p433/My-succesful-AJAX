
from django import forms

from .models import Comment



class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('is_active','author','likes')
        #widgets = {'product': forms.HiddenInput}
