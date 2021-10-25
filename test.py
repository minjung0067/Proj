import upnpy

upnp = upnpy.UPnP()

# Discover UPnP devices on the network
# Returns a list of devices e.g.: [Device <Broadcom ADSL Router>]
devices = upnp.discover()

# Select the IGD
# alternatively you can select the device directly from the list
# device = devices[0]
device = upnp.get_igd()

# Get the services available for this device
# Returns a list of services available for the device
# e.g.: [<Service (WANPPPConnection) id="WANPPPConnection.1">, ...]
device.get_services()

# We can now access a specific service on the device by its ID
# The IDs for the services in this case contain illegal values so we can't access it by an attribute
# If the service ID didn't contain illegal values we could access it via an attribute like this:
# service = device.WANPPPConnection

# We will access it like a dictionary instead:
service = device['WANPPPConnection.1']

# Get the actions available for the service
# Returns a list of actions for the service:
#   [<Action name="SetConnectionType">,
#   <Action name="GetConnectionTypeInfo">,
#   <Action name="RequestConnection">,
#   <Action name="ForceTermination">,
#   <Action name="GetStatusInfo">,
#   <Action name="GetNATRSIPStatus">,
#   <Action name="GetGenericPortMappingEntry">,
#   <Action name="GetSpecificPortMappingEntry">,
#   <Action name="AddPortMapping">,
#   <Action name="DeletePortMapping">,
#   <Action name="GetExternalIPAddress">]
service.get_actions()

# Finally, get the external IP address
# Execute the action by its name
# Returns a dictionary: {'NewExternalIPAddress': 'xxx.xxx.xxx.xxx'}:wq
