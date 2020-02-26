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
    locality = models.CharField(max_length=30, default="e.g Metroplois, Gotham, Starcity etc")
    name = models.CharField(max_length=30)
    occupants_count = models.IntegerField(default=0, blank=True)
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='areas', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    

    @classmethod
    def search_areacode_by_name(cls, search_term):
        areacodes = cls.objects.filter(name__icontains=search_term)
        return areacodes

    @classmethod
    def one_areacode(cls, id):
        areacode = Areacode.objects.filter(id=id)
        return areacode

    @classmethod
    def all_areacodes(cls):
        areacodes = cls.objects.all()
        return areacodes



    @classmethod
    def get_areacode_by_id(cls, id):
        areacode = Areacode.objects.filter(id=Areacode.id)
        return areacode

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile


class Business(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=70, blank=True)
    biz_owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    biz_area = models.ForeignKey(Areacode, on_delete=models.CASCADE, related_name='biz', null=True)

    

    @classmethod
    def search_by_name(cls, search_term):
        businesses = cls.objects.filter(name__icontains=search_term)
        return businesses

    @classmethod
    def get_areacode_businesses(cls, areacode_id):
        businesses = Business.objects.filter(areacode_id=id)
        return businesses

    @classmethod
    def get_area_biz(cls, biz_area):
        businesses = Business.objects.filter(biz_area_pk=biz_area)
        return businesses

    @classmethod
    def get_profile_businesses(cls, profile):
        businesses = Business.objects.filter(biz_owner__pk=profile)
        return businesses


class Join(models.Model):
    '''
    Updating user location each time they join or leave a neghborhood	
    '''
    user_id = models.OneToOneField(User)
    area_id = models.ForeignKey(Areacode)

    def __str__(self):
        return self.user_id


class Post(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.CharField(max_length=30)
    poster = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post_area = models.ForeignKey(Areacode, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)

    

    @classmethod
    def search_post(cls, search_term):
        posts = cls.objects.filter(name__icontains=search_term)
        return posts

    @classmethod
    def get_area_posts(cls, post_area):
        posts = Post.objects.filter(post_area=id)
        return posts

    @classmethod
    def search_by_name(cls, search_term):
        posts = cls.objects.filter(name__icontains=search_term)
        return posts

    @classmethod
    def all_posts(cls,id):
        posts = Post.objects.all()
        return posts
