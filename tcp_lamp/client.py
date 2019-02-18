from tcp_lamp.lamp import TheLamp
from tcp_lamp.utils import int_from_bytes
from time import sleep
from tornado import gen
from tornado.ioloop import IOLoop
from tornado.iostream import StreamClosedError
from tornado.tcpclient import TCPClient


class Client(TCPClient):

    @gen.coroutine
    def run(self, host, port):
        lamp = TheLamp()
        while True:
            try:
                stream = yield self.connect(host, port)

                while True:
                    method = yield stream.read_bytes(1)
                    length = yield stream.read_bytes(2)
                    value = yield stream.read_bytes(int_from_bytes(length))
                    lamp.api(method, value)
            except StreamClosedError:
                print("The server is offline, lets try later")
                sleep(10)


def start(host=None, port=None):
    if not host:
        host = str(raw_input("Input server addres (default 127.0.0.1): ")) or "127.0.0.1"
    if not port:
        try:
            port = int(raw_input("Input server port (default 9999): "))
        except ValueError:
            port = 9999

    Client().run(host, port)
    IOLoop.instance().start()


def stop():
    IOLoop.instance().stop()

