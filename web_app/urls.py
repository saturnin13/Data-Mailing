from django.conf.urls import url

from web_app import views

urlpatterns = [
    url(r'^user/', views.UserView.as_view()),
    url(r'^', views.Index.as_view()),
]
