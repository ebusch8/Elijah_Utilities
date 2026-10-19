# Import
from datetime import datetime

def log(message, when=None):
  """Log a message with a timestamp.
  Args:
    message: Message to print.
    when: datetime of when the message occurred.
    Defaults to the present time.
  """
when = datetime.now() if when is None else when
print(‘%s: %s’ % (when, message))

def distance(x1,y1,x2,y2):
  pass
