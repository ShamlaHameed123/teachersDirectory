from django.db import models

# Create your models here.
class Teachers(models.Model):

    first_name = models.CharField(max_length=50, db_column='First Name')
    last_name = models.CharField(max_length=50, db_column='Last Name')
    profile_picture = models.CharField(max_length=50, default="default_teacher.png", db_column='Profile picture')
    email_address = models.CharField(max_length=50, unique=True, db_column='Email Address')
    phone_number = models.CharField(max_length=17, db_column='Phone Number')
    room_number = models.CharField(max_length=5, db_column='Room Number')
    subject_taught = models.TextField(max_length=100, db_column='Subjects taught')

    def __str__(self):
        return self.first_name + " " + self.last_name
