#!/bin/python3

import math
import os
import random
import re
import sys



n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

arr.reverse()

arrstring = ' '.join(str(e) for e in arr)

print(arrstring)
