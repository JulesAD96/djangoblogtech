from django import forms
from django.contrib.auth.models import User

from siteapp.models import Comment, Contact

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ["body_comment"]
        widgets = {
            'body_comment': forms.Textarea(attrs={'cols': 5, 'rows': 5}),
        }
       

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


    