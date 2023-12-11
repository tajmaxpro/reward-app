from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Wallet
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.test import APIClient


class WalletAPITests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.access_token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(self.access_token))

    def test_create_wallet(self):
        data = {
            'user': self.user.id,
            'wallet_address': 'Test Wallet Address',
            'wallet_balance': 200,
            'private_key': 'Test Private Key',
            'public_key': 'Test Public Key',
            'mnemonic_phrase': 'Test Mnemonic Phrase'
        }

        response = self.client.post('/wallet/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Wallet created successfully')
        self.assertEqual(response.data['wallet']['user'], self.user.id)

    def test_retrieve_existing_wallet(self):
        wallet = Wallet.objects.create(
            user=self.user,
            wallet_address='Existing Wallet Address',
            wallet_balance=300,
            private_key='Existing Private Key',
            public_key='Existing Public Key',
            mnemonic_phrase='Existing Mnemonic Phrase'
        )

        response = self.client.get(f'/wallet/{wallet.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_wallet(self):
        wallet = Wallet.objects.create(
            user=self.user,
            wallet_address='Initial Wallet Address',
            wallet_balance=400,
            private_key='Initial Private Key',
            public_key='Initial Public Key',
            mnemonic_phrase='Initial Mnemonic Phrase'
        )

        data = {
            'id': wallet.id,
            'wallet_address': 'Updated Wallet Address',
            'wallet_balance': 500,
            'private_key': 'Updated Private Key',
            'public_key': 'Updated Public Key',
            'mnemonic_phrase': 'Updated Mnemonic Phrase'
        }

        response = self.client.put(f'/wallet/{wallet.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_wallet(self):
        wallet = Wallet.objects.create(
            user=self.user,
            wallet_address='ToDelete Wallet Address',
            wallet_balance=600,
            private_key='ToDelete Private Key',
            public_key='ToDelete Public Key',
            mnemonic_phrase='ToDelete Mnemonic Phrase'
        )

        response = self.client.delete(f'/wallet/{wallet.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Wallet.objects.filter(id=wallet.id).exists())
