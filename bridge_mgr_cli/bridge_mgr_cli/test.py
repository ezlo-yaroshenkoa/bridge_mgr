from pyroute2.iproute import IPRoute

ip = IPRoute()
try:
    links = ip.get_links()
    result = ip.link_create(ifname='br12', kind='bridge')
finally:
    pass

idx = ip.link_lookup(ifname='br12')[0]
ip.link_remove(idx)
k = 4

