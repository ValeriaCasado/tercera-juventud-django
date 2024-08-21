from django.test import TestCase
from django.test import Client
import json

class TestEndpoints(TestCase):
    c = Client()

    def test_assert_get_home(self):
        
        response = self.c.get("/")
        assert response.status_code == 200
    
    def test_assert_get_info(self):
    
        response = self.c.get("/info")
        assert response.status_code == 200

    def test_assert_get_project_page(self):
    
        response = self.c.get("/proyectos")
        assert response.status_code == 200
