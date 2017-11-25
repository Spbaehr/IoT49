import ivi
import socket

# https://github.com/python-ivi
# https://github.com/python-ivi/python-ivi/blob/master/README.md

dns = "dmm34461a.home"   # actually used below
ip  = "192.168.10.148"
mac = "80:09:02:06:15:42"

class DMM34461A:

    # connect to scope and reset (default) to known state
    def __init__(self, ip=dns, reset=True):
        ip = socket.gethostbyname(ip)
        print("Connecting to DMM34461A at {} ...".format(ip))
        self.ip = ip
        self.dmm = ivi.agilent.agilent34401A("TCPIP0::" + ip + "::INSTR")
        if reset: self.reset()

    # Configure/inquire measurement mode
    #   mode:  'dc_volts', 'ac_volts', 'dc_current', 'ac_current',
    #          'resistance', 'two_wire_resistance', 'four_wire_resistance',
    #          'frequency', 'period', 'continuity', 'diode', 'capacitance',
    #          'temperature'
    #   returns current configuration
    def config(self, mode=None):
        modes = {
            'dc_volts': 'VOLT:DC',
            'ac_volts': 'VOLT:AC',
            'dc_current': 'CURR:DC',
            'ac_current': 'CURR:AC',
            'resistance' : 'RES',
            'two_wire_resistance' : 'RES',
            'four_wire_resistance' : 'FRES',
            'frequency': 'FREQ',
            'period': 'PER',
            'continuity': 'CONT',
            'diode': 'DIOD',
            'capacitance': 'CAP',
            'temperature': 'TMEP'
        }
        cmd = modes.get(mode, None)
        if cmd: self.dmm._write('CONF:' + cmd)
        conf = self.dmm._ask('CONF?').replace('"', '').split(' ')[0]
        if conf == 'VOLT': return 'dc_volts'
        for k, v in modes.items():
            if v == conf: return k
        return "UNKNOWN configuration: " + conf

    def read(self):
        return self.dmm.measurement.read(0)

    # release TCP connection to scope
    def close(self):
        self.dmm.close

    # put scope in known configuration (same as pressing Default Setup key)
    def reset(self):
        self.dmm._write(':SYSTem:PRESet')

    # low-level library commands
    def help(self):
        return self.dmm.help()
