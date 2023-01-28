import sys
sys.path.insert(1,'WGSdb/check_1/store/security')
sys.path.insert(1,'WGSdb/check_2/logo')
sys.path.insert(1,'WGSdb/check_3/config/root/store/webtemp')

from checkUp import *
from buners import *

from time import sleep
from rich.progress import track
from termcolor import colored

import colorama
import rich
import os

clear = lambda: os.system('clear')
clear()