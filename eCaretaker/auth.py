from django.contrib.auth.hashers import check_password, make_password
from eCaretakerWeb.models import Users

class UserBackend(object):
    def authenticate(username=None, password=None):
        pwd_valid = make_password(password)
        if username and pwd_valid:
            try:
                user = Users.objects.get(username=username)
            except Users.DoesNotExist:
                user = Users(username=username, password=pwd_valid)
                user.is_active = True
                user.is_admin = False
                user.save()
            return user
        return None