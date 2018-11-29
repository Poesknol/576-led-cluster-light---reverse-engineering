import pygatt
import logging
import time

mac = "24:35:CC:09:88:57"

handle = 37

logging.basicConfig()
logging.getLogger('pygatt').setLevel(logging.DEBUG)
# The BGAPI backend will attemt to auto-discover the serial device name of the
# attached BGAPI-compatible USB adapter.
adapter = pygatt.GATTToolBackend()

try:
    adapter.start()
    device = adapter.connect(mac)
    device.char_write_handle(handle, bytearray([1, 1, 1, 0]))

finally:
    adapter.stop()
