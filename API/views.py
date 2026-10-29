from django.shortcuts import render,redirect
from .serializers import CandidateSerializer,VoteSerializer,RegisterSerializer
from .models import Candidate,Vote,EligibleVoter
from rest_framework import viewsets,permissions
from .permissions import IsAdminOrReadOnly
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.db import transaction
from rest_framework.throttling import AnonRateThrottle
from django.db.models import F
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.http import urlsafe_base64_decode



# Create your views here.

class RegisterThrottle(AnonRateThrottle):
    rate='5/min'  

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()     
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    throttle_classes=[RegisterThrottle]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        uid = urlsafe_base64_encode(
            force_bytes(user.pk)
        )

        token = default_token_generator.make_token(user)

        verification_link = (
            f"{settings.SITE_URL}/api/verify-email/"
            f"?uid={uid}&token={token}"
        )

        send_mail(
            subject="Verify your email",
            message=f"""
Hello {user.username},

Please verify your email by clicking the link below:

{verification_link}

If you did not register, ignore this email.
""",
            from_email=None,
            recipient_list=[user.email],
            fail_silently=False,
        )

        return Response({
            "message": "Registration successful. Please check your email to verify your account."
        })

class VerifyEmailView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):

        uid = request.GET.get('uid')
        token = request.GET.get('token')

        if not uid or not token:
            return Response({
                "message": "Invalid verification link."
            }, status=400)

        try:
            user_id = urlsafe_base64_decode(uid).decode()
            user = User.objects.get(pk=user_id)

        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            return Response({
                "message": "Invalid verification link."
            }, status=400)

        if not default_token_generator.check_token(user, token):
            return Response({
                "message": "Invalid or expired verification link."
            }, status=400)

        user.is_active = True
        user.save(update_fields=['is_active'])

        return redirect('/')



class CandidateViewSet(viewsets.ModelViewSet):
    queryset=Candidate.objects.all()
    serializer_class=CandidateSerializer
    permission_classes=[IsAdminOrReadOnly]
    
   
class VoteViewSet(viewsets.ModelViewSet):  #modelviewset bade akhane generic view use kora vlo karon o sudhu POST dei.code lekha kom lage 
    queryset=Vote.objects.all()
    serializer_class=VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):   
        user = self.request.user

        if user.is_staff:                   #akhane general user jeno URD korte na pare tai  
            return Vote.objects.all()
        return Vote.objects.none()
    
    @transaction.atomic
    def perform_create(self, serializer):
        nid=self.request.data.get("n_id")
        village=self.request.data.get("village")
        date_of_birth=self.request.data.get("date_of_birth")
        
        try:
            voter=EligibleVoter.objects.select_for_update().get(NID=nid,village=village,date_of_birth=date_of_birth)
        except EligibleVoter.DoesNotExist:
            raise ValidationError({"error":"দুঃখিত! আপনার দেওয়া তথ্য ভোটার তালিকার সাথে মিলছে না।"})
        if voter.has_votted:
            raise ValidationError({"error":"সতর্কতা! এই ভোটার ইতিমধ্যে একবার ভোট দিয়ে দিয়েছেন।"})

        vote=serializer.save()
        voter.has_votted=True
        voter.save()

        
        # candidate=vote.candidate
        # candidate.vote_count +=1        #akadik user ekoi candidate vote korle akhane race condition hote pare. 
        # candidate.save()
        Candidate.objects.filter(pk=vote.candidate_id).update(vote_count=F('vote_count')+1)  #akhane F expression use kora holo jate race condition na hoy. akadik user ekoi candidate vote korle akhane race condition hote pare.















    





    
        

