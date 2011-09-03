#!/usr/bin/env python
from api.authenticate.models import User
from api.authenticate.models import UserToken
from django.contrib import admin

admin.site.register(User)
admin.site.register(UserToken)

