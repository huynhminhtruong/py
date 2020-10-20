import math
import os
import random
import re
import sys
from operator import itemgetter, attrgetter

if __name__ == '__main__':
    n, k = [int(x) for x in input().strip().split()]
    y = [int(x) for x in input().strip().split()]
    r = 0