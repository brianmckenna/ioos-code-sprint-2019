#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
from getpass import getpass
from warrant.aws_srp import AWSSRP

from settings import *

# authenticate
cognito_idp = boto3.client('cognito-idp')
username  = input('Email: ')
aws = AWSSRP(
    username  = username,
    password  = getpass('Password: '),
    pool_id   = pool_id,
    client_id = client_id,
    client    = cognito_idp
)
tokens = aws.authenticate_user()

# get identity
cognito_identity = boto3.client('cognito-identity')
logins = {login: tokens['AuthenticationResult']['IdToken']}
identity = cognito_identity.get_id(
    IdentityPoolId=identity_pool_id,
    Logins=logins
)

# get credentials
credentials = cognito_identity.get_credentials_for_identity(
    IdentityId=identity['IdentityId'],
    Logins=logins
)

# write shell script, temporary credentials require SessionToken
with open('aws.sh', 'w') as f:
    f.write("# Expiration: {:s}".format(credentials['Credentials']['Expiration'].isoformat()))
    f.write("AWS_ACCESS_KEY_ID={:s}\n".format(credentials['Credentials']['AccessKeyId']))
    f.write("AWS_SECRET_ACCESS_KEY={:s}\n".format(credentials['Credentials']['SecretKey']))
    f.write("AWS_SESSION_TOKEN={:s}\n".format(credentials['Credentials']['SessionToken']))
    f.write("$@")

print("Keys will expire: {:s}".format(credentials['Credentials']['Expiration'].isoformat()))
