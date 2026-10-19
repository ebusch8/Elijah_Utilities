#!/usr/bin/env python3
# Docstring
"""
Elijah's Python Utilities Module. Contains functions that may be useful.
Can be used on microcontroller
"""
# Import

import sys
from datetime import datetime
import json
import math
import cmath
import os
import subprocess

# Functions

def bash(command):
  result = subprocess.run(command.split(), capture_output=True, text=True)
  if result.returncode != 0:
    print("Error %s:", result.stderr % result.returncode)
  print(result.stdout)
  return result.returncode

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

def read_json(path, default=None):
    """Read a JSON file and return its content, or default if missing/invalid."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return default

def write_json(path, data, indent=2):
    """Write a Python object to a JSON file."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent)
        f.write("\n")

def read_text(path, default=""):
    """Read a text file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return default

def write_text(path, text):
    """Write text to a file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def append_text(path, text):
    """Append text to a file."""
    with open(path, "a", encoding="utf-8") as f:
        f.write(text)

def file_exists(path):
    """Return True if a file exists."""
    return os.path.exists(path)

def ensure_dir(path):
    """Create a directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)
    return path

def list_files(directory):
    """Return a list of files in a directory."""
    return [os.path.join(directory, f) for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))]

