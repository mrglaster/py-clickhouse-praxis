import unittest
from modules.service.proxy import db_proxy

class proxy_tests(unittest.TestCase):
   #Checks the connection to the database
    def test_connect_database(self):
        # Initialization
        proxy = db_proxy()

        # Action
        proxy.create()

        # Checks
        print(proxy.error_text)
        assert proxy.error_text == ""
        assert proxy.is_error == False

    
