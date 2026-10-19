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
import cmath


def log(message, when=None):
  """Log a message with a timestamp.

Args:
    message (str): Message to print.
    when (datetime, optional): Time the message occurred.
        Defaults to the current time.
"""
  when = datetime.now() if when is None else when
  print('%s: %s' % (when, message))


def distance(x1, y1, x2, y2):
  """Calculate the distance between two points.

Args:
    x1 (float): x-coordinate of the first point.
    y1 (float): y-coordinate of the first point.
    x2 (float): x-coordinate of the second point.
    y2 (float): y-coordinate of the second point.

Returns:
    float: Distance between the two points.
"""
  # Use math.hypot for numerical stability
  return math.hypot(x2 - x1, y2 - y1)


def quad(a, b, c):
  """Solve a quadratic equation.

Args:
    a (float): Quadratic coefficient.
    b (float): Linear coefficient.
    c (float): Constant term.

Returns:
    tuple[complex, complex]: The two roots (may be real or complex) of the equation
        ax^2 + bx + c = 0.
"""
  if a == 0:
    # Linear equation bx + c = 0
    if b == 0:
      raise ValueError("Both a and b are zero — equation is not solvable or has infinite solutions")
    return (-c / b, -c / b)

  # discriminant
  d = b * b - 4 * a * c
  if d >= 0:
    sqrt_d = math.sqrt(d)
  else:
    sqrt_d = cmath.sqrt(d)

  root1 = (-b + sqrt_d) / (2 * a)
  root2 = (-b - sqrt_d) / (2 * a)
  return (root1, root2)
