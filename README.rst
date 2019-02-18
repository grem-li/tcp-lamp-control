===============================
TCP Lamp
===============================

**Test project for RGB lamp with tcp-server control**

Example
_______________________________

>>> from tcp_lamp import client
>>> client.start()
Input server addres (default 127.0.0.1): 192.168.0.2
Input server port (default 9999): 007

or just

>>> from tcp_lamp import client
>>> client.start('127.0.0.1', 9999)

also you can use shell

$ tcp_lamp --host 192.168.0.3 --port 7777

