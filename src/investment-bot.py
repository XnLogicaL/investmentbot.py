import requests
import os
import time
import random
import math
import modules.exchange as exchange
import modules.fibonacci as fibonacci
import modules.approximate as approximate
import modules.binance as binance

class app:
    def BINANCE():
        return ".binance"
    def METAMASK():
        return ".metamask"

class bot:
    def get(firm: int, _index, app: app):
        if app == app.BINANCE():
            