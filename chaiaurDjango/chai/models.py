from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('PG', 'PREMIUM GOLD'),
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHIE'),
        ('GR', 'GREEN'),
    ]
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name


# One To Many Relationship
class ChaiReview(models.Model):
    CHAI_RATING_CHOICE = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.CharField(max_length=2, choices=CHAI_RATING_CHOICE)
    comment = models.TextField(default='')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} Review For {self.chai.name}'
    

# Many To Many Relationship
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_variety = models.ManyToManyField(ChaiVarity, related_name='stores')
    
    def __str__(self):
        return self.name
    
# One To One Relationship
class ChaiCertificate(models.Model):
    chai = models.OneToOneField(ChaiVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificate')
    date_issued = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} Certificate For {self.name.chai}'