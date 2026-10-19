#!/usr/bin/env python3
# Docstring
"""
Elijah's Python Utilities Module. Contains functions that may be useful.
Can be used on microcontroller
"""
# Import
import sys
if sys.platform != "nspire":
  from datetime import datetime
import math

def log(message, when=None):
  """Log a message with a timestamp.

Args:
    message (str): Message to print.
    when (datetime, optional): Time the message occurred.
        Defaults to the current time.
"""
  when = datetime.now() if when is None else when
  print('%s: %s' % (when, message))

def distance(x1,y1,x2,y2):
  """Calculate the distance between two points.

Args:
    x1 (float): x-coordinate of the first point.
    y1 (float): y-coordinate of the first point.
    x2 (float): x-coordinate of the second point.
    y2 (float): y-coordinate of the second point.

Returns:
    float: Distance between the two points.
"""
  pass

def quad(a,b,c):
  """Solve a quadratic equation.

Args:
    a (float): Quadratic coefficient.
    b (float): Linear coefficient.
    c (float): Constant term.

Returns:
    tuple[float, float]: The two roots of the equation
        ax^2 + bx + c = 0.
"""
  pass
