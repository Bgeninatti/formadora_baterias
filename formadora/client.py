import time
import binascii
import struct
import zmq

from ClaptonBase.containers import Package
from ClaptonBase.clients import TKLanClient


REQUIRED_PACKAGES = {
    'banderas': {
        "label": "Banderas del sistema",
        "package": Package(destination=8, function=1, data=struct.pack('BB', 0, 1)),
        },
    'temperatura_bateria':  {
        "label": "Temperatura de batería",
        "package": Package(destination=8, function=1, data=struct.pack('BB', 1, 1)),
        },
    'set_corriente':  {
        "label": "Set de corriente  /10",
        "package": Package(destination=8, function=1, data=struct.pack('BB', 2, 1)),
        },
    'set_corriente_corregido':  {
        "label": "Set de corriente corregido /10",
        "package": Package(destination=8, function=1, data=struct.pack('BB', 3, 1)),
        },
    'corriente_control':  {
        "label": "Corriente para control",
        "package": Package(destination=8, function=1, data=struct.pack('BB', 4, 1)),
        },
    'corriente_display':  {
        "label": "Corriente en display",
        "package": Package(destination=8, function=1, data=struct.pack('BB', 5, 1)),
        },
    'carga_paso': {
        "label": "Carga del PASO",
        "package": Package(destination=8, function=1, data=struct.pack('BB', 6, 2)),
    },
    'carga_total':  {
        "label": "Carga TOTAL",
        "package": Package(destination=8, function=1, data=struct.pack('BB', 8, 2)),         },
    'set_carga_paso':  {
        "label": "Set carga del PASO",
        "package": Package(destination=8, function=1, data=struct.pack('BB', 10, 2)),
    },
    'maquina_estado': {
        "label": "Maquina de estado",
        "package": Package(destination=8, function=1, data=struct.pack('BB', 12, 1)),
    },
    'paso_actual':  {
        "label": "Paso actual",
        "package": Package(destination=8, function=1, data=struct.pack('BB', 13, 1)),
    },
    'set_corriente':  {
        "label": "Set de corriente /10 (paso actual)",
        "package": Package(destination=8, function=1, data=struct.pack('BB', 14, 1)),
    },
    'set_carga':  {
        "label": "Set de carga x5 (paso actual)",
        "package": Package(destination=8, function=1, data=struct.pack('BB', 15, 1)),
    },
    'temperatura_inferior':  {
        "label": "Temperatura inferior (paso actual)",
        "package": Package(destination=8, function=1, data=struct.pack('BB', 16, 1)),
    },
    'temperatura_superior':  {
        "label": "Temperatura superior (paso actual)",
        "package": Package(destination=8, function=1, data=struct.pack('BB', 17, 1)),
    },
    'temperatra_disipador': {
        "label": "Temperatura del disipador",
        "package": Package(destination=8, function=1, data=struct.pack('BB', 18, 1)),
    },
    'identificacion': {
        "label": "Identificacion 676",
        "package": Package(destination=8, function=0),
    }
}


def as_int(value):
    return struct.unpack('B', value)[0]


def as_short(value):
    return struct.unpack('H', value)[0]


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

    @property
    def banderas(self):
        rta = self._get_data(
            REQUIRED_PACKAGES['banderas']['package'],
        )
        return binascii.hexlify(rta)

    @property
    def temperatura_bateria(self):
        rta = self._get_data(
            REQUIRED_PACKAGES['temperatura_bateria']['package'],
        )
        return as_int(rta)

    @property
    def set_corriente(self):
        rta = self._get_data(
            REQUIRED_PACKAGES['set_corriente']['package'],
        )
        return as_int(rta) / 10.0

    @property
    def set_corriente_corregido(self):
        rta = self._get_data(
            REQUIRED_PACKAGES['set_corriente_corregido']['package'],
        )
        return as_int(rta) / 10.0

    @property
    def corriente_control(self):
        rta = self._get_data(
            REQUIRED_PACKAGES['corriente_control']['package'],
        )
        return as_int(rta)

    @property
    def corriente_display(self):
        rta = self._get_data(
            REQUIRED_PACKAGES['corriente_display']['package'],
        )
        return as_int(rta) / 10.0

    @property
    def carga_paso(self):
        rta = self._get_data(
            REQUIRED_PACKAGES['carga_paso']['package'],
        )
        return as_short(rta)

    @property
    def carga_total(self):
        rta = self._get_data(
            REQUIRED_PACKAGES['carga_total']['package'],
        )
        return as_short(rta)

    @property
    def set_carga_paso(self):
        rta = self._get_data(
            REQUIRED_PACKAGES['set_carga_paso']['package'],
        )
        return as_short(rta)

    @property
    def maquina_estado(self):
        rta = self._get_data(
            REQUIRED_PACKAGES['maquina_estado']['package'],
        )
        return binascii.hexlify(rta)

    @property
    def paso_actual(self):
        rta = self._get_data(
            REQUIRED_PACKAGES['paso_actual']['package'],
        )
        return as_int(rta)

    @property
    def set_carga(self):
        rta = self._get_data(
            REQUIRED_PACKAGES['set_carga']['package'],
        )
        return as_int(rta) * 5.0

    @property
    def temperatura_inferior(self):
        rta = self._get_data(
            REQUIRED_PACKAGES['temperatura_inferior']['package'],
        )
        return as_int(rta)

    @property
    def temperatura_superior(self):
        rta = self._get_data(
            REQUIRED_PACKAGES['temperatura_superior']['package'],
        )
        return as_int(rta)

    @property
    def temperatra_disipador(self):
        rta = self._get_data(
            REQUIRED_PACKAGES['temperatra_disipador']['package'],
        )
        return as_int(rta)

    @property
    def identificacion(self):
        rta = self._get_data(
            REQUIRED_PACKAGES['identificacion']['package'],
        )
        return binascii.hexlify(rta)

    def __repr__(self):
        msg = ""
        for key in REQUIRED_PACKAGES:
            value = getattr(self, key)
            msg += "{key}: {value}\n".format(key=key, value=value)
        return msg
