import math
import os
import random
import re
import sys
import functools
from operator import itemgetter, attrgetter

if __name__ == '__main__':
    n, k = list(map(int, input().strip().split()))
    s = sorted(list(map(ord, input().strip())))