from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):

    peoples = [
        {'name' : 'Dharmendra Singh', 'age' : 20},
        {'name' : 'Abhishek Yadav', 'age' : 21},
        {'name' : 'Raj Prajapati', 'age' : 19},
        {'name' : 'Sachin Kurmi', 'age' : 20},
        {'name' : 'Nikhil Ahirwar', 'age' : 19},
        {'name' : 'Vikas Nath', 'age' : 21},
        {'name' : 'Harsh Rajput', 'age' : 13}
    ]

    # for people in peoples:
    #     print(peoples)

    return render(request , "index.html",context={'peoples':peoples})

def about(request):
    ab="<h1>This is about page</h1>"
    return HttpResponse(ab)