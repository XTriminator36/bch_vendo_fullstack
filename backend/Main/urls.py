from django.urls import path
from . import views

urlpatterns = [
    #add necessary paths for view
    path("", views.showProducts, name="products"),
    path("auth/login/", views.authLogin, name="authlogin"),
    path("auth/dashboard/", views.authDashboard, name="authdashboard"),
    path("auth/inventories/", views.authInventories, name="authinventories"),
    path("auth/notifications/", views.authNotifications, name="authnotifications"),
    path("auth/sales/", views.authSales, name="authsales"),
    path("auth/transactions/", views.authTransactions, name="authtransactions"),
    path("auth/vendos/", views.authVendos, name="authvendos"),
    path("addProduct/", views.addProduct, name="addProduct"),
    path("registerVendo/", views.registerVendo, name="registerVendo"),
]