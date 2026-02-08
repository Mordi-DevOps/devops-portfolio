"""Prints OS name,Logged user name, Current working directory"""
import os
import sys
import getpass

def os_info():
    print("OS Name: ", sys.platform, os.name)
    print("Logged user name: ", getpass.getuser())
    print("Current working directory: ", os.getcwd())
os_info()
