from django.urls import path
from .views import *


urlpatterns = [
    path("walletEndpoint", walletView),
    path("searchUserWallet/<int:id>", userWalletSearch),
    path("transactionEndpoint", transactionView),
    path("searchUserTransactions/<int:id>", userTransactionSearch)
]
