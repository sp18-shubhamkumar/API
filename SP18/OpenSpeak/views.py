from django.shortcuts import render
from .models import Speak
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import Speakforms,user_Regs_form
# Create your views here.
def index(request):
    return render(request,'index.html')

def Speak_list(request):
    speaks=Speak.objects.all().order_by('-created_at')
    for i in speaks:
        print(i.text,i.id)
    return render(request,'Speak_list.html',{'speaks':speaks})
@login_required
def speak_create(request):
    if request.method == "POST":
        form=Speakforms(request.POST,request.FILES)
        if form.is_valid():
            speak=form.save(commit=False)
            speak.user=request.user
            speak.save()
            return redirect("Speak_list")
    else:
        form=Speakforms()
    return render(request,'speak_form.html',{'form':form})
@login_required
def speak_edit(request,speak_id):
    speak=get_object_or_404(Speak,pk=speak_id,user=request.user)

    if(request.method=='POST'):
        form=Speakforms(request.POST, request.FILES,instance=speak)
        if form.is_valid():
            speak=form.save(commit=False)
            speak.user=request.user
            speak.save()
            return redirect('Speak_list')
    else:
        form=Speakforms(instance=speak)
    return render(request, 'speak_form.html',{'form':form})
@login_required
def speak_delete(request,speak_id):
    speak=get_object_or_404(Speak,pk=speak_id,user=request.user)
    if request.method == 'POST':
        speak.delete()
        return redirect('Speak_list')
    return render(request, 'speak_confirm_delete.html',{'speak':speak})

def register(request):
    if request.method == 'POST':
        form = user_Regs_form(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('Speak_list')
    else:
        form=user_Regs_form()
    return render(request, 'registration/register.html',{'form':form})


