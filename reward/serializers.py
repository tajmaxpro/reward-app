from rest_framework import serializers
from .models import Wallet
from django.contrib.auth.models import User


class WalletSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Represent user as primary key

    class Meta:
        model = Wallet
        fields = ('id', 'user', 'wallet_address', 'wallet_balance', 'private_key', 'public_key', 'mnemonic_phrase')


class UpdateWalletSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wallet
        fields = ('id', 'wallet_address', 'wallet_balance', 'private_key', 'public_key', 'mnemonic_phrase')
