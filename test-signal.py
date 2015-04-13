#!/usr/bin/env python

import time
import signal
import sys

def clean_shutdown(signum, frame):
    print "CLEANED!"
    sys.exit(0)

def run():

    signal.signal(signal.SIGALRM, clean_shutdown)
    signal.signal(signal.SIGHUP, clean_shutdown)
    signal.signal(signal.SIGINT, clean_shutdown)
    signal.signal(signal.SIGTERM, clean_shutdown)

    while True:
        print "Python sleeping"
        time.sleep(60)


if __name__ == "__main__":
    run()