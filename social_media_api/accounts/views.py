from django.contrib.auth import authenticate
from rest_framework import permissions, generics
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, UserSerializer
from .models import CustomUser


User = get_user_model()

class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response({
                "user": serializer.data,
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password"]
            )

            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    "token": token.key
                })
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(generics.GenericAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    @action(detail=True, methods=["post"])
    def follow(self, request, pk=None):
        user_to_follow = self.get_object()

        if request.user == user_to_follow:
            return Response({"error": "You cannot follow yourself."}, status=400)
        
        if request.user.following.filter(id=user_to_follow.id).exists():
            return Response({"error": "Already following this user."}, status=400)

        request.user.following.add(user_to_follow)
        return Response({"message": "User followed successfully."})

    @action(detail=True, methods=["post"])
    def unfollow(self, request, pk=None):
        user_to_unfollow = self.get_object()

        if not request.user.following.filter(id=user_to_unfollow.id).exists():
            return Response({"error": "You are not following this user."}, status=400)
    
        request.user.following.remove(user_to_unfollow)
        return Response({"message": "User unfollowed successfully."})