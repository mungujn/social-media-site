from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import generic

from Profile.models import Profile


@login_required(login_url='home/login')
def home(request):
    template_name = 'Home/home.html'
    prof = get_object_or_404(Profile, user__username=request.user.username)

    #info that appears on the home page
    try:
        friends = prof.friends.objects.all()[:5]
        posts = prof.posts.objects.all()[:5]
    except AttributeError:
        friends = None
        posts = None

    return render(request, template_name, {'profile':prof,'posts':posts,'friends':friends})


def contact(request):
    return HttpResponse("Not Implemented yet !")


def about(request):
    return HttpResponse("Not Implemented yet !")

