#### build Lambda layer

see [AWS Lambda Limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html) for some limits on what can be executed in Lambda.

AWS provides a [layer](https://aws.amazon.com/blogs/aws/new-for-aws-lambda-use-any-programming-language-and-share-common-components/) with `numpy` and `scipy` at
arn:aws:lambda:us-east-2:259788987135:layer:AWSLambda-Python36-SciPy1x:2

Most of the time this is useful, but given the 250 MB (*unzipped, including layers*) deployment package size limit, a custom layer may be beneficial.


#### overly simplistic script to package layer: lambda_py36.sh
`sh lambda_py36.sh  xarray_netcdf4` will build `xarray_netcdf4_py36.zip` in the directory.

- `strip` can be useful to reduce the size of shared libraries (NOTE: risky, if you're seeing *invalid ELF header* messages, try without.
- `tests` can often be removed to shrink package size
- plenty more opportunities
