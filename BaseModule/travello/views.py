from django.shortcuts import render
from .models import Destination, Testimonial

def index(request):
    # return HttpResponse("Hello World")

    # dest1 = Destination()
    # dest1.name = "Dhaka"
    # dest1.desc = "I Love Bangladesh"
    # dest1.img = 'destination_1.jpg'
    # dest1.price = 900
    # dest1.offer = True

    # dest2 = Destination()
    # dest2.name = "Noakhali"
    # dest2.desc = "I Love Bangladesh"
    # dest2.img = 'destination_1.jpg'
    # dest2.price = 900
    # dest2.offer = False

    # dest3 = Destination()
    # dest3.name = "Jessor"
    # dest3.desc = "I Love Bangladesh"
    # dest3.img = 'destination_1.jpg'
    # dest3.price = 900
    # dest3.offer = True

    # dests = [dest1, dest2, dest3]
    # return render(request,"index.html", {'dests': dests},)
    # -------------------------------------------------------
    dests = Destination.objects.all()
    messages = Testimonial.objects.all()

    return render(request,"index.html", {'dests': dests,'messages': messages})