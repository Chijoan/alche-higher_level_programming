#!/usr/bin/python3
print("\n".join("{} = 0x{}".format(i, hex(i)[2:]) for i in range(99)))
