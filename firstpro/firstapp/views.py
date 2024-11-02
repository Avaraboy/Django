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

    text="""Lorem, ipsum dolor sit amet consectetur adipisicing elit. Autem natus dignissimos explicabo harum, a, alias omnis aut eius, accusantium recusandae eveniet sit nobis numquam cupiditate. Eos ipsum aliquid ut facere? Dolorem nostrum reprehenderit veniam suscipit obcaecati dignissimos deserunt modi? Nam quos in, soluta et qui accusantium facere omnis explicabo laborum provident, excepturi magnam saepe? Aspernatur quas soluta expedita quos, adipisci nesciunt velit ut veniam modi consectetur voluptatum enim iusto, maiores exercitationem molestias ipsum consequuntur. Dolorum mollitia maiores consequatur labore inventore numquam tenetur, tempore fugit facilis. Voluptatem aliquid recusandae necessitatibus hic ullam ex laboriosam, magni, quasi eos, et corrupti excepturi quibusdam."""

    # for people in peoples:
    #     print(peoples)

    return render(request , "index.html",context={'peoples':peoples,'text':text})

def other(request):

    vegetables={'Pumpkin','Tomato','Potatao'}

    return render(request , "other.html",context={'vegetables':vegetables,'page':'other'})

def about(request):
    context = {'page':'about'}
    return render(request , "about.html",context)

def contact(request):
    context = {'page':'contact'}
    return render(request , "contact.html",context)