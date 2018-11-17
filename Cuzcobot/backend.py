from Cuzcobot.models.ApplicationUser import ApplicationUser as cUser
from django.core.exceptions import ObjectDoesNotExist


class CuzcoBotAuthenticationBackend:
    """
    Authentication Bankend for custom user model implimentation.
    Written on 11/16/2018
    Authored By Christopher Bigelow
    """

    def authenticate(self, **credentials):
        profile = None
        if credentials['username'] is not None:
            try:
                cUser.objects.filter(email=credentials['username']).get()
            except ObjectDoesNotExist:
                return None

        if ((profile is not None) and (credentials['password'] is not None)):
            b = profile.check_password(credentials['password'])

            if b == True:
                return profile
            else:
                return None
        else:
            return None

    def get_user(self, id):
        try:
            return cUser.objects.filter(pk=id).get()
        except cUser.DoesNotExist:
            return None
