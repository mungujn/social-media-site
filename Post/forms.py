from django import forms

from Post.models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField(label="Text", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'control-label', 'name': 'text','placeholder':'Whats on your mind'}))
    class Meta:
        model = Post
        fields = ('text', 'image')