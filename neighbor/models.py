from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'images/', blank=True)
    contact = models.CharField(max_length=10)
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

class Areacode(models.Model):
    locality = models.CharField(
        max_length=30, default="e.g Metroplois, Gotham, Starcity etc")
    name = models.CharField(max_length=30)
    occupants_count = models.IntegerField(default=0, blank=True)
    user_profile = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='hoods', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    

    @classmethod
    def search_Areacode_by_name(cls, search_term):
        Areacodes = cls.objects.filter(name__icontains=search_term)
        return Areacodes

    @classmethod
    def one_Areacode(cls, id):
        Areacode = Areacode.objects.filter(id=id)
        return Areacode

    @classmethod
    def all_Areacodes(cls):
        Areacodes = cls.objects.all()
        return Areacodes



    @classmethod
    def get_Areacode_by_id(cls, id):
        Areacode = Areacode.objects.filter(id=Areacode.id)
        return Areacode

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile