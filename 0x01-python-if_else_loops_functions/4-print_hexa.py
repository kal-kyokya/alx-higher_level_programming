#!/usr/bin/python3
nums = "0123456789abcdef"
for num in range(0, 99):
    if (int(num / 16) == 0):
        print("{} = 0x{}".format(num, nums[num % 16]))
        continue
    print("{} = 0x{}{}".format(num, int(num / 16), nums[num % 16]))
