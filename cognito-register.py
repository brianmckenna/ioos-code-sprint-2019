#!/usr/bin/env python
# -*- coding: utf-8 -*-

from getpass import getpass
from warrant import Cognito

from settings import *

#pool_id   = 'us-east-1_KeZCl0wwt'
#client_id = '2lup6diqlr7usgsn26sqm9vd6c'

name   = input('Your Name: ')
email  = input('Your Email: ')
secret = input('Code Sprint Secret: ')

u = Cognito(pool_id, client_id)
u.add_base_attributes(email=email, name=name)
u.add_custom_attributes(secret=secret)
u.register(email, getpass(prompt='Password: '))

print("verification email will come from no-reply@verificationemail.com")
