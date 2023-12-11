from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()



# Create your models here.
class Wallet(models.Model):
    '''The user wallet holds user token balance
    This address wallet will also be rewarded accordingly '''
    # A wallet address will be created each time user signs up for an account
    # some wallet functionalities will not currently be available until
    # our blockchain is ready hence, their values can be left out blank
    user = models.OneToOneField(User, on_delete=models.SET_NULL, blank=True, null=True)
    wallet_address = models.CharField(max_length=254, blank=True, null=True)
    wallet_balance = models.PositiveIntegerField(default=0)
    private_key = models.TextField(blank=True, null=True)
    public_key = models.TextField(blank=True, null=True)
    mnemonic_phrase = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.email
