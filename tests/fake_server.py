from tornado.tcpserver import TCPServer
from tornado.ioloop import IOLoop
from tornado.gen import *
from time import sleep


class TcpConnection(object):
    def __init__(self,stream,address):
        self._stream=stream
        self._address=address
        self._stream.set_close_callback(self.on_close)
        self.send_messages()

    def send_messages(self):
        sleep(2)
        self._stream.write(b'\xf1\x00\x02\x00\x05')
        print("SEND TRASH")
        sleep(2)
        self._stream.write(b'\x12\x00\x00')
        print("SEND ON")

        sleep(5)
        self._stream.write(b'\x20\x00\x03')
        sleep(1)
        self._stream.write(b'\x01')
        sleep(1)
        self._stream.write(b'\x02')
        sleep(1)
        self._stream.write(b'\x03')
        print("SEND COLOR")

        sleep(5)
        self._stream.write(b'\x13\x00\x00')
        print("SEND OFF")

    def on_close(self):
        print("connection lost {}".format(self._address))

class MonitorServer(TCPServer):

    def handle_stream(self,stream,address):
        print("new connection {}".format(address))
        conn = TcpConnection(stream,address)

if  __name__=='__main__':
    print('server start .....')
    server=MonitorServer()
    server.listen(9999)
    IOLoop.instance().start()
