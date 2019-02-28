#! /usr/bin/python

# import client
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

# Input Sysdig API token
sdc_token = os.environ['SYSDIG_API_TOKEN']

# Instantiate the Sysdig client

sdclient = SdcClient(sdc_token)



#### TEAM CREATION ColonialOne ####
print('Now trying to create a team with name:', 'ColonialOne')
ok, res = sdclient.create_team( 'ColonialOne', filter="kubernetes.namespace.name='devops-wekan'", show="container" )
if not ok:
    print('Team creation failed:', res, '. Exiting.')
else:
    print('Team creation succeeded.', res)



#### USER INVITES ColonialOne ####
print('Trying to invite a user:', 'husker@arctiq.ca')
ok, res = sdclient.create_user_invite('husker@arctiq.ca')
if not ok:
    if res == 'user ' + 'husker@arctiq.ca' + ' already exists':
        print('User creation failed because', 'husker@arctiq.ca', 'already exists. Continuing.')
    else:
        print('User creation failed:', res, '. Exiting.')
else:
    print('User creation succeeded')
print('Trying to invite a user:', 'boomer@arctiq.ca')
ok, res = sdclient.create_user_invite('boomer@arctiq.ca')
if not ok:
    if res == 'user ' + 'boomer@arctiq.ca' + ' already exists':
        print('User creation failed because', 'boomer@arctiq.ca', 'already exists. Continuing.')
    else:
        print('User creation failed:', res, '. Exiting.')
else:
    print('User creation succeeded')

#### EDIT TEAM ColonialOne #####
print('Now trying to edit team:', 'ColonialOne')
# memberships = {
#     'admin@draios.com': 'ROLE_TEAM_MANAGER',
#     'john-doe@sysdig.com': 'ROLE_TEAM_READ'
# }
memberships={'husker@arctiq.ca': 'ROLE_TEAM_READ', 'boomer@arctiq.ca': 'ROLE_TEAM_READ'}
ok, res = sdclient.edit_team('ColonialOne', memberships=memberships)
if not ok:
    print('Could not edit team:', res, '. Exiting.')
else:
    print('Edited team to change description and add users')


#### DASHBOARD CREATION ####
dashboardSource = "MongoDB"
dashboardName = "ColonialOne-" + dashboardSource


print('Creating dashboard from dashboard')
ok, res = sdclient.create_dashboard_from_view(dashboardName, dashboardSource, None, True)

#
# Check the result
#
if ok:
    print('Dashboard copied successfully')
else:
    print(res)
