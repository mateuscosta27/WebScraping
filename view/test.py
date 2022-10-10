import os 
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
sys.path.insert(0,os.path.abspath(os.curdir))
from controller import Controller