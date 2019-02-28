#! /usr/bin/python

# import client
import os
from sdcclient import SdcClient

# Input Sysdig API token
api_token = os.environ['SYSDIG_API_TOKEN']

# Instantiate the Sysdig client

sdclient = SdcClient(sdc_token)

print('Now trying to create a team with name:', team_name)
ok, res = sdclient.create_team(team_name)
if not ok:
    print('Team creation failed:', res, '. Exiting.')
    sys.exit(1)
else:
    print('Team creation succeeded.', res)
