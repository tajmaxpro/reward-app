from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Wallet
from .serializers import WalletSerializer, UpdateWalletSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication


"""
    API endpoint to create a wallet or retrieve an existing wallet for a user.

    If the wallet for the given user already exists, returns the existing wallet details.
    If no wallet exists, creates a new wallet for the user.

    - For creating a new wallet:
        - HTTP Method: POST
        - Endpoint: /api/wallet/create/
        - Authentication: Requires a valid JWT token in the Authorization header
        - Permissions: Requires the user to be authenticated
        - Request Body: 
                {
                    "user": 1,
                    "wallet_address": "Your Wallet Address",
                    "wallet_balance": 100,
                    "private_key": "Your Private Key",
                    "public_key": "Your Public Key",
                    "mnemonic_phrase": "Your Mnemonic Phrase"
                }

        - Response: {'message': 'Wallet created successfully', 'wallet': {...}}
"""
class WalletCreateAPIView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WalletSerializer

    def create(self, request, *args, **kwargs):
        selected_user_id = self.request.data.get('user')  # Assuming 'user_id' is passed in the request data

        existing_wallet = Wallet.objects.filter(user_id=selected_user_id).first()
        if existing_wallet:
            serializer = WalletSerializer(existing_wallet)
            return Response({"message": "Wallet already exists", "wallet": serializer.data}, status=status.HTTP_200_OK)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"message": "Wallet created successfully", "wallet": serializer.data}, status=status.HTTP_201_CREATED)
    


"""
    API endpoint to view, update, or delete a specific wallet.

    - To retrieve wallet details:
        - HTTP Method: GET
        - Endpoint: wallet/<wallet_id>/
        - Authentication: Requires a valid JWT token in the Authorization header
        - Permissions: Requires the user to be authenticated
        - Response: Wallet details for the specified ID

    - To update wallet details:
        - HTTP Method: PUT
        - Endpoint: wallet/<wallet_id>/
        - Authentication: Requires a valid JWT token in the Authorization header
        - Permissions: Requires the user to be authenticated
        - Request Body: Updated wallet data
                            {
                                "id": 5,
                                "wallet_address": "sdf",
                                "wallet_balance": 100,
                                "private_key": "sdf",
                                "public_key": "sdf",
                                "mnemonic_phrase": "fsd"
                            }
        - Response: Updated wallet details

    - To delete a wallet:
        - HTTP Method: DELETE
        - Endpoint: wallet/<wallet_id>/
        - Authentication: Requires a valid JWT token in the Authorization header
        - Permissions: Requires the user to be authenticated
        - Response: Empty response with status 204 if successful
    """

class WalletDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    queryset = Wallet.objects.all()  # Queryset to retrieve all wallets
    serializer_class = UpdateWalletSerializer  # Serializer class for wallets

