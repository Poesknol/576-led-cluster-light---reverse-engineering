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

def brightness_to_bytearray(percentage):
    print "kakhoofd"
    if percentage >= 0 and percentage <= 100:
        value = int(mapping(percentage, 0, 100, config["brightnessMin"], config["brightnessMax"]))
        hexValue = config["command"]["brightness"][:-2] + format(value, '02x')
        print hexValue
        return conf_to_bytearray(hexValue)


def mapping(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    valueScaled = float(value - leftMin) / float(leftSpan)

    return rightMin + (valueScaled * rightSpan)

def parse_command(command, config):
    if command in config["command"]:
        if command == "mode":
            print "henkie"
        elif command == "brightness":
            return brightness_to_bytearray(int(sys.argv[2]))
        else:
            return conf_to_bytearray(config["command"][command])



command = sys.argv[1]
config = load_config(configFile)
bytesToSend = parse_command(command, config)

print binascii.hexlify(bytesToSend)
try:
    print "henk"
    adapter.start()
    device = adapter.connect(config["mac"])
    device.char_write_handle(config["handle"], bytesToSend)

finally:
    print "henk"
    adapter.stop()
