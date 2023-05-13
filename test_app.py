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

    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assert200(response)
        self.assert_template_used('land.html')

    def test_country_redirect(self):
        response = self.client.post('/land_weiterleitung', data={'land': 'schweiz'})
        self.assertRedirects(response, '/eingabe')

        response = self.client.post('/land_weiterleitung', data={'land': 'deutschland'})
        self.assert200(response)
        self.assert_template_used('countries/deutschland.html')

    def test_speed_input(self):
        response = self.client.get('/eingabe')
        self.assert200(response)
        self.assert_template_used('eingabe.html')

    def test_speed_difference(self):
        response = self.client.post('/kategorie', data={
            'gefahren': 100,
            'erlaubt': 80,
            'wiederholung': 'nein',
            'radar': 'laser',
            'strassentyp': 'Autobahn'
        })
        self.assertEqual(session.get('result'), 16)
        self.assert_template_used('ergebnisse/ergebnis_30er_zone.html')

        response = self.client.post('/kategorie', data={
            'gefahren': 80,
            'erlaubt': 80,
            'wiederholung': 'nein',
            'radar': 'laser',
            'strassentyp': '30er Zone'
        })
        self.assertEqual(session.get('result'), 0)
        self.assert_template_used('ergebnisse/keine_strafe.html')

if __name__ == '__main__':
    unittest.main()