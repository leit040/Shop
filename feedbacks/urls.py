from django.urls import path

from feedbacks import views

urlpatterns = [
    path('', views.index, name='addFeedback')
]
