import controller.activityController as Activity
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def bootstrap():
    Activity.init()

if __name__ == '__main__':
    bootstrap()