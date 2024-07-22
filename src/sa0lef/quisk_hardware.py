from __future__ import absolute_import
from __future__ import absolute_import
from __future__ import division

import quisk as QS
from sa0lef.station_hardware import StationAPI

import wx, traceback, types
try:
  import serial
except:
  serial = None
from QS.quisk_hardware_model import Hardware as BaseHardware

class Hardware(BaseHardware):

    def __init__(self, app, conf):
      BaseHardware.__init__(self, app, conf)
      self.api_sg231 = StationAPI('http://10.0.0.51/api/')
      self.api_switch_inside = StationAPI('http://10.0.0.234/api/')
      self.api_atu100ctl = StationAPI('http://10.0.0.235/api')

      
