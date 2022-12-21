from cProfile import label
from dataclasses import fields
from django import forms
from gallery.models import Artwork, Comment

class UploadForm(forms.ModelForm):
    class Meta:
        model = Artwork
        fields = ['image', 'subject', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        label = {
            'content': '댓글내용'
        }