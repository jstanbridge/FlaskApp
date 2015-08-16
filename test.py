from app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that login page loads
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data)

    # Ensure that login page behaves correctly given correct data
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        self.assertIn(b'Login successful.', response.data)

    # Ensure that login page behaves correctly given correct data
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(username="wrong", password="wrong"), follow_redirects=True)
        self.assertIn(b'Invalid username or password', response.data)

    # Ensure logout works correctly
    def test_logout(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(username="admin", password="admin"), follow_redirects=True)
        response = tester.get('/logout', follow_redirects=True)
        self.assertIn(b'Logout successful.', response.data)

    # Ensure that main page needs login
    def test_login_required(self):
        tester = app.test_client(self)
        response = tester.get('/', follow_redirects=True)
        self.assertTrue(b'You need to login first.' in response.data)

if __name__ == '__main__':
    unittest.main()





