import json
import sys
from fabric.api import local


def add_neighbor(neighbor_address, peer_as, mgmt_addr):
    cmd = 'gobgp -j neighbor add {0} as {1} -u {2}'.format(neighbor_address, peer_as, mgmt_addr)
    ret = local(cmd, capture=True)
    return ret

def main(argv):
    neighbor_address = argv[1]
    peer_as = argv[2]
    mgmt_addr = argv[3]
    ret = add_neighbor(neighbor_address, peer_as, mgmt_addr)
    if ret == "":
        print "Success!"
    else:
        print "Error!"

if __name__ == '__main__':
    if (len(sys.argv) != 4):
        print "Usage: python add_neighbor.py [neighbor_address] [peer_as] [mgmt_addr]"
        sys.exit()
    else:
        main(sys.argv)
