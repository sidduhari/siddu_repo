from django.shortcuts import render
from testapp.forms import EmployeeForm
# Create your views here.

def  home_view(request):
    return render(request,'testapp/home.html')
def about_view(request):
    return render(request,'testapp/about.html')

def login_view(request):
    form = EmployeeForm()
    submitted = False
    name = ''
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            print('Form validation success and printing feedback information')
            print('Name:',form.cleaned_data['name'])
            print('PHONE_NUMBER:',form.cleaned_data['phone_number'])
            submitted = True
            name = form.cleaned_data['name']
    return render(request,'testapp/form.html', {'form':form,'submitted':submitted,'name':name})

