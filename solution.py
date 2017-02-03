import struct
from enum import Enum

class MessageTypes(Enum):
    """
    Types of OpenFlow protocol messages.
    Source: http://archive.openflow.org/wk/images/c/c5/Openflow_packet_format.pdf
    """
    HELLO = 0x00
    ERROR = 0x01
    ECHO_REQUEST = 0x02
    ECHO_REPLY = 0x03
    VENDOR = 0x04
    FEATURES_REQUEST = 0x05
    FEATURES_REPLY = 0x06
    GET_CONFIG_REQUEST = 0x07
    GET_CONFIG_REPLY = 0x08
    SET_CONFIG = 0x09
    PACKET_INPUT_NOTIFICATION = 0x0a
    FLOW_REMOVED_NOTIFICATION = 0x0b
    PORT_STATUS_NOTIFICATION = 0X0c
    PACKET_OUTPUT = 0x0d
    FLOW_MODIFICAITON = 0x0e
    PORT_MODIFICATION = 0x0f
    STATS_REQUEST = 0x10
    STATS_REPLY = 0x11
    BARRIER_REQUEST = 0x12
    BARRIER_REPLY = 0x13

class OpenFlowMessage:
    """
    Entity that represents the OpenFlow protocol message.
    Usage:
    $ my_msg = OpenFlowMessage()
    $ my_msg.load_from_file("mynicefile.bin", "rb")
    $ my_msg.show_info()
    """

    def __init__(self):
        self.version = 0
        self.type = MessageTypes.ERROR.value
        self.length = -1
        self.transaction_id = 1<<31

    def load_from_file(self, path, mode):
        data = open(path, mode).read()
        dezip = struct.unpack('b b h i', data)
        self.version, self.type, self.length, self.transation_id = dezip

    def show_info(self):
        print("OpenFlow protocol version: " + str(hex(self.version)))
        print("Message of type " + str(hex(self.type)) + " - " + MessageTypes(self.type).name)
        print("Length: " + str(hex(self.length)))
        print("Transaction id: " + str(hex(self.transaction_id)))

msg = OpenFlowMessage()
msg.load_from_file("ofpt_hello.dat", "rb")
msg.show_info()

