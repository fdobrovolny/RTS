"""
RTS - RealTime Isometric pygame-opengl based game.
Copyright (C) 2014 Filip Dobrovolny

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import datetime


class Logger(object):
    """
    classdocs
    """

    def __init__(self, print2Console=False, logfile=None):
        """
        Constructor
        """
        if logfile is None:
            self.logfile = "../logs/" + str(datetime.date.today())
        else:
            self.logfile = logfile
        self.print2Console = print2Console
        self.levels = {0: "DEBUG:", 1: "INFO", 2: "WARN", 3: "ERROR"}

    def log(self, level, name, message):
        if self.print2Console:
            print(
                str(datetime.datetime.now().time()),
                self.levels[level],
                name + ":",
                message,
            )
