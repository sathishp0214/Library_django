# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
# Create your tests here
from django.contrib import auth

class AuthTestCase(TestCase):
    def setUp(self):
        self.u = User.objects.create_user('sathish1', 'sathishp0214@gmail.com', 'india@123')
        self.u.is_staff = True
        self.u.is_superuser = True
        self.u.is_active = True
        self.u.save()

    def testLogin(self):
        self.client.login(username='sathish1', password='india@123')
