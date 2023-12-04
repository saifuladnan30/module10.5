from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    d = {
            'id': 1,
            'name': 'Saiful Adnan',
            'self': "i'am Saiful. i love Bangladesh",
            'age': 24,
            'today': datetime.now(),
            'nationality': 'Bangladeshi',
            'nid':"",
            'about': 'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has',
            'lst':['a', 'b', 'c'],
            'test': ['States', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']],
            'message': 3,
        }
    return render(request, 'home.html', d)

def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')