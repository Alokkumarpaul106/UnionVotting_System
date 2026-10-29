from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Candidate(models.Model):
    name=models.CharField(max_length=50)
    party=models.CharField(max_length=100)
    symbol=models.ImageField(upload_to="symbols/",blank=True,null=True)
    image=models.ImageField(upload_to="candidates/",blank=True,null=True)
    vote_count=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name}-{self.party}"

class Vote(models.Model):
    candidate=models.ForeignKey(Candidate,on_delete=models.CASCADE,related_name='votes')
    name=models.CharField(max_length=50)
    VILLAGE_CHOICES=(
        ('bilsorail', 'বিলসরাইল'),
        ('kandakul', 'কান্দাকুল'),
        ('icakhali', 'ইচাখালি')
    )
    village=models.CharField(max_length=20,choices=VILLAGE_CHOICES,null=True,blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    n_id=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class EligibleVoter(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='eligible_voter',null=True,blank=True)
    name=models.CharField(max_length=100)
    village=models.CharField(max_length=20,choices=Vote.VILLAGE_CHOICES,null=True,blank=True)
    date_of_birth=models.DateField(null=True,blank=True)
    NID=models.CharField(max_length=20,unique=True,db_index=True)
    has_votted=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}-{self.has_votted}"
