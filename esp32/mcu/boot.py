import micropython, machine, network, time, sys, binascii

# edit to match your WiFi settings
known_wifi_nets = {
    # SSID : PSK (passphrase)
    b"EECS-PSK": "Thequickbrown",
}

# board identifier
def get_id():
    return machine.nvs_getstr('ID')

# micropython internals
micropython.alloc_emergency_exception_buf(100)

# fix path
sys.path.append('/flash/lib')

# convenience functions
def mac_address():
    return binascii.hexlify(wlan.config('mac'), ':')

def ip_address():
    return wlan.ifconfig()[0]

# establish wifi connection & initialize rtc with ntp time
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

def wifi_rtc():
    global wlan
    print("Connecting to WLAN ...")
    if wlan.isconnected(): return
    for ssid, _, sec, _, rssi, _ in wlan.scan():
        try:
            # print("try", ssid, sec, rssi, known_wifi_nets[ssid])
            wlan.connect(ssid, known_wifi_nets[ssid], 5000)
            break
        except KeyError:
            # SSID not in known nets
            # print("KeyError")
            pass
    # wait for connection to be established ...
    for _ in range(30):
        if wlan.isconnected(): break
        time.sleep_ms(100)
    if not wlan.isconnected():
        print("Unable to connect to WiFi")
        print("scan:", wlan.scan())
        wlan.disconnect()
    else:
        print("IP", wlan.ifconfig()[0])
        # fetch ntp time
        rtc = machine.RTC()
        rtc.ntp_sync(server="hr.pool.ntp.org")
        for _ in range(100):
            if rtc.synced(): break
            time.sleep_ms(100)
        if rtc.synced():
            print(time.strftime("%c", rtc.now()))
        else:
            print("Unable to get ntp time")

# connect to wifi
wifi_rtc()

# start servers
network.telnet.start()
network.ftp.start()
