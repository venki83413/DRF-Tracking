from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import User
from .serializers import Registerserializer, UserSerializer, UserLoginSerializer, UserLogoutSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework_jwt.views import ObtainJSONWebToken
from .serializers import JWTSerializer


class Record(generics.ListCreateAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AuthToken:
    pass


class RegisterAPI(generics.GenericAPIView):
    serializer_class = Registerserializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "User": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class Login(generics.GenericAPIView):
    # get method handler
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLoginSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class Logout(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer_class = UserLogoutSerializer(data=request.data)
        if serializer_class.is_valid(raise_exception=True):
            return Response(serializer_class.data, status=HTTP_200_OK)
        return Response(serializer_class.errors, status=HTTP_400_BAD_REQUEST)


class ObtainJWTView(ObtainJSONWebToken):
    serializer_class = JWTSerializer

def index(request):
    return redirect('/api/login')
