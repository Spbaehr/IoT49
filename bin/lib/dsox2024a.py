import ivi
import socket

# https://github.com/python-ivi
# https://github.com/python-ivi/python-ivi/blob/master/README.md

dns = "dsox2024a.home"   # actually used below
ip  = "192.168.10.146"
mac = "00:30:D3:29:95:87"

# helper to make result from config easier to use
class Dotdict(dict):
    __getattr__ = dict.get
    def __getstate__(self): return self.__dict__
    def __setstate__(self, d): self.__dict__.update(d)

class DSOX2024A:

    # connect to scope and reset (default) to known state
    def __init__(self, ip=dns):
        ip = socket.gethostbyname(ip)
        print("Connecting to DSOX2024A at {} ...".format(ip))
        self.ip = ip
        self.dso = ivi.agilent.agilentDSOX2024A("TCPIP0::" + ip + "::INSTR")

    def _map_properties(self, obj, set, properties):
        for name, value in set.items():
            setattr(obj, name, value)
        res = {}
        for p in properties:
            res[p] = getattr(obj, p)
        return res

    # release TCP connection to scope
    def close(self):
        self.dso.close

    # put scope in known configuration (same as pressing Default Setup key)
    def reset(self):
        self.dso._write(':SYSTem:PRESet')

    # same as pressing Autoscale button
    def autoscale(self):
        self.dso._write(':AUToscale')

    # save current display
    # valid formats: png, bmp, bmp8
    def screenshot(self, filename='dsox2024a_screenshot.png', invert=True, format='png'):
        # self.dso._write(':SAVE:IMAGe:INKSaver OFF')
        png = self.dso.display.fetch_screenshot(invert=invert, format=format)
        with open(filename, 'wb') as f:
            f.write(png)

    # return last acquired waveform for specified channel
    #     return { t: (), v: () }
    def acquire(self, ch):
        assert ch >= 1 and ch <= 4, "Invalid channel {} outside range 1 ... 4".format(ch)
        wf = self.dso.channels[ch-1].measurement.fetch_waveform()
        wf = list(zip(*wf))
        return Dotdict({ 't': wf[0], 'v': wf[1] })

    # save present scope setup to file
    def save_setup(self, filename='dsox2024a_setup.dat'):
        setup = self.dso.system.fetch_setup()
        with open(filename, 'wb') as f:
            f.write(setup)

    # load setup previously created with save_setup
    def load_setup(self, filename='dsox2024a_setup.dat'):
        with open(filename, 'rb') as f:
            setup = f.read()
        self.dso.system.load_setup(setup)

    # channel configuration
    #   ch: channel number, 1 ... 4
    def channel(self, ch, **kwargs):
        assert ch >= 1 and ch <= 4, "Invalid channel {} outside range 1 ... 4".format(ch)
        return Dotdict(self._map_properties(self.dso.channels[ch-1], kwargs,
            [ 'enabled', 'range', 'scale', 'coupling', 'invert', 'offset',
              'input_impedance', 'input_frequency_max', 'bw_limit',
              'probe_attenuation', 'probe_id', 'probe_skew',
              'name', 'label' ] ))

    # timebase configuration
    def timebase(self, **kwargs):
        return Dotdict(self._map_properties(self.dso.timebase, kwargs,
            [ 'mode', 'position', 'range', 'reference', 'scale' ] ))

    # trigger configuration
    #   source: 1 ... 4, 'chan1' ... 'chan4', 'ext', 'wgen', 'line'
    def trigger(self, **kwargs):
        t = self.dso.trigger
        if 'source' in kwargs:
            s = kwargs['source']
            if isinstance(s, int):
                s = [ '', 'chan1', 'chan2', 'chan3', 'chan4' ][s]
            self.dso._write(':TRIGger:SOURce ' + s)
            kwargs.pop('source', None)
        return Dotdict(self._map_properties(t, kwargs,
            [ 'source', 'level', 'type', 'continuous', 'coupling', 'holdoff' ] ))

    # acquisition configuration
    def acquisition(self, **kwargs):
        return Dotdict(self._map_properties(self.dso.acquisition, kwargs,
            [ 'type', 'start_time', 'time_per_record',
              'sample_rate', 'sample_mode', 'record_length',
              'number_of_averages', 'number_of_envelopes', 'number_of_points_minimum' ] ))

    # waveform generator configuration
    #   waveform = sine, square, ramp_up, pulse, noise, dc
    def waveform_generator(self, **kwargs):
        out = self.dso.outputs[0]
        if 'enabled' in kwargs: out.enabled = kwargs['enabled']
        kwargs.pop('enabled', None)
        p = self._map_properties(out.standard_waveform, kwargs,
            [ 'waveform', 'amplitude', 'dc_offset', 'frequency', 'duty_cycle_high', 'start_phase' ] )
        p['enabled'] = out.enabled
        return Dotdict(p)

    # low-level library commands
    def help(self):
        return self.dso.help()
