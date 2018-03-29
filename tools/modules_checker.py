# coding: utf8
from sys import exit

def check_module(name):
    """Check if the given module is available to use.

    Keyword arguments:
    name -- the module name
    """
    try:
        __import__(name)
    except ImportError:
        exit("❌ Please install " + name + " first.")
    print("✅ " + name + " is installed.")

def check_modules(names):
    for name in names:
        check_module(name)
