from django.shortcuts import render , redirect , HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.conf import settings
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.forms import AuthenticationForm
from blogs.models import blog, CommentModel
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.core.mail import send_mail 
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, UpdateView
from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Profile

# Create your views here.

def lists(request):
    return render(request,'profiles\list.html')


def error_404(request, exception):
        data = {}
        return render(request,'404.html', data)

def follow_unfollow_profile(request):
    if request.method=="POST":
        my_profile = Profile.objects.get(user=request.user)
        pk = request.POST.get('profile_pk')
        obj = Profile.objects.get(pk=pk)

        if obj.user in my_profile.following.all():
            my_profile.following.remove(obj.user)
        else:
            my_profile.following.add(obj.user)
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('profiles:profile-list-view')

class Editprofilepageview(UpdateView):
    model = Profile
    template_name = 'profiles/edit_profile_page.html'
    fields = ['bio','photo']
    success_url = reverse_lazy('/')

class Showprofileview(DetailView):
    model = Profile
    template_name = 'profiles/editprofile.html'

    def get_context_data(self, **kwargs):
        user = Profile.objects.all()
        context = super(Showprofileview,self).get_context_data(**kwargs)
        #view_profile = self.get_objects()
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        blogs = blog.objects.filter(user=page_user.user).count()
        #blogpost = blog.objects.filter(user=page_user)
        pro = Profile.objects.get(id=page_user.id)
        followingcount = pro.following.count() 
        
        #my_profile = Profile.objects.get(user=self.request.user)
        context['following'] =  followingcount
        context["page_user"] = page_user
        context["blogs"] = blogs
        return context


class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/main.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        return Profile.objects.all().exclude(user=self.request.user)

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/detail.html'


    def get_objects(self, **kwargs):
        pk = self.kwargs.get('pk')
    
        view_profile = Profile.objects.get(pk=pk)
        #view_profile = get_object_or_404(Profile, id=self.kwargs['pk'])
        return view_profile
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view_profile = self.get_objects()
        my_profile = Profile.objects.get(user=self.request.user)
        blogscount = blog.objects.filter(user=view_profile.user).count()
        blogs = blog.objects.filter(user=view_profile.user)
        if view_profile.user in my_profile.following.all():
            follow = True
        else:
            follow = False
        context["blogs"] = blogs
        context["blogscount"] = blogscount
        context["my_profile"] = my_profile
        context["follow"] = follow
        return context