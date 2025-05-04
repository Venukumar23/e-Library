from django.urls import path

from . import views

urlpatterns = [path("index.html", views.index, name="index"),
	       path("UserLogin", views.UserLogin, name="UserLogin"),
	       path("Login.html", views.Login, name="Login"),
	       path("AdminLogin.html", views.AdminLogin, name="AdminLogin"),
	       path("AdminLoginAction", views.AdminLoginAction, name="AdminLoginAction"),	       
	       path("Register.html", views.Register, name="Register"),
	       path("RegisterAction", views.RegisterAction, name="RegisterAction"),	
	       path("AddBook.html", views.AddBook, name="AddBook"),
	       path("AddBookAction", views.AddBookAction, name="AddBookAction"),
	       path("AddUrl.html", views.AddUrl, name="AddUrl"),
	       path("AddUrlAction", views.AddUrlAction, name="AddUrlAction"),
	       path("ViewBooks", views.ViewBooks, name="ViewBooks"),
	       path("PlayVideo", views.PlayVideo, name="PlayVideo"),
	       path("DeleteFile", views.DeleteFile, name="DeleteFile"),
	       path("SearchBook.html", views.SearchBook, name="SearchBook"),
	       path("SearchBookAction", views.SearchBookAction, name="SearchBookAction"),
]