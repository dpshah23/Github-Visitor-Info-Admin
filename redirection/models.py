from django.db import models

class Users_main(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=120, unique=True)
    password = models.CharField(max_length=120)
    unique_link = models.CharField(max_length=255, unique=True)
    github_username = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True,blank=True)


    class Meta:
        db_table = 'Users_main'

    def __str__(self):
        return self.email

    
class Visits(models.Model):
    id = models.AutoField(primary_key=True)
    unique_link = models.CharField(max_length=200)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Visits'
    
    def __str__(self):
        return self.unique_link
    