import json
from fabric.api import local

BGP_ATTR_TYPE_NEXT_HOP = 3
BGP_ATTR_TYPE_MP_REACH_NLRI = 14

def get_global_rib():
    cmd = 'gobgp -j global rib'
    output = local(cmd, capture=True)
    ret = json.loads(output)
    rib_list = []
    for d in ret:
        buf = {}
        buf["prefix"] = d["prefix"]
        list = []
        nexthop = {}
        for p in d["paths"]:
            nexthop["best"] = p["best"]
            nexthop["nexthop"] = _get_nexthop(p)
            list.append(nexthop)
        buf["nexthop"] = list
        rib_list.append(buf)
    return rib_list

def _get_nexthop(path):
    for p in path['attrs']:
        if p['type'] == BGP_ATTR_TYPE_NEXT_HOP or p['type'] == BGP_ATTR_TYPE_MP_REACH_NLRI:
            return p['nexthop']

if __name__ == '__main__':
    ret = get_global_rib()
    print json.dumps(ret, indent=4)
