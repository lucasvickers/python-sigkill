import time
import atexit

def clean_shutdown():
    print "Cleaning shutdown called."

def run():
    atexit.register(clean_shutdown)

    while True:
        print "Python sleeping"
        time.sleep(60)


if __name__ == "__main__":
    run()