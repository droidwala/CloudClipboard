from django import forms
from django.contrib.auth.models import User
from login.models import Page,Category,UserProfile


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,help_text="Please enter Cateory name")
    #views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    #likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
    #slug = forms.SlugField(widget=forms.HiddenInput(),required=False)
    
    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    #title = forms.IntegerField(max_length=128,help_text="Enter title of Page..")
    url = forms.URLField(max_length=128,help_text="Enter URL")
    #views =forms.IntegerField(widget=forms.HiddenInput(),initial=0)

    class Meta:
        model = Page
        #fiels = ('url',)
        exclude = ('category',)       

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
    def save(self,commit=True):
        user = super(UserProfile,self).save(commit = False)
        user.email = self.cleaned_data['email']
        if commit:
            user.is_active = False
            user.save()

        return user

    class Meta:
        model = UserProfile
        fields = ('website','picture')
    
