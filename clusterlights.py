import pygatt
import logging
import json
import sys
import binascii


configFile = "config.json"

logging.basicConfig()
logging.getLogger('pygatt').setLevel(logging.DEBUG)

# The BGAPI backend will attemt to auto-discover the serial device name of the
# attached BGAPI-compatible USB adapter.
adapter = pygatt.GATTToolBackend()

def load_config(filename):
    return json.load(open(configFile, "r"))

def conf_to_bytearray(confValue):
    hex_string = confValue.replace(":", "")
    return bytearray.fromhex(hex_string)

def perc_to_hex(maxHex, minHex, percentage):
    raise NotImplementedError

def parse_command(command, config):
    if command in config["command"]:
        if command == "mode":
            print "henkie"
        elif command == "brightness":
            print "shoarma"
        else:
            return conf_to_bytearray(config["command"][command])



command = sys.argv[1]
config = load_config(configFile)
bytesToSend = parse_command(command, config)

print binascii.hexlify(bytesToSend)

try:
    print "henk"
    adapter.start()
    device = adapter.connect(mac)
    device.char_write_handle(handle, bytesToSend)

finally:
    print "henk"
    adapter.stop()
