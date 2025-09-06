from django.db import models

# Create your models here.

# home + about page models

class Information(models.Model):
  workers = models.IntegerField(default=0)
  clients = models.IntegerField(default=0)
  completed_projects = models.IntegerField(default=0)
  running_projects = models.IntegerField(default=0)
  
  class Meta:
    verbose_name = "Information"
    verbose_name_plural = "Information"
  
  def __str__(self):
    return f"Workers: {self.workers}, Clients: {self.clients}"
  
# home + about + Service page models

class Question(models.Model):
  question = models.CharField(max_length=250)
  answer = models.TextField()
  
  class Meta:
    verbose_name = "Question"
    verbose_name_plural = "Questions"
  
  def __str__(self):
    return self.question

# home + Service page models

class Service(models.Model):
  img_url = models.URLField()
  title = models.CharField(max_length=140)
  description = models.TextField()
  
  class Meta:
    verbose_name = "Service"
    verbose_name_plural = "Services"
  
  def __str__(self):
    return self.title


# team page models

class Team(models.Model):
  img_url = models.URLField()
  name = models.CharField(max_length=50)
  position = models.CharField(max_length=50)
  facebook_link = models.URLField(null=True, blank=True)
  twitter_link = models.URLField(null=True, blank=True)
  linkdin_link = models.URLField(null=True, blank=True)
  instagram_link = models.URLField(null=True, blank=True)
  
  class Meta:
    verbose_name = "Team Member"
    verbose_name_plural = "Team Members"
  
  def __str__(self):
    return f"{self.name} - {self.position}"


# projects page

class Projects(models.Model):
    STATUS_CHOICES = (
        ('complete', 'Complete'),
        ('running', 'Running'),
        ('upcoming', 'Upcoming')
    )
    
    img_url = models.URLField()
    title = models.CharField(max_length=140)
    description = models.TextField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    
    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return f"{self.title} ({self.status})"


# for contact page + footer(all-page)
class Contact(models.Model):
  location = models.CharField(max_length=100)
  phone = models.CharField(max_length=15)
  email = models.EmailField()
  
  class Meta:
    verbose_name = "Contact"
    verbose_name_plural = "Contacts"
  
  def __str__(self):
    return f"{self.location} - {self.phone}"


# for contact and show_contact_message pages
class ContactMessage(models.Model):
    STATUS_CHOICES = (
        ("checked", "Checked"),
        ("unchecked", "Unchecked")
    )
    
    name = models.CharField(max_length=140)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default="unchecked"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']  # Most recent first
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"
    
    def __str__(self):
        return f"{self.name} - {self.subject} ({self.status})"
    
    @property
    def is_checked(self):
        return self.status == 'checked'
    
    @property
    def is_unchecked(self):
        return self.status == 'unchecked'


# for footer(all-page)
class SocialMedia(models.Model):
  name = models.CharField(max_length=30)
  logo_class = models.CharField(max_length=20)
  link = models.URLField()
  
  class Meta:
    verbose_name = "Social Media"
    verbose_name_plural = "Social Media"
  
  def __str__(self):
    return self.name

#for home page(video):
class Video(models.Model):
  link = models.URLField()
  
  class Meta:
    verbose_name = "Video"
    verbose_name_plural = "Videos"
  
  def __str__(self):
    return f"Video: {self.link}"