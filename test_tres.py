import unittest
import json

# from tests.base_case import BaseTestClass

class UserClientTestCase():

    def test_index_create_user(self):
        response = self.client.post(
            '/users/',
            data=json.dumps(
                {
                    'email': 'fake@fake.com',
                    'password': 'fake123'
                }
            ),
            content_type='application/json',)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 201)
        self.assertTrue(data['success'])
    
    def test_index_unauthorized(self):
        res = self.client.get('/users/')
        self.assertEqual(401, res.status_code)

if __name__ == '__main__':
    unittest.main()