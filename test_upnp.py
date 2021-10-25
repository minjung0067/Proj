import miniupnpc

def open_port(port_no):
    '''this function opens a port using upnp'''
    upnp = miniupnpc.UPnP()

    upnp.discoverdelay = 10
    upnp.discover()

    upnp.selectigd()

    # addportmapping(external-port, protocol, internal-host, internal-port, description, remote-host)
    try:
        result=upnp.addportmapping(port_no, 'TCP', upnp.lanaddr, port_no, 'testing', '')
        return result
        print(result)
    except Exception as e:
        print(e)
