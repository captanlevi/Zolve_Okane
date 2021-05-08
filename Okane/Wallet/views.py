from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import exceptions
from .models import Wallet, Transaction
from Accounts.models import User
from .serializers import WallerSerializer, TransactionSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

"""


**********************************************************************************************************************
I have performed all the sanity and validation checks in the serializers , so you wont find no such logic written here.

The idea is to use views only for directing requets and push all the logic to the serializers

**********************************************************************************************************************

"""

@api_view(["GET", "POST"])
def walletView(request):
    """
    End point to get all the wallets, or to save a new one 
    """

    if(request.method == "GET"):
        allWallets = Wallet.objects.all()
        serializer = WallerSerializer(allWallets, many = True)
        return Response(serializer.data)


    if(request.method == "POST"):
        # creating a new wallet here 
        serializer = WallerSerializer(data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data , status= status.HTTP_201_CREATED)

        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)




@api_view(["GET"])
def walletDetailView(request, id : int):
    """
    End point to get a particular wallet  ,
    here the id refers to the id of the wallet and not the user
    """

    if(request.method == "GET"):
        try:
            wallet = Wallet.objects.get(id = id)
        except ObjectDoesNotExist:
            raise exceptions.ValidationError("Wallet with id = {} does not exist".format(id))

        serializer = WallerSerializer(instance= wallet)

        return Response(serializer.data)


@api_view(["GET"])
def userWalletSearch(request, id : int):
    """
    End point to get a particular wallet  
    here the id refers to the id of the user and not the wallet
    """

    if(request.method == "GET"):
        try:
            wallet = Wallet.objects.get(user = id)
        except ObjectDoesNotExist:
            raise exceptions.ValidationError("Wallet with user id = {} does not exist".format(id))

        serializer = WallerSerializer(instance= wallet)

        return Response(serializer.data)




@api_view(["GET"])
def userTransactionSearch(request, id : int):
    """
    End point to get all transactions of a user  
    here the id refers to the id of the user.
    """

    if(request.method == "GET"):
        transactions = Transaction.objects.filter(user = id)

        serializer = TransactionSerializer(transactions , many = True)

        return Response(serializer.data)


@api_view(["GET", "POST"])
def transactionView(request):
    """
    End point to get all ransactions , or to make any transaction 
    """

    if(request.method == "GET"):
        allTransactions = Transaction.objects.all()
        serializer = TransactionSerializer(allTransactions, many = True)
        return Response(serializer.data)


    if(request.method == "POST"):
        # creating a new wallet here 
        serializer = TransactionSerializer(data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data , status= status.HTTP_201_CREATED)

        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)




