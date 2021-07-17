from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower()!='z':
        raise forms.ValidationError('Name Needs to start with Z')



class FormName(forms.Form):
    name=forms.CharField(validators=[check_for_z])
    email_ID=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)


    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    #def clean_botcatcher(self):
        #botcatcher=self.cleaned_data['botcatcher']
        #if len(botcatcher)>0:
            #raise forms.ValidationError("GOTCHA!")
        #return botcatcher                              ------> only for reference, in actuality we'll use built in
                                                                #validations
