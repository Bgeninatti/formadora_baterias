import time
import binascii
import struct
import zmq

from ClaptonBase.containers import Package
from ClaptonBase.clients import TKLanClient


REQUIRED_PACKAGES = (
    Package(destination=4, function=1, data=struct.pack('BB', 1, 8)), # Temperaturas
    Package(destination=4, function=1, data=struct.pack('BB', 9, 2)), # Salidas 420
    Package(destination=5, function=1, data=struct.pack('BB', 1, 8)), # Temperaturas
    Package(destination=5, function=1, data=struct.pack('BB', 9, 2)), # Salidas 420
    Package(destination=6, function=1, data=struct.pack('BB', 1, 8)), # Temperaturas
    Package(destination=6, function=1, data=struct.pack('BB', 9, 2)), # Salidas 420
    Package(destination=6, function=1, data=struct.pack('BB', 11, 2)), # Setpoints
    Package(destination=6, function=1, data=struct.pack('BB', 13, 1)), # Entradas digitales
    Package(destination=6, function=1, data=struct.pack('BB', 206, 18)), # pid
    Package(destination=14, function=0), # Identificacion 676
)


class TKL688:

    def __init__(self, ip, timeout=5):
        self._client = TKLanClient(ip)
        self.timeout = timeout

    def _get_data(self, package):
        self._client.send_package(package)
        timeout = time.time() + self.timeout

        while time.time() < timeout:
            try:
                rta = self._client.recv_response()
                return binascii.unhexlify(rta['data'])
            except zmq.ZMQError as ex:
                if time.time() > timeout:
                    raise ex

    # @property
    # def temperatura_entrada(self):
        # data = self._get_data(REQUIRED_PACKAGES[4])
        # temperaturas = parsers.temperaturas(data)
        # return temperaturas['temperatura_a']
