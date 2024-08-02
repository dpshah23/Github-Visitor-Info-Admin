from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Users_main(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=120, unique=True)
    password = models.CharField(max_length=120)
    unique_link = models.CharField(max_length=255, unique=True)
    github_username = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True,blank=True)


    class Meta:
        db_table = 'Users_main'

    def set_password(self, raw_password):
        self.password = make_password(raw_password)


    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

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
        # return f"{self.getusername()} visited from {self.city}, {self.state}, {self.country} at {self.timestamp}"
        return f"{self.city} from {self.country} at {self.timestamp} for {self.getusername()}"
    def getusername(self):
        return Users_main.objects.get(unique_link=self.unique_link).github_username