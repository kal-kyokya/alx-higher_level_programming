#!/usr/bin/env python3
import dis
add = __import__('10-main').add
print(dis.dis(add))
