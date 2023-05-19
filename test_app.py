'''
In this file you will find different tests for the application.
Mainly the test's purpose is to check if the right html templates are used.
'''

import unittest
from flask import session
from flask_testing import TestCase
from app import app

class FlaskTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    def test_home(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_country_redirect(self):
        response = self.client.post('/land_weiterleitung', data=dict(land='schweiz'), follow_redirects=False)
        self.assertEqual(response.location, '/eingabe') 

    def test_speed_input(self):
        response = self.client.post('/eingabe', data=dict(gefahrene=120, erlaubte=100, wiederholung = 'nein', strassentyp = 'Autobahn', radar = 'mobil'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_speed_difference(self):
        with self.client:
            self.client.post('/eingabe', data=dict(gefahrene=120, erlaubte=100, wiederholung = 'nein', strassentyp = 'Autobahn', radar = 'mobil'), follow_redirects=True)
            self.assertEqual(session.get('result'), 12)

if __name__ == '__main__':
    unittest.main()