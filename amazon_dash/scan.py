import logging

from amazon_dash.exceptions import SocketPermissionError

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *


try:
    PermissionError
except NameError:
    import socket
    PermissionError = socket.error


def scan_devices(fn, lfilter, iface=None):
    """Sniff packages

    :param fn: callback on packet
    :param lfilter: filter packages
    :return: loop
    """
    try:
        sniff(prn=fn, store=0, filter="(udp and (port 67 or 68))", lfilter=lfilter, iface=iface)
    except PermissionError:
        raise SocketPermissionError
