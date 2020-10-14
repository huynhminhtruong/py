import math
import os
import random
import re
import sys

if __name__ == "__main__":
    s = input()
    last_val = s[len(s) - 1]
    s += 's' if (last_val != 's') else 'es'
    print(s)