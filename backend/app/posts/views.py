from django.shortcuts import render


# Create your views here.
def home(request):
    """Define route for home Page."""
    return render(request, "posts/home.html")
