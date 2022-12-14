from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text" : "This is about me",
        "my_number" : 123,
        "my_list" : [12, 34, 56, "abc"]
    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})