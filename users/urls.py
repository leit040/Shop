from django.urls import path, include

from Forms.RegistrationForm import RegistrationForm
from feedbacks import views
from users.views import Registration

# urlpatterns = [
#     path('login/', LoginView.as_view(), name='login')
# ]

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', Registration.as_view(), name='registration')
]
