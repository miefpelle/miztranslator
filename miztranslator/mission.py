# -*- coding: UTF-8 -*-

################################################################################

class Event(object):
    """docstring for Event"""
    def __init__(self, arg):
        super(Event, self).__init__()
        self.arg = arg

class Custom(object):
    """docstring for Custom"""
    def __init__(self, arg):
        super(Custom, self).__init__()
        self.arg = arg

class CustomStartup(object):
    """docstring for CustomStartup"""
    def __init__(self, arg):
        super(CustomStartup, self).__init__()
        self.arg = arg

class Result(object):
    """docstring for Result"""
    def __init__(self, arg):
        super(Result, self).__init__()
        self.arg = arg

################################################################################

class Weather(object):
    """Weather -- representing the weather in DCS"""
    atmosphereType = 0
    qnh = 0
    name = ""
    enableFog =
    wind = {'atGround' : {'speed' : 0, 'dir' : 0},
        'at2000' : {'speed' : 0, 'dir' : 0},
        'at8000' : {'speed' : 0, 'dir' : 0}
        }
    turbulence = {'atGround' : 0, 'at2000' : 0, 'at8000' : 0}
    season = {'iseason' : 0, 'temperature' : 0}
    fog = {'density' : 0, 'visibility' : 0, 'thickness' : 0}
    visibility = {'distance' : 0}
    clouds = {'density' : 0, 'thickness' : 0, 'base' : 0, 'iprecptns' : 0}
    cyclones = {}
    def __init__(self, arg):
        super(Weather, self).__init__()
        self.arg = arg

class Zone(object):
    """docstring for Zone"""
    y = 0.0
    x = 0.0
    radius = 0
    zoneId = 0
    color = [ 0, 0, 0, 0.0 ]
    hidden = True
    name = ""
    def __init__(self, arg):
        super(Zone, self).__init__()
        self.arg = arg

class Role(object):
    """docstring for Role"""
    name = ""
    blue = 0
    red = 0
    def __init__(self, arg):
        super(Role, self).__init__()
        self.arg = arg

class Trig(object):
    """docstring for Trig"""
    actions = []
    func = []
    flag = []
    conditions = []
    funcStartup = []

    def __init__(self, arg):
        super(Trig, self).__init__()
        self.arg = arg

class Result(object):
    """docstring for Result"""
    # offline, red und blue bestehen jeweils aus einem "conditions", "actions"
    # und "func" Array -- schauen, wie sich das am besten abbilden lässt...
    offline = []
    red = []
    blue = []
    total = 3

    def __init__(self, arg):
        super(Result, self).__init__()
        self.arg = arg

class GroundControl(object):
    """docstring for GroundControl"""
    isPilotControlVehicles = False
    roles = []
    def __init__(self, arg):
        super(GroundControl, self).__init__()
        self.arg = arg


class Mission(object):
    """docstring for Mission"""
    theatre = "Caucasus"
    descriptionText = ""
    descriptionBlueTask = ""
    descriptionRedTask = ""
    sortie = ""
    version = 0
    currentKey = 0
    startTime = 0
    #
    usedModules = []
    resourceCounter = []
    needModules = []
    pictureFileNameR = []
    pictureFileNameB = []
    #
    trig = Trig()
    result = Result()
    groundControl = GroundControl()
    weather = Weather()
    #
    # missionMap wird zu "map", aber "map" ist eine Funktion in Python...
    missionMap = {'centerX' : 0.0, 'centerY' : 0.0, 'zoom' : 0}
    coalitions = {'red' : [], 'blue' : []}
    def __init__(self, arg):
        super(Mission, self).__init__()
        self.arg = arg
