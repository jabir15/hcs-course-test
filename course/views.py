from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Standard, Subject, Chapter, Topic
from .forms import CustomUserCreationForm

# Create your views here.

def index(request):
    if request.method=='POST':
        if 'sign-up' in request.POST:
            loginform = AuthenticationForm()
            signupform = CustomUserCreationForm(request.POST)
            if signupform.is_valid():
                signupform.save()
                username = signupform.cleaned_data.get('username')
                raw_password = signupform.cleaned_data.get('password1')
                user = authenticate(username=username,password=raw_password)
                login(request,user)
                return redirect('home-page')
            tab = 'signup'

        if 'log-in' in request.POST:
            signupform = CustomUserCreationForm()
            loginform = AuthenticationForm(data=request.POST)
            if loginform.is_valid():
                user = loginform.get_user()
                login(request,user)
                return redirect('home-page')
            tab = 'login'
    else:
        signupform = CustomUserCreationForm()
        loginform = AuthenticationForm()
        tab = 'login'

    return render(request, 'course/login.html', {'signupform':signupform, 'loginform':loginform, 'tab':tab})




def get_home(request):
    standards = Standard.objects.all()
    response = render(request, 'course/homepage.html',{'standards':standards})
    return response

def subjects_by_class(request):
    if request.method=="POST":
        classID = request.POST.get('classID','')
        if classID == 'C00':
            subjects = Subject.objects.none()
        else:
            subjects = Subject.objects.filter(which_class__name=classID).order_by('name')

    return render(request, 'course/includes/subjectsbyclass.html', {'subjects':subjects})

def chapters_by_subject(request):
    if request.method=="POST":
        classID = request.POST.get('classID','')
        subjectID = request.POST.get('subjectID','')
        if classID == 'C00' or subjectID == 'None':
            chapters = Chapter.objects.none()
        else:
            chapters = Chapter.objects.filter(which_class__name=classID).filter(which_subject__name=subjectID).order_by('name')
    return render(request, 'course/includes/chaptersbysubject.html',{'chapters':chapters})

def topics_by_chapter(request):
    if request.method=="POST":
        classID = request.POST.get('classID','')
        subjectID = request.POST.get('subjectID','')
        chapterID = request.POST.get('chapterID','')
        chapterNumber = request.POST.get('chapterNumber','')

        topics = Topic.objects.filter(which_class__name=classID).filter(which_subject__name=subjectID).filter(which_chapter__name=chapterID)
    
    return render(
        request,
        'course/includes/topicsbychapter.html',
        {'topics':topics, 'chapterNumber':chapterNumber, 'chapterID':chapterID, 'classID':classID, 'subjectID':subjectID}
    )

