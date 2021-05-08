from rest_framework import exceptions, serializers
from .models import Wallet, Transaction
from Accounts.models import User




class WallerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ["id", "user", "balance"]


    def validate(self, attrs):
        super().validate(attrs)

        if(attrs["balance"] < Wallet._minAccountBalance):
            raise exceptions.ValidationError("The balance cannot be lower than {} , but found {}".format(Wallet._minAccountBalance,attrs["balance"]))


        return attrs






class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id", "user", "isCredit", "amount", "timeStamp"]



    def validate(self, attrs):
        """
        Basics checks like user pk exists and everything is 
        done using the super().validate()
        Here the extra check is whether the user has enough balance to keep the min amount in his/her account
        """
        super().validate(attrs)

        isCredit = attrs["isCredit"]

        if(isCredit):
            # if its credit , then no need to check ant further
            return attrs
        
        
        user : User = attrs["user"]
        amount = attrs["amount"]
        wallet : Wallet = user.userWallet
        balance = wallet.balance



        # Checking if the balance will go down
        if(balance - amount < Wallet._minAccountBalance):
            raise exceptions.ValidationError("cant deduct amount {} from {}'s account as min balance to maintain is {}".format(amount,user.email,Wallet._minAccountBalance))


        return attrs


    def create(self, validated_data):
        """
        Now that we have the validated data , we will also make changes to the Wallet
        and finally save a new row in the transaction table
        """


        user : User = validated_data["user"]
        wallet : Wallet = user.userWallet
        amount = validated_data["amount"]
        isCredit = validated_data["isCredit"]

        if(isCredit):
            wallet.balance = wallet.balance + amount

        else:
            wallet.balance = wallet.balance - amount



        # saving the changes wallet state        
        wallet.save()

        return super().create(validated_data= validated_data)