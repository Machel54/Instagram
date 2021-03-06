from django import forms
from .models import *

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
     
class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget=forms.TextInput()
        self.fields['text'].widget.attrs['placeholder']='Add comment..'
    
    class Meta:
        model = Comment
        fields = ('text',)
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user', 'pub_date')
        
class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget=forms.TextInput()
    class Meta:
        model = Profile
        fields = ('profile_image','first_name','last_name','bio' )