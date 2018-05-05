from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from Profile.forms import ProfileForm
from controller import ProfileInterface, getProfile, getFriends


def createProfileView(request):
    template_name = 'profile/create-profile.html'

    if request.method == 'POST':
        registration_form = ProfileForm(request.POST)
        interface = ProfileInterface()

        if registration_form.is_valid():
            interface.createUserProfile(registration_form.cleaned_data)

            if 'profile_picture' in request.FILES:
                interface.addPictureToProfile(request.FILES['profile_picture'])

            return redirect('/login')

        # Invalid form Print problems to the terminal They'll also be shown to the user.
        else:
            # print registration_form.errors
            return render(request, template_name, {'form': registration_form})

    else:
        registration_form = ProfileForm()

    # Render the template depending on the context.
    return render(request, template_name, {'form': registration_form})


def viewProfile(request, username):
    profile = getProfile(username)
    friends = getFriends()
    template_name = 'profile/view-profile.html'

    if request.user.username == username:
        current_user = True
        return render(request, template_name, {'profile':profile,'current_user':current_user,'friends':friends})

    else:
        current_user = False
        return render(request, template_name, {'profile':profile,'current_user':current_user,'friends':friends})


@login_required(login_url='home/login')
def edit(request):
    template_name = 'profile/create-profile.html'
    profile = getProfile(request.user.username)
    if profile is None:
        return HttpResponse("No Profile Found")
    else:
        if request.method == 'POST':
            registration_form = ProfileForm(request.POST)
            interface = ProfileInterface()

            if registration_form.is_valid():
                interface.createUserProfile(registration_form.cleaned_data)

                if 'profile_picture' in request.FILES:
                    interface.addPictureToProfile(request.FILES['profile_picture'])

                return redirect('/login')

            # Invalid form Print problems to the terminal They'll also be shown to the user.
            else:
                # print registration_form.errors
                return render(request, template_name, {'form': registration_form})
        else:
            user_data = {
                'first_name':profile.user.first_name,
                'last_name': profile.user.last_name,
                'username':profile.user.username,
                'bio':profile.bio,
                'school':profile.school,
                'work':profile.work,
                'location':profile.location,
                'email':profile.email
            }
            profile_form = ProfileForm(user_data)

        # Render the template depending on the context.
        return render(request, template_name, {'profile_form': profile_form})


def all(request):
    return HttpResponse("Not Implemented yet !")


def addFriend(request):
    return HttpResponse("Not Implemented yet !")
