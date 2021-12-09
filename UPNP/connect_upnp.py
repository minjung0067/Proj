@login_required
def connect_upnp(request):
    if request.method == "POST":
        result = False
        internal_port = int(request.POST['iport'])
        protocol = request.POST['protocol']
        ip_address = request.POST['ip']
        upnp_content = request.POST['content']

        ret = {"data":[]}

        try: 
            # create the object
            u = miniupnpc.UPnP()
            u.discoverdelay = 200
            print('Discovering... delay time =%ums' % u.discoverdelay)
            ndevices = u.discover() #find the router
            print(ndevices, 'device(s) detected')
            
            u.selectigd()
            eport = 30001 

            # find a free port for the redirection (from 30001 to 35000)
            tcp = u.getspecificportmapping(eport, 'TCP')
            udp = u.getspecificportmapping(eport, 'UDP')

            while (tcp != None or udp != None) and eport < 35001:
                eport = eport + 1
                tcp = u.getspecificportmapping(eport, 'TCP')
                udp = u.getspecificportmapping(eport, 'UDP')
            
            print("_------------설정된 외부포트-----------" , eport)


            try:
                print("도전1",protocol,ip_address,internal_port,upnp_content)
                print(type(u.lanaddr))

                upnp = u.addanyportmapping(eport, protocol, ip_address, internal_port, upnp_content, '')
                print(upnp)
            except Exception as e:
                print("도전2",protocol,ip_address,internal_port,upnp_content)
                print(u.lanaddr)
                upnp = u.addportmapping(eport, protocol, ip_address, internal_port, upnp_content, '')
                print(upnp)

            if upnp:
                print('Success. Now waiting for some HTTP request on %u' ,upnp)
                #DB에 저장 + 체크 

                try:
                    upnp_object = Upnp_list()
                    upnp_object.server_ip = ip_address
                    upnp_object.internal_port = internal_port
                    upnp_object.external_port = upnp
                    upnp_object.protocol = protocol
                    upnp_object.content = upnp_content
                    upnp_object.save()
                    result = True
                except Exception as e:
                    print("-------11",e)
                    ret["data"].append({
                        'eport' : upnp,
                        'result': result
                    })
                    return JsonResponse(ret)
            
            else:
                print("come to else part")
                ret["data"].append({
                    'result': result
                })
                return JsonResponse(ret)

        except Exception as e:
            print("-------22",e)
            ret["data"].append({
                'result': result
            })
            return JsonResponse(ret)
    else:
        return redirect