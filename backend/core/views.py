from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView,
)
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import InvalidToken
from core.models import Example
from core.serializers import ExampleSerializer, UserSerializer
from rest_framework import viewsets
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response


class ExampleViewSet(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer


class CookieTokenObtainPairView(TokenObtainPairView):
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get("refresh"):
            response.set_cookie(
                "refresh_token",
                response.data["refresh"],
                max_age=settings.SESSION_COOKIE_AGE,
                httponly=True,
            )
        return super().finalize_response(request, response, *args, **kwargs)


class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = None

    def validate(self, attrs):
        attrs["refresh"] = self.context["request"].COOKIES.get("refresh_token")
        if attrs["refresh"]:
            return super().validate(attrs)
        else:
            raise InvalidToken(
                "No valid token found in cookie 'refresh_token'"
            )


class CookieTokenRefreshView(TokenRefreshView):
    serializer_class = CookieTokenRefreshSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get("refresh"):
            response.set_cookie(
                "refresh_token",
                response.data["refresh"],
                max_age=settings.SESSION_COOKIE_AGE,
                httponly=True,
            )
            # del response.data["refresh"]
        return super().finalize_response(request, response, *args, **kwargs)


class CookieTokenClearView(APIView):
    allowed_methods = ["DELETE"]

    def delete(self, request):
        resp = Response()
        resp.delete_cookie("refresh_token")
        return resp


class ProfileView(APIView):
    def get(self, request):
        user = UserSerializer(request.user)
        return Response(user.data)
