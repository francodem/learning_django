from django.shortcuts import render, HttpResponse, render

html_base = """
    <h1>Mi web personal</h1>
    <ul>
        <li><a href="/">Home</li>
        <li><a href="/about">About</a></li>
        <li><a href="/portfolio">Portfolio</li>
        <li><a href="/contact">Contact</li>
    </ul>
"""


# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def about(request):
    return HttpResponse(request, 'core/about.html')


def portfolio(request):
    return HttpResponse("<h1>Portfolio</h1><h3>This is my current stack.</h2>")


def contact(request):
    return HttpResponse("<h1>Contact</h1><h3>This is mi email.</h2>")
