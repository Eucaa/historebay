
"""This file contains custom authentication codes."""
from django.contrib.auth.models import User


class EmailAuth:
    """Recognise user by on exact match of username and password."""

    def authenticate(self, username=None, password=None):
        """Get an instance of 'User' based off the username / email and verify
        the password."""
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
            return None

        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """Get a user instance"""
        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            return None

        except User.DoesNotExist:
            return None
