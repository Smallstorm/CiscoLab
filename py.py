# from telnetlib import Telnet
import telnetlib
telnet = telnetlib.Telnet('172.17.9.151',4009,15)

def to_bytes(line):
    return f"{line}\n".encode("utf-8")

with open('conf.txt') as f:
    for line in f.readlines():
        telnet.write(to_bytes(line))
        telnet.write(b"\n")
        # print(telnet.read_until(b'exit'))
f.close()

print(telnet.read_until(b'#'))

telnet.close()