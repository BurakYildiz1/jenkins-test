from flask import Flask
from flask_testing import TestCase

class MyTest(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app
    
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello Jenkins')
        
    def test_hello(self):
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')