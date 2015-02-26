from __future__ import absolute_import

from flaskapp.application import app

import unittest

class IndexTestCase(unittest.TestCase):

    def test_content(self):
        t = app.test_client(self)
        response = t.get('/')

if __name__ == '__main__':
    unittest.main()
