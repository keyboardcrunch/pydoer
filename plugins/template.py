import PluginManager
from datetime import datetime

class Reporting(PluginManager.Plugin):
    def __init__(self):
        self.name = 'Template'
        self.description = 'Template description'
        self.interval = 30 # Minutes

    def execute(self):
        """ The main plugin method """
        #raise NotImplementedError
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{timestamp} : {self.name} was executed.")
