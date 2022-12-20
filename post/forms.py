from django import forms
from . models import post, Category
choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)

class postform(forms.ModelForm):
    class Meta:
        model = post
        fields=('title','body','category','authour','thumbnail_des','header_image')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'authour':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'elder',"type":'hidden'}),
           # 'authour':forms.Select(attrs={'class':'form-control'}),
            'category':forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'thumbnail_des':forms.Textarea(attrs={'class':'form-control'}),
            #'header_image':forms.ImageInput(attrs={'class':'form-control'}),
           
        }

class editform(forms.ModelForm):
    class Meta:
        model = post
        fields=('title','body')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),   
        }