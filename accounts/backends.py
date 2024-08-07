from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class EmailOrUsernameModelBackend(ModelBackend):
    """
    Authentication backend which allows users to authenticate using either their
    username or email address
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        user_model = get_user_model()

        if username is None:
            username = kwargs.get(user_model.USERNAME_FIELD)

        # The `username` field is allowed to contain `@` characters so
        # technically a given email address could be present in either field,
        # possibly even for different users, so we'll query for all matching
        # records and test each one.
        try:
            users = user_model._default_manager.filter(
                Q(**{user_model.USERNAME_FIELD: username}) | Q(email__iexact=username)
            )
        except user_model.DoesNotExist:
            # No user exists, run the default password hasher to reduce timing attacks
            user_model().set_password(password)
            return None

        # Test whether any matched user has the provided password:
        for user in users:
            if user.check_password(password):
                return user
        
        # No valid user found
        return None
