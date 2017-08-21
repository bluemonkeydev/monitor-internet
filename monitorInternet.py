#!/usr/bin/env python

# launch:
# python -u monitorInternet.py >> monitorInternet.log
# https://www.dropbox.com/s/lue7cpdj7bkr5l9/monitorInternet.log?dl=0
# https://www.dropbox.com/s/1sl6cj1fxbw2xns/monitorInternet.txt?dl=0

import datetime
import time
import socket


def isInternetAvail():
  domain = "yahoo.com"
  for x in range(1,3):
    try:
      host = socket.gethostbyname(domain)
      socket.create_connection((host, 80), 1)
      return True
    except:
      pass
  return False

#end isInternetAvail


def main():
  down = False
  while True:
    input_state = isInternetAvail()
    if input_state == False:
      # no internet; we're fucked!!!
      if (down == False):
        print( str(datetime.datetime.now()) + ": DOWN")
        down = True
    else:
      if down == True:
        # just came back up
        print( str(datetime.datetime.now()) + ": UP")
        down = False
      # end if
    #end if
    time.sleep(2)
  #end while

#end main


if __name__ == '__main__':
  main()
