from django.urls import path, include

from accounts.views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
]
