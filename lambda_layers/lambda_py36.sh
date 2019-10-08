#!/bin/sh
deactivate > /dev/null 2>&1
LAYERNAME=${1%/}
#LAYERNAME=$1
cd "$LAYERNAME"
# clean out
rm -rf python env
# venv
python3.6 -m venv env
source env/bin/activate
# AWS provided
pip install boto3       # provided by AWS core environment
pip install numpy scipy # provided by AWS layer
# install to python directory
pip install --no-deps -t python -r requirements.txt
# reduce footprint
#find python -name "*.so" | xargs strip
#find python -type d -name "tests" -exec rm -rf {} \;
# compress
zip -r -9 -q "${LAYERNAME}_py36.zip" python
