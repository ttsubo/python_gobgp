import json
import copy
import eventlet
from fabric.api import local

class Monitor(object):
    def __init__(self):
        self.old_results = {}

    def start(self):
        self._thread = eventlet.spawn(self._monitor_neighbor)

    def wait(self):
        self._thread.wait()

    def _monitor_neighbor(self):
        while True:
            results = {}
            cmd = 'gobgp -j neighbor'
            output = local(cmd, capture=True)
            ret = json.loads(output)
            for i in range(len(ret)):
               addr = ret[i]['conf']['remote_ip']
               state = ret[i]['info']['bgp_state']
               results[addr] = state
            change_result = self._extract_change_state(results)
            if change_result != {}:
                print change_result
            eventlet.sleep(5)

    def _extract_change_state(self, new_results):
        change_result = {}
        for target_addr in set(new_results) & set(self.old_results):
            new_state = new_results[target_addr]
            old_state = self.old_results[target_addr]
            if new_state != old_state:
                change_result[target_addr] = new_state
        self.old_results = copy.deepcopy(new_results)
        return change_result

if __name__ == '__main__':
    gobgp1 = Monitor()
    gobgp1.start()
    gobgp1.wait()
