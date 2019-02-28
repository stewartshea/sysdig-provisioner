#! /usr/bin/python

# import client
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

# Input Sysdig API token
sdc_token = os.environ['SYSDIG_API_TOKEN']
#sdc_token = sys.argv[1]

# Instantiate the Sysdig client

sdclient = SdcClient(sdc_token)

team_name = sys.argv[1]


print('Now trying to create a team with name:', team_name)
ok, res = sdclient.create_team(team_name)
if not ok:
    print('Team creation failed:', res, '. Exiting.')
else:
    print('Team creation succeeded.', res)

