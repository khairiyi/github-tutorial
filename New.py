__author__ = 'blackboyyi'


def squared(var):
  try:
    return int(var)**2
  except ValueError:
    print("Not a number")
  else:
    return var*len(var)

if __name__ == '__main__':
    squared("ds")

