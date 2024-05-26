from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt
import africastalking
from django.contrib import messages

# Initialize Africastalking
username = "sandbox"
api_key = '5ee2153c399094599f3eeab6149e107d4374f7dd2337fce90959d0210a6d5ad8'
africastalking.initialize(username, api_key)
sms = africastalking.SMS

# Create your views here.
def home(request):
    slides = Slide.objects.all()
    featured_event = FeaturedEvent.objects.first()
    videos = Video.objects.all()
    gallery_items = GalleryItem.objects.all()
    blog_posts = BlogPost.objects.all()
    events = Event.objects.all().order_by('date')
    services = Service.objects.all()

    context = {
        'slides': slides,
        'featured_event': featured_event,
        'videos': videos,
        'gallery_items': gallery_items,
        'blog_posts': blog_posts,
        'events': events,
        'services':services
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def news_detail(request, blog_id):
    blog = get_object_or_404(BlogPost, id=blog_id)

    context = {
        'blog':blog
    }

    return render(request, 'details.html', context)

def services(request):
    services = Service.objects.all()

    context = {
        'services':services
    }
    return render(request, 'services.html', context)

def events(request):
    videos = Video.objects.all()
    gallery_items = GalleryItem.objects.all()

    context = {
        'videos': videos,
        'gallery_items': gallery_items,
    }
    return render(request, 'events.html', context)

def contact(request):
    
    return render(request, 'contact.html')

@csrf_exempt
def send_sms(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        location = request.POST.get('location')
        service = request.POST.get('service')
        message = request.POST.get('message')

        # Create the SMS message
        sms_message = f"Name: {name}\nPhone: {phone}\nEmail: {email}\nLocation: {location}\nService: {service}\nMessage: {message}"

        recipients = ["+255719807543",]
        # Send the SMS
        try:
            sender = "GEITATECH"
            response = sms.send(sms_message, recipients, sender)
            messages.success(request, "Your message has been sent successfully!")
            print("SMS Response:", response)
        except Exception as e:
            messages.error(request, f"Error sending message: {e}")
            print(f"Error sending SMS: {e}")

        return redirect('contact')  # Redirect to a thank you page after submission

    return send_sms