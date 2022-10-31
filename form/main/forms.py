from django import forms
from django.forms import ModelForm
from . models import *

# class ProductForm(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField()


class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    roll_number = forms.IntegerField(help_text='enter your roll number')
    password = forms.CharField(widget=forms.PasswordInput())


# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = '__all__'


# class ProductForm(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField()
#     views = forms.IntegerField()
#     available = forms.BooleanField()

# class ProductForm(forms.Form):
#     title = forms.CharField(widget=forms.Textarea)
#     description = forms.CharField(widget=forms.CheckboxInput)
#     views = forms.IntegerField(widget=forms.TextInput)
#     available = forms.BooleanField(widget=forms.Textarea)


# class ProductForm(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField()
#     views = forms.IntegerField()
#     date = forms.DateField(widget=forms.SelectDateWidget)



# define the class of a form
# class PostForm(ModelForm):
# 	class Meta:
# 		model = Post	
# 		fields =["username", "gender", "text"]

# 	def clean(self):
# 		super(PostForm, self).clean()
# 		username = self.cleaned_data.get('username')
# 		text = self.cleaned_data.get('text')

# 		if len(username) < 5:
# 			self._errors['username'] = self.error_class([
# 				'Minimum 5 characters required'])
# 		if len(text) <10:
# 			self._errors['text'] = self.error_class([
# 				'Post Should Contain a minimum of 10 characters'])

# 		return self.cleaned_data



    
            
