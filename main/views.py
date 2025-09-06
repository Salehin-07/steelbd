from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from .models import *

# Create your views here.

def home(request):
  
  info = Information.objects.all()
  question = Question.objects.all()
  services = Service.objects.all()
  contacts = Contact.objects.all()
  social_media = SocialMedia.objects.all()
  video = Video.objects.all()
  context = {
    'information':info,
    'questions': question,
    "services":services,
    "team_members":team,
    "contacts":contacts,
    "social_media":social_media,
    "video":video,
  }
  
  return render(request, "index.html", context)

def about(request):
  
  info = Information.objects.all()
  question = Question.objects.all()
  contacts = Contact.objects.all()
  social_media = SocialMedia.objects.all()
  context = {
    'information':info,
    'questions': question,
    "contacts":contacts,
    "social_media":social_media,
  }
  
  return render(request, "about.html", context)

def service(request):
  
  services = Service.objects.all()
  question = Question.objects.all()
  contacts = Contact.objects.all()
  social_media = SocialMedia.objects.all()
  context = {
    "services":services,
    'questions': question,
    "contacts":contacts,
    "social_media":social_media,
  }
  
  return render(request, "service.html", context)

def team(request):
  
  team = Team.objects.all()
  contacts = Contact.objects.all()
  social_media = SocialMedia.objects.all()
  context = {
    "team_members":team,
    "contacts":contacts,
    "social_media":social_media,
  }
  return render(request, "team.html", context)

def projects(request):
  
  projects = Projects.objects.all()
  contacts = Contact.objects.all()
  social_media = SocialMedia.objects.all()
  context = {
    "projects":projects,
    "contacts":contacts,
    "social_media":social_media,
  }
  return render(request, "portfolio.html", context)

def contact(request):
  
  if request.method == "POST" :
    name = request.POST.get("name")
    email = request.POST.get("email")
    subject = request.POST.get("subject")
    message = request.POST.get("message")
    
    contact_message = ContactMessage(name=name, email=email, subject=subject, description=message)
    contact_message.save()
    
    return redirect("home")
  
  contacts = Contact.objects.all()
  social_media = SocialMedia.objects.all()
  context = {
    "contacts":contacts,
    "social_media":social_media,
  }
  return render(request, "contact.html", context)

# show_contact_message pages

def show_contact_message(request):
    # Only get unchecked messages
    contact_message = ContactMessage.objects.filter(status='unchecked').order_by('-id')
    contacts = Contact.objects.all()
    social_media = SocialMedia.objects.all()
    context = {
        "contact_message": contact_message,
        "contacts":contacts,
        "social_media":social_media,
    }
    return render(request, "show_contact_message.html", context)

@require_POST
def toggle_message_status(request, message_id):
    """
    AJAX endpoint to toggle message status from unchecked to checked
    """
    try:
        message = ContactMessage.objects.get(id=message_id)
        
        # Parse JSON data from request body
        data = json.loads(request.body)
        new_status = data.get('status', 'checked')
        
        # Update the status
        message.status = new_status
        message.save()
        
        return JsonResponse({
            'success': True,
            'message': f'Message status updated to {new_status}',
            'new_status': new_status
        })
        
    except ContactMessage.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Message not found'
        }, status=404)
        
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)
