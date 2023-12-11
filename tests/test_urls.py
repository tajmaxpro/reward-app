# from django.test import TestCase
# from django.urls import reverse, resolve
# from reward.views import WalletCreateAPIView, WalletDetailAPIView

# class TestUrls(TestCase):

#     def test_wallet_create(self):
#         url = reverse('wallet-create')
#         self.assertEqual(resolve(url).func.view_class, WalletCreateAPIView)

#     def test_wallet_detail(self):
#         # Assuming pk=1 for testing purposes; you can change this value as needed
#         url = reverse('wallet-detail', kwargs={'pk': 1})
#         self.assertEqual(resolve(url).func.view_class, WalletDetailAPIView)

#     def test_token_obtain_pair(self):
#         url = reverse('token_obtain_pair')
#         self.assertEqual(resolve(url).func.vi)