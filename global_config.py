import json
import sys
from fabric.api import local


def global_config(local_as, router_id):
    cmd = 'gobgp -j global as {0} router-id {1}'.format(local_as, router_id)
    ret = local(cmd, capture=True)
    return ret

def main(argv):
    local_as = argv[1]
    router_id = argv[2]
    ret = global_config(local_as, router_id)
    if ret == "":
        print "Success!"
    else:
        print "Error!"

if __name__ == '__main__':
    if (len(sys.argv) != 3):
        print "Usage: python global_config.py [local_as] [router_id]"
        sys.exit()
    else:
        main(sys.argv)
