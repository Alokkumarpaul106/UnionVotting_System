from django.urls import path
from .import views
from rest_framework import routers
from API.views import CandidateViewSet,VoteViewSet,RegisterView,VerifyEmailView
router = routers.DefaultRouter()
router.register(r'candidate', CandidateViewSet)
router.register(r'vote',VoteViewSet)
urlpatterns = router.urls
urlpatterns += [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
]
