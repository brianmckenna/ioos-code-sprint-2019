#!/usr/bin/env python
# -*- coding: utf-8 -*-

from getpass import getpass
from warrant import Cognito

from settings import *

name   = input('Your Name: ')
email  = input('Your Email: ')
secret = input('Code Sprint Secret: ')

u = Cognito(pool_id, client_id)
u.add_base_attributes(email=email, name=name)
u.add_custom_attributes(secret=secret)
u.register(email, getpass(prompt='Password: '))

print("verification email will come from no-reply@verificationemail.com")
