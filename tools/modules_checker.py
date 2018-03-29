# coding: utf8
from sys import exit

def check_module(name):
    """Check if the given module is available to use.

    :param str name: The module name to check
    """
    try:
        __import__(name)
    except ImportError:
        exit("❌ Please install " + name + " first.")
    print("✅ " + name + " is installed.")

def check_modules(names):
    """Check if all of the given modules are available.

    :param list names: The list of module names
    """
    for name in names:
        check_module(name)
