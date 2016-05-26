import json
import sys
from fabric.api import local


def global_config(local_as, router_id, mgmt_addr):
    cmd = 'gobgp -j global as {0} router-id {1} -u {2}'.format(local_as, router_id, mgmt_addr)
    ret = local(cmd, capture=True)
    return ret

def main(argv):
    local_as = argv[1]
    router_id = argv[2]
    mgmt_addr = argv[3]
    ret = global_config(local_as, router_id, mgmt_addr)
    if ret == "":
        print "Success!"
    else:
        print "Error!"

if __name__ == '__main__':
    if (len(sys.argv) != 4):
        print "Usage: python global_config.py [local_as] [router_id], [mgmt_addr]"
        sys.exit()
    else:
        main(sys.argv)
