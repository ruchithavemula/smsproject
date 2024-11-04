from django.db import models
from django.contrib.auth.models import User  # Only import User if you're using Django's default User model


class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class StudentList(models.Model):
    Register_Number = models.CharField(max_length=20, unique=True)
    Name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  # Only use Django's User here if needed

    def __str__(self):
        return f'{self.Name} ({self.Register_Number})'


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    average_sales = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"File uploaded on {self.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')}"
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)  # Adjust the max_length as needed
    address = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name