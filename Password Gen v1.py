import requests
import sys 
import os
import json
import colorama
from colorama import Fore, Back, Style
from os import system
import ctypes
import time
import random

colorama.init()
ctypes.windll.kernel32.SetConsoleTitleW("CodeCyphers Password Gen")

print(Fore.LIGHTBLUE_EX +'''
CodeCypher Password Gen
=======================
''' + Fore.RESET)
#Character List
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'

number = input('number of passwords?')
number = int(number)

length = input('password length?')
length = int(length)

print('\nhere are your passwords:')

for pwd in range(number):
  password = ''
  for c in range(length):
    password += random.choice(chars)
  print(password)