from django.shortcuts import render
from basicapp import forms

def index(request):
     return render(request,'basicapp/index.html')

def form_name_view(request):
    form= forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email_ID'])
            print("TEXT: "+form.cleaned_data['text'])


    return render(request,'basicapp/forms_page.html',{'form':form})
# Create your views here.
