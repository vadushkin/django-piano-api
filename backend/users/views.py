import datetime

from django.conf import settings
import jwt
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class GetRoutesView(APIView):
    def get(self, _):
        routes = [
            {
                "Endpoint": "/register/",
                "method": "POST",
                "body": {
                    "name": "Require",
                    "email": "Require",
                    "password": "Require",
                    "photo": "Not Require",
                },
                "description": "Registers you",
            },
            {
                "Endpoint": "/login/",
                "method": "POST",
                "body": {"email": "Require", "password": "Require"},
                "description": "Logins you",
            },
            {
                "Endpoint": "/logout/",
                "method": "GET",
                "body": None,
                "description": "Logouts you",
            },
            {
                "Endpoint": "/user/",
                "method": "GET",
                "body": None,
                "description": "Returns your data if you are registered",
            },
        ]

        return Response(routes)


class RegisterView(APIView):
    def post(self, request):
        token = request.COOKIES.get("jwt")

        if token:
            response = Response()
            response.data = {
                "message": "You're authenticated!",
            }
            return response

        serializer = UserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        token = request.COOKIES.get("jwt")

        if token:
            response = Response()
            response.data = {
                "message": "You're authenticated!",
            }
            return response

        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("User not found!")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        response = Response()

        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {
            "jwt": token,
        }
        return response


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            raise AuthenticationFailed("Unauthenticated!")

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError):
            raise AuthenticationFailed(
                "Token expired! Please logout and then authenticate!",
            )

        user = User.objects.filter(id=payload["id"]).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)


class LogoutView(APIView):
    def get(self, request):
        token = request.COOKIES.get("jwt")
        response = Response()

        if token:
            response.delete_cookie("jwt")
            response.data = {
                "message": "success",
            }
        else:
            response.data = {
                "message": "Login to logout",
            }

        return response
