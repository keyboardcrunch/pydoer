from PluginManager import PluginCollection
import schedule
import threading
import time

plugins = PluginCollection('plugins')
print() # Space after plugin enumeration

def pexec(plugin_name):
    plugins.execute_plugin(plugin_name)

def worker(plug):
    schedule.every(plug.interval).minutes.do(pexec, plug.name)
    while True:
        schedule.run_pending()
        time.sleep(28)

if __name__ == "__main__":
    for plug in plugins.list_plugins():
        t = threading.Thread(target=worker, args=(plug,))
        t.daemon = True # True ensures threads close with main
        t.start()

    while True:
        print(f'{threading.active_count() -1} threads still active.')
        time.sleep(30)
