'''
In this file you will find different tests for the application.
Mainly the test's purpose is to check if the right html templates are used.
'''

import unittest
from flask import session
from flask_testing import TestCase
from app import app
from calculations import speed_difference, penalty_30er_zone, penalty_innerorts, penalty_ausserorts, penalty_autobahn

class FlaskTestCase(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        return app

    # Checks whether the home page is displayed
    def test_home(self):
        response = self.client.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Checks whether the input page is displayed when country selection = Switzerland
    def test_country_redirect(self):
        response = self.client.post('/land_weiterleitung', data=dict(land='schweiz'), follow_redirects=False)
        self.assertEqual(response.location, '/eingabe') 

    # Checks whether the values are correctly stored in the session
    def test_speed_input(self):
        response = self.client.post('/kategorie', data=dict(gefahren=120, erlaubt=100, wiederholung = 'nein', strassentyp = 'Autobahn', radar = 'mobil'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # Checks different calculations in the calculations.py file
    def test_calculations(self):
        self.assertEqual(speed_difference(70, 60, 'laser'), 7)
        self.assertEqual(penalty_30er_zone(5), ('keine weitere Strafe', 40))
        self.assertEqual(penalty_innerorts(10), ('keine weitere Strafe', 120))
        self.assertEqual(penalty_ausserorts(15), ('keine weitere Strafe', 160))
        self.assertEqual(penalty_autobahn(20), ('keine weitere Strafe', 180))

    # Tests the 'category' route with cookies and checks if the correct speed is calculated
    def test_kategorie(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess['gefahrene'] = 80
                sess['erlaubte'] = 70
                sess['wiederholung'] = 'nein'
                sess['strassentyp'] = 'Autobahn'
            response = self.client.post('/kategorie', data={'gefahren': 80, 'erlaubt': 70, 'wiederholung': 'nein', 'strassentyp': 'Autobahn', 'radar': 'laser'})
            self.assertIn('result', session)
            self.assertEqual(session['result'], 7)

    # another speed difference test
    def test_speed_difference(self):
        with self.client:
            self.client.post('/kategorie', data=dict(gefahren=120, erlaubt=100, wiederholung = 'nein', strassentyp = 'Autobahn', radar = 'mobil'), follow_redirects=True)
            self.assertEqual(session.get('result'), 12)

    
if __name__ == '__main__':
    unittest.main()