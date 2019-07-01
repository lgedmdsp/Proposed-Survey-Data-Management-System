from django.forms import ModelForm
from django import forms
from .models import data,Photo
from django.contrib.auth.models import User



class BaseForm(ModelForm):
    #updated_by = forms.CharField(initial=User.username) 
    #updated_by = forms.ModelChoiceField(queryset=User.objects.distinct("username").all())

    class Meta:
       model = data
       fields = ['uniqueid','eduid','district','upazilla','s_union','mouza','village','sheltername','northing','easting','distance','expectedpopulation','waterlevel','pucca','semipucca','wooden','bamboo','thatched','shanty','total_house']




class PhotoForm(forms.ModelForm):
    
    shelterid = forms.CharField(max_length=200)
    class Meta:
        model = Photo        
        fields = ('shelterid','file', )