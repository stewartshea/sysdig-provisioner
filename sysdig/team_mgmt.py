#! /usr/bin/python

# import client
import os
import copy
import json
import requests
import sys
import hashlib
import traceback
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

# Input Sysdig API token
sdc_token = os.environ['SYSDIG_API_TOKEN']

# Instantiate the Sysdig client

sdclient = SdcClient(sdc_token)



#### TEAM CREATION ColonialOne ####
nsfilter="kubernetes.namespace.name='devops-wekan'"


print (filter)
print('Now trying to create a team with name:', 'ColonialOne')

ok, res = sdclient.create_team( 'ColonialOne', filter=nsfilter, show="container" )
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
memberships={'husker@arctiq.ca': 'ROLE_TEAM_MANAGER', 'boomer@arctiq.ca': 'ROLE_TEAM_MANAGER'}
ok, res = sdclient.edit_team('ColonialOne', memberships=memberships)
if not ok:
    print('Could not edit team:', res, '. Exiting.')
else:
    print('Edited team to change description and add users')


#### DASHBOARD CREATION ####

####### IMPERSONATE USER #######
print('Get User Token')
remote_user = "husker@arctiq.ca"
remote_team = "ColonialOne"
dashboard_token = sdclient.get_user_api_token(remote_user, remote_team)
print(dashboard_token)
print('Set client with token')
teamclient = SdcClient(dashboard_token[1])

dashboardSource = "MongoDB"
dashboardName = "ColonialOne-" + dashboardSource


print('Creating dashboard from dashboard')
ok, res = teamclient.create_dashboard_from_view(dashboardName, dashboardSource, None, True)

#
# Check the result
#
if ok:
    print('Dashboard copied successfully')
else:
    print(res)

####### IMPERSONATE USER #######
print('Get User Token')
remote_user = "husker@arctiq.ca"
remote_team = "ColonialOne"
dashboard_token = sdclient.get_user_api_token(remote_user, remote_team)
print(dashboard_token)
print('Set client with token')
teamclient = SdcClient(dashboard_token[1])

dashboardSource = "MySQL/PostgreSQL"
dashboardName = "ColonialOne-" + dashboardSource


print('Creating dashboard from dashboard')
ok, res = teamclient.create_dashboard_from_view(dashboardName, dashboardSource, None, True)

#
# Check the result
#
if ok:
    print('Dashboard copied successfully')
else:
    print(res)

#### TEAM CREATION Galactica ####
nsfilter="kubernetes.namespace.name='devops-wekan'"


print (filter)
print('Now trying to create a team with name:', 'Galactica')

ok, res = sdclient.create_team( 'Galactica', filter=nsfilter, show="container" )
if not ok:
    print('Team creation failed:', res, '. Exiting.')
else:
    print('Team creation succeeded.', res)



#### USER INVITES Galactica ####
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

#### EDIT TEAM Galactica #####
print('Now trying to edit team:', 'Galactica')
memberships={'husker@arctiq.ca': 'ROLE_TEAM_MANAGER', 'boomer@arctiq.ca': 'ROLE_TEAM_MANAGER'}
ok, res = sdclient.edit_team('Galactica', memberships=memberships)
if not ok:
    print('Could not edit team:', res, '. Exiting.')
else:
    print('Edited team to change description and add users')


#### DASHBOARD CREATION ####

####### IMPERSONATE USER #######
print('Get User Token')
remote_user = "husker@arctiq.ca"
remote_team = "ColonialOne"
dashboard_token = sdclient.get_user_api_token(remote_user, remote_team)
print(dashboard_token)
print('Set client with token')
teamclient = SdcClient(dashboard_token[1])

dashboardSource = "MongoDB"
dashboardName = "Galactica-" + dashboardSource


print('Creating dashboard from dashboard')
ok, res = teamclient.create_dashboard_from_view(dashboardName, dashboardSource, None, True)

#
# Check the result
#
if ok:
    print('Dashboard copied successfully')
else:
    print(res)

####### IMPERSONATE USER #######
print('Get User Token')
remote_user = "husker@arctiq.ca"
remote_team = "ColonialOne"
dashboard_token = sdclient.get_user_api_token(remote_user, remote_team)
print(dashboard_token)
print('Set client with token')
teamclient = SdcClient(dashboard_token[1])

dashboardSource = "MySQL/PostgreSQL"
dashboardName = "Galactica-" + dashboardSource


print('Creating dashboard from dashboard')
ok, res = teamclient.create_dashboard_from_view(dashboardName, dashboardSource, None, True)

#
# Check the result
#
if ok:
    print('Dashboard copied successfully')
else:
    print(res)
