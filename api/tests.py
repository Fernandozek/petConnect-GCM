from django.test import TestCase

# Create your tests here.

# Path: api/tests.py
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Profile
from .serializers import ProfileSerializer
