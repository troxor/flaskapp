import os

# Defaults, overridden by os.environ()
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
THREADS_PER_PAGE = 2
CSRF_ENABLED = True

DEBUG = False

LISTEN = "127.0.0.1"
PORT = 3000

REDISHOST = "localhost"
REDISPORT = 6379

SITE_HOSTNAME = "example.com"
