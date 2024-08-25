from django.test import TestCase
from django.test import Client
import json

class TestEndpoints(TestCase):
    c = Client()

    def test_assert_get_home(self):
        
        response = self.c.get("/")
        assert response.status_code == 200
    
    def test_assert_get_endpoints(self):
    
        response = self.c.get("/informacion")
        assert response.status_code == 200
