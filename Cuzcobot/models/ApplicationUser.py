from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from string import ascii_uppercase, digits
from random import choice

from Cuzcobot.managers.customusermanager import userman
from Cuzcobot.dataAPI.Client import api

chars = ascii_uppercase + digits

class ApplicationUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='Email Address', unique=True)
    first_name = models.CharField(max_length=60, blank=True)
    last_name = models.CharField(max_length=60)
    paperTrade =models.BooleanField(default=True)
    is_active = models.BooleanField(verbose_name='active', default=True)
    is_superuser = models.BooleanField(verbose_name='Super Admin', default=False)
    is_admin = models.BooleanField(verbose_name='Staff', default=False)

    objects = userman()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name',
                       'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin

    def getBuyingPower(self):
        # print('api.get_account().buying_power')
        return api.get_account().buying_power  # string<number>