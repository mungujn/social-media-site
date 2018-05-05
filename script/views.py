from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from script.forms import NameForm
from script.models import Names


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check form validity
        if form.is_valid():
            # process cleaned data
            x = Names(name=form.cleaned_data['your_name'])
            x.save()
            #redirect to a new URL:
            return HttpResponseRedirect('/admin/script/names/')

    else:
        form = NameForm()

    return render(request, 'script/form_html.html', {'form':form})