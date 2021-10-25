import upnpy

upnp = upnpy.UPnP()

# Discover UPnP devices on the network
# Returns a list of devices e.g.: [Device <Broadcom ADSL Router>]
devices = upnp.discover()
print("==========devices==========")
print(devices)
print("----------------------\n\n")

# Select the IGD
# alternatively you can select the device directly from the list
# device = devices[0]
device = upnp.get_igd()

# Get the services available for this device
# Returns a list of services available for the device
# e.g.: [<Service (WANPPPConnection) id="WANPPPConnection.1">, ...]
device.get_services()
print("========get_services==================")
print(device.get_services())
print("--------------------------\n\n")


# We can now access a specific service on the device by its ID
# The IDs for the services in this case contain illegal values so we can't access it by an attribute
# If the service ID didn't contain illegal values we could access it via an attribute like this:
service = device.WANIPConn1


#PortMappingNumberOfEntries
#[<Service (Layer3Forwarding) id="L3Forwarding1">, <Service (WANCommonInterfaceConfig) id="WANCommonIFC1">, 
# <Service (WANIPConnection) id="WANIPConn1">, <Service (WFAWLANConfig) id="WFAWLANConfig1">]




# We will access it like a dictionary instead:
#service = device['WANPPPConnection.1']

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
print("=============== 사용 가능한 액션들 ================")
print(service.get_actions())
print("-------------------------------------\n\n")


# Finally, get the external IP address
# Execute the action by its name
# Returns a dictionary: {'NewExternalIPAddress': 'xxx.xxx.xxx.xxx'}
#service.GetGenericPortMappingEntry()
print("================ 필요한 인자값 ===============")
print(service.GetSpecificPortMappingEntry())
print("----------------------------------------------\n\n-")

# service.AddPortMapping.get_input_arguments()

# Finally, add the new port mapping to the IGD
# This specific action returns an empty dict: {}
# a = service.AddPortMapping(
#     NewRemoteHost='',
#     NewExternalPort=12344,
#     NewProtocol='TCP',
#     NewInternalPort=81,
#     NewInternalClient='192.168.100.107',
#     NewEnabled=1,
#     NewPortMappingDescription='Test port mapping entry from UPnPy.',
#     NewLeaseDuration=0
# )

# print(">", a)

# b = service.DeletePortMapping(
#     NewRemoteHost='',
#     NewExternalPort=46123,
#     NewProtocol='TCP',
# )

# print(">>", b)


# a = service.GetGenericPortMappingEntry(
#     NewPortMappingIndex = 1
# )

# print(">", a)


# a = service.GetSpecificPortMappingEntry(
#     NewPortMappingIndex = 0
# )

# print(">", a)

