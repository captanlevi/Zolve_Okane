from django.db import models
from Accounts.models import User
# Create your models here.


class Wallet(models.Model):
    """
    The wallet table
    """

    _minAccountBalance = 500  # change the min account balance here 

    user = models.OneToOneField(to = User, on_delete= models.CASCADE, related_name= "userWallet")
    balance = models.FloatField()




class Transaction(models.Model):
    """
    A table to save the logs of all the transactions 
    """
    user = models.ForeignKey(to = User, on_delete= models.CASCADE)
    isCredit = models.BooleanField()
    amount = models.FloatField()
    timeStamp = models.DateTimeField(auto_now= True)  # the Transaction will be saved at the time of making it
