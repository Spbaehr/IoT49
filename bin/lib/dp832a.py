import ivi
import socket

# https://github.com/python-ivi
# https://github.com/python-ivi/python-ivi/blob/master/README.md

dns = "dp832a.home"   # actually used below
ip  = "192.168.10.137"
mac = "00:19:AF:5B:77:26"

# helper to make result from config easier to use
class Dotdict(dict):
    __getattr__ = dict.get
    def __getstate__(self): return self.__dict__
    def __setstate__(self, d): self.__dict__.update(d)


class DP832A:

    def __init__(self, ip=dns):
        ip = socket.gethostbyname(ip)
        print("Connecting to DP832A at {} ...".format(ip))
        self.ip = ip
        self.dp = ivi.rigol.rigolDP832A("TCPIP0::" + ip + "::INSTR")

    # helpers ... overcome bug in ivi library for DP832A
    def _ovp_enabled(self, ch):
        return self.dp._ask("source:voltage:protection:state?") == 'ON'

    def _ocp_enabled(self, ch):
        return self.dp._ask("source:current:protection:state?") == 'ON'

    def help(self):
        return self.dp.help()

    # channel configuration
    #   channel: 1 ... 3
    #   optional arguments: enabled=True|False, v=value, i=value, ovp=value|None, ocp=value|None
    #   returns current config as a dict
    #   Examples:
    #      config(2).v   --> current voltage setting of channel
    #      config(1, v=15, ovp=20, ocp=None)  --> sets voltage to 15V, ...
    def config(self, ch, **kwargs):
        assert ch >= 1 and ch <= 3, "Invalid channel {} outside range 1 ... 3".format(ch)
        out = self.dp.outputs[ch-1]
        out.enabled   # set channel for subsequent commands
        if "enabled" in kwargs: out.enabled = kwargs["enabled"]
        if "v" in kwargs: out.voltage_level = kwargs["v"]
        if "i" in kwargs: out.current_limit = kwargs["i"]
        if "ovp" in kwargs:
            if kwargs["ovp"]: out.ovp_limit = kwargs["ovp"]
            self.dp._write(":OUTPut:OVP {}".format("ON" if kwargs["ovp"] else "OFF"))
        if "ocp" in kwargs:
            if kwargs["ocp"]: self.dp._write(":OUTPut:OCP:VALue {}".format(kwargs["ocp"]))
            self.dp._write(":OUTPut:OCP {}".format("ON" if kwargs["ocp"] else "OFF"))

        return Dotdict({
            'enabled': out.enabled,
            'v': out.voltage_level,
            'i': out.current_limit,
            'ovp': out.ovp_limit if self._ovp_enabled(ch) else None,
            'ocp': self.dp._ask(":OUTPut:OCP:VALue?") if self._ocp_enabled(ch) else None,
            'v_max': out.query_voltage_level_max(0),
            'i_max': out.query_current_limit_max(0)
            })

    # measure present channel voltage
    def v(self, ch):
        assert ch >= 1 and ch <= 3, "Invalid channel {} outside range 1 ... 3".format(ch)
        out = self.dp.outputs[ch-1]
        return out.measure('voltage')

    # measure present channel current
    def i(self, ch):
        assert ch >= 1 and ch <= 3, "Invalid channel {} outside range 1 ... 3".format(ch)
        out = self.dp.outputs[ch-1]
        return out.measure('current')

    def p(self, ch):
        assert ch >= 1 and ch <= 3, "Invalid channel {} outside range 1 ... 3".format(ch)
        CH = [ '', 'CH1', 'CH2', 'CH3']
        return float(self.dp._ask(":MEASure:POWEr? {}".format(CH[ch])))

    # instrument temperature
    def temperature(self):
        return self.dp._ask(":SYSTem:SELF:TEST:TEMP?")
