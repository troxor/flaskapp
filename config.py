import os

# Defaults, overridden by os.environ()
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
THREADS_PER_PAGE = 2
CSRF_ENABLED = True

PORT = 3002

