
# IOOS Code Sprint 2019 - AWS

Temporary credentials `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and `AWS_SESSION_TOKEN` (*required when using temporary credentials*) can be obtained through Cognito.

### register for temporary credentials
```
(env) [bo@ty 2019_IOOS_CODESPRINT]$ python cognito-register.py 
Your Name: Boaty McBoatface
Your Email: boaty.mcbo@tface.com
Code Sprint Secret:
Password:
verification email will come from no-reply@verificationemail.com
```
You'll need to click a link in an email to be assigned group permissions. See host for `Code Sprint Secret` and password has no restrictions other than 6+ characters.

### login for temporary credentials
```
(env) [bo@ty 2019_IOOS_CODESPRINT]$ python cognito-login.py 
Email: boaty.mcbo@tface.com
Password: 
Keys will expire: 2019-10-03T19:36:13-04:00
```
After authentication, the temporary credentials are dumped into `aws.sh` which is just a wrapper setting the AWS environment variables. Feel free to assign them as you wish, script can be used to execute `awscli` commands, e.g. `sh aws.sh aws lambda list-function`

#### example: upload Lambda layer
```
aws lambda publish-layer-version   \
  --layer-name xarray_netcdf4_py36 \
  --zip-file fileb://xarray_netcdf4_py36.zip
```

#### example: list a code sprint bucket
```
aws s3 ls s3://ioos-code-sprint-2019
```
