
#  This file contains custom authentication codes.
from django.contrib.auth.models import User


class EmailAuth:
    """Recognise user by on exact match of username and password."""

    def authenticate(self, username=None, password=None):
        """Get an instance of 'User' based off the username / email and verify the password."""

        try:  # Try to get a user by using User.objects.filter.
            #user = User.objects.filter(Q(username__exact=username_or_email) | Q(email__exact=username_or_email))
            user = User.objects.get(username=username)
            if user.check_password(password):  # If the password is available, return the user. If not, then return nothing.
                return user
            return None

        except User.DoesNotExist:  # If the user does not exist, return a None as well.
            return None

    def get_user(self, user_id):
        """Get a user instance"""

        try:
            user = User.objects.get(pk=user_id)  # Here, var user shall have user_id as primary key(pk).

            if user.is_active:
                return user
            return None

        except User.DoesNotExist:
            return None
