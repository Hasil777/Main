from post.models import Post, Comment
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    password1=forms.CharField(label=' password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='repeat the password',widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email']
    def clean_password(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match")
        return cd['password2']
    
class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25) 
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user','text']
        
class SearchForm(forms.Form):
    query = forms.CharField()