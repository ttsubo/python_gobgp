import json
import sys
from fabric.api import local


def add_neighbor(neighbor_address, peer_as):
    cmd = 'gobgp -j neighbor add {0} as {1}'.format(neighbor_address, peer_as)
    ret = local(cmd, capture=True)
    return ret

def main(argv):
    neighbor_address = argv[1]
    peer_as = argv[2]
    ret = add_neighbor(neighbor_address, peer_as)
    if ret == "":
        print "Success!"
    else:
        print "Error!"

if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print "Usage: python neighbor_add.py [neighbor_address] [peer_as]"
        sys.exit()
    else:
        main(sys.argv)
