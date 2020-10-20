import math
import os
import random
import re
import sys
from operator import itemgetter, attrgetter

if __name__ == '__main__':
    n, k = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    b, p, s = list(), 0, ""