from django.contrib.auth.models import User, Permission
from django.db import models

users = User.objects.all()
print("O:" + users)
