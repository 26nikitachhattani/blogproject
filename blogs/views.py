from django.shortcuts import render , redirect , HttpResponseRedirect, get_object_or_404
from blogs.forms import ImageForm, CommentForm
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.forms import AuthenticationForm
from blogs.models import blog, CommentModel
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404
from django.core.mail import send_mail 
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from profiles.models import Profile

# Create your views here.

def likeview(request, likeid):
    post = get_object_or_404(blog, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    #post.likes.add(request.user)
    post.save()
    return HttpResponseRedirect(reverse('postdetail', args=[str(likeid)]))


@login_required(login_url="signin")
def feed_show(request):
    feeds = blog.objects.all().exclude(user= request.user).order_by('-date')
    
    pros = Profile.objects.get(user=request.user)
    followed = pros.following.all()
    print(feeds)
    fol = []

    #users = [user for user in pros.following.all()]

    for feed in feeds:
        if feed.user in pros.following.all():
            follow = "yes"
            fol.append(follow)

        else:
            follow = "No"
            fol.append(follow)
          
    
    return render(request,'feed.html', {'feeds': feeds, 'pros': pros, 'follow':follow,'fol':fol})


# sigup for user.
def signup(request):
    if request.method == 'POST':
        #fm = User_registration(request.POST)
        #if fm.is_valid():
        nm=request.POST["name"]
        fnm=request.POST["firstname"]
        num=request.POST["number"]
        em=request.POST["email"]
        pw=request.POST["pass"]
        if User.objects.filter(username=nm).exists():
            messages.info(request,'username taken')
            return redirect('/signup')
        elif User.objects.filter(email=em).exists():
            messages.info(request,'email taken')
            return redirect('/signup')
        else:
            user=User.objects.create_user(username=nm, password=pw, email=em, first_name=fnm, last_name=num)
            user.save()
        subject = 'welcome to CHANNEL world'
        message = f'Hi {user.username}, thank you for registering in CHANNEL STORIES. share your stories with us'
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = [user.email, ] 
        send_mail( subject, message, email_from, recipient_list )
        return HttpResponseRedirect('/')
    else:
        return render(request,'signup.html')

@login_required(login_url="signin")
def post_detail(request,_id,**kwargs):
    try:
        data =blog.objects.get(id =_id)
        liked = False
        if data.likes.filter(id=request.user.id).exists():
            liked = True
        post_is_liked = liked

        post_likes = data.likes.count()
        comments = CommentModel.objects.filter(blog = data)
    except blog.DoesNotExist:
        raise Http404('Data does not exist')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            #Comment = CommentModel(your_name= form.cleaned_data['your_name'],
            #comment_text=form.cleaned_data['comment_text'],
            #blog=data)
            #Comment.save()
            Comment = CommentModel(your_name= request.user,
            comment_text=form.cleaned_data['comment_text'],
            blog=data)
            Comment.save()
            return redirect(f'/postdetail/{_id}')
    else:
        form = CommentForm()
    context = {
            'post_is_liked':post_is_liked,
            'post_likes':post_likes,
            'data':data,
            'form':form,
            'comments':comments,
        }
    return render(request,'postdetail.html',context)
     

#profile
def profile_view(request):
    return render(request,'profile.html')

#profile

#blogdetail
@login_required(login_url="signin")
def BlogDetailView(request,_id):
    try:
        data =blog.objects.get(id =_id)
        comments = CommentModel.objects.filter(blog = data)
    except blog.DoesNotExist:
        raise Http404('Data does not exist')
     
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = CommentModel(your_name= request.user,
            comment_text=form.cleaned_data['comment_text'],
            blog=data)
            Comment.save()
            return redirect(f'/blog/{_id}')
    else:
        form = CommentForm()
    context = {
            'data':data,
            'form':form,
            'comments':comments,
        }
    return render(request,'detailview.html',context)
#blogdetail

@login_required(login_url="signin")
def post(request):
    pros = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit = False)
            obj.user = request.user
            obj.save()
            return HttpResponseRedirect('/')
    else:
        form = ImageForm()
        return render(request,'postblog.html' ,{'form':form ,'pros':pros})


# signin/login for user.
def signin(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['username']
            pw = fm.cleaned_data['password']
            user = authenticate(username=nm, password=pw)
            if user is not None:
                print("user", user)
                login(request, user)
                if request.GET.get('next',None):
                   return HttpResponseRedirect(request.GET['next'])
                return HttpResponseRedirect('/')
        else:
            messages.info(request,'invalid credential')
            return redirect('/signin')
    else:
        fm = AuthenticationForm()
        return render(request,'signin.html' ,{'form':fm})
    
# signin/logout for user
def signout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')