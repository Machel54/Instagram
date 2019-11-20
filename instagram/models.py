from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length =30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    
    def __str__(self):
        return self.user_name
    class Meta:
        ordering = ['user_name']
    def save_user(self):
        self.save()
    
class tags(models.Model):
    name = models.CharField(max_length= 20)
    
    def __str__(self):
        return self.name
   
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    bio = models.TextField(default="Hello Friends")
    
    def __str__(self):
        return f'{self.user.username}'
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
    def delete_profile(self):
        self.delete()
        
    def comment(self, photo, text):
        Comment(text=text, photo=photo, user=self).save()
        
    @classmethod
    def search_by_user(cls,search_term):
        profiles = cls.objects.filter(user__name__icontains=search_term)
        return profiles
    
    def post(self, form):
        image = form.save(commit=False)
        image.user = self
        image.save()
        
        
    class Meta:
        ordering = ['user']
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        
    @property
    def all_comments(self):
        return self.comments.all()
    
    
class NewsletterRecipients(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()