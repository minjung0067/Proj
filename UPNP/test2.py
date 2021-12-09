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

service = device.WANIPConn1

service.get_actions()

# The action we are looking for is the "AddPortMapping" action
# Lets see what arguments the action accepts
# Use the get_input_arguments() or get_output_arguments() method of the action
# for a list of input / output arguments.
# Example output of the get_input_arguments method for the "AddPortMapping" action
# Returns a dictionary:
# [
#     {
#         "name": "NewRemoteHost",
#         "data_type": "string",
#         "allowed_value_list": []
#     },
#     {
#         "name": "NewExternalPort",
#         "data_type": "ui2",
#         "allowed_value_list": []
#     },
#     {
#         "name": "NewProtocol",
#         "data_type": "string",
#         "allowed_value_list": [
#             "TCP",
#             "UDP"
#         ]
#     },
#     {
#         "name": "NewInternalPort",
#         "data_type": "ui2",
#         "allowed_value_list": []
#     },
#     {
#         "name": "NewInternalClient",
#         "data_type": "string",
#         "allowed_value_list": []
#     },
#     {
#         "name": "NewEnabled",
#         "data_type": "boolean",
#         "allowed_value_list": []
#     },
#     {
#         "name": "NewPortMappingDescription",
#         "data_type": "string",
#         "allowed_value_list": []
#     },
#     {
#         "name": "NewLeaseDuration",
#         "data_type": "ui4",
#         "allowed_value_list": []
#     }
# ]
service.AddPortMapping.get_input_arguments()

# Finally, add the new port mapping to the IGD
# This specific action returns an empty dict: {}
service.AddPortMapping(
    NewRemoteHost='',
    NewExternalPort=80,
    NewProtocol='TCP',
    NewInternalPort=8000,
    NewInternalClient='192.168.1.3',
    NewEnabled=1,
    NewPortMappingDescription='Test port mapping entry from UPnPy.',
    NewLeaseDuration=0
)