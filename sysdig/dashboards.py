#!/usr/bin/env python
#
# This example shows various functions to create a new dashboard or find an existing on,
# edit the content, and then delete it.
#

import getopt
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), '..'))
from sdcclient import SdcClient

# Input Sysdig API token
sdc_token = os.environ['SYSDIG_API_TOKEN']

# Instantiate the Sysdig client

sdclient = SdcClient(sdc_token)


dashboardSource = "MongoDB"
dashboardName = "Copy Of {}".format(dashboardName)
dashboardFilter = "kubernetes.namespace.name=production"

print('Creating dashboard from dashboard')
ok, res = sdclient.create_dashboard_from_view(dashboardName, dashboardSource, dashboardFilter)

#
# Check the result
#
if ok:
    print('Dashboard copied successfully')
else:
    print(res)
