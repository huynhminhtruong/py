import math
import os
import random
import re
import sys
import functools
from operator import itemgetter, attrgetter

if __name__ == '__main__':
    n, m = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    d = dict()