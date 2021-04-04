#!/usr/bin/env/python2
# coding=utf-8

#imports
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import getpass
import urllib
import cookielib
from multiprocessing.pool import ThreadPool

try:
    import mechanize
except ImportError:
    os.system("pip2 install mechanize")

try:
    import requests
except ImportError:
    os.system("pip2 install requests")
from requests.exceptions import ConnectionError
from mechanize import Browser