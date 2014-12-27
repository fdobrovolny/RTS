import datetime
'''
Created on 27. 12. 2014

@author: fdobrovolny
'''

class Logger(object):
    '''
    classdocs
    '''


    def __init__(self, print2Console=False, logfile="../logs/"+str(datetime.date.today())):
        '''
        Constructor
        '''
        self.print2Console = print2Console
        self.levels = {0 : "DEBUG:", 1 : "INFO", 2 : "WARN", 3 : "ERROR"}
    
    def log(self, level, name, message):
        if self.print2Console:
            print(str(datetime.datetime.now().time()),self.levels[level], name + ":", message)