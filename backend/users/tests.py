from http.cookies import SimpleCookie

from rest_framework.test import APITestCase


class TestAuthentication(APITestCase):
    login_url = "/api/login/"
    register_url = "/api/register/"
    logout_url = "/api/logout/"

    def test_register(self):
        # test case
        test_payload = {
            "name": "oak",
            "email": "oak@oak.com",
            "password": "oak",
        }
        # response from server
        response = self.client.post(
            self.register_url,
            data=test_payload,
        )

        # check if we get 200
        self.assertEqual(response.status_code, 200)
        # check if we get right name and email
        self.assertEqual(response.data.get("name"), "oak")
        self.assertEqual(response.data.get("email"), "oak@oak.com")
        # check if we get password in response
        self.assertIsNone(response.data.get("password"))

    def test_login(self):
        # create oak-account
        self.test_register()
        # test case
        test_payload = {
            "email": "oak@oak.com",
            "password": "oak",
        }
        # response from server
        response = self.client.post(
            self.login_url,
            data=test_payload,
        )

        # check if we get 200
        self.assertEqual(response.status_code, 200)
        # check if we get jwt token
        self.assertIsNotNone(response.data.get("jwt"))

    def test_logout_with_cookies(self):
        # set cookies
        self.client.cookies = SimpleCookie({"jwt": "123456789"})

        # response from server
        response = self.client.post(
            self.logout_url,
        )

        # check if we get 200
        self.assertEqual(response.status_code, 200)
        # check if message is success
        self.assertEqual(response.data.get("message"), "success")

    def test_logout_without_cookies(self):
        # response from server
        response = self.client.post(
            self.logout_url,
        )

        # check if we get 200
        self.assertEqual(response.status_code, 200)
        # check if message is not success
        self.assertEqual(response.data.get("message"), "Login to logout")
