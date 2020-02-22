from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'images/', blank=True)
    contact = CharField()
    email = models.EmailField(max_length=70, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls, id):
        profile = Profile.objects.get(user=id)
        return profile

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def find_profile(cls, search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user=id).first()
        return profile

    class Meta:
        ordering = ['user']

