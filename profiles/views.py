from django.shortcuts import render

# Create your views here.
# create profile view returns html template
def profile(request):
    """ Display the user's profile. """
    
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)