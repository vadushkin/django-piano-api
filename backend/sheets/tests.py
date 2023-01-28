from rest_framework.test import APITestCase


class TestSheets(APITestCase):
    sheets_url = "/api/v1/sheets/"
    register_url = "/users/register/"
    login_url = "/users/login/"

    def _prepare_for_tests(self):
        reg_user1 = {
            "name": "oak",
            "email": "oak@oak.com",
            "password": "oak",
        }

        reg_user2 = {
            "name": "oak2",
            "email": "oak2@oak.com",
            "password": "oak2",
        }

        log_user1 = {
            "email": "oak@oak.com",
            "password": "oak",
        }

        # Register
        self.client.post(
            self.register_url,
            data=reg_user1,
        )
        self.client.post(
            self.register_url,
            data=reg_user2,
        )

        # Login
        self.client.post(
            self.login_url,
            data=log_user1,
        )

    def test_crud(self):
        """Why I don't use 5 functions for this,
        because every function needs test data,
        and if we go 2 or 2 > times to populate the database with data,
        it will be error 400. If you know how to get it, would be helpful.

        To supplement:
        The tests do not check whether the first user can see messages from the second user
        If you know how to get it, would be helpful.
        """

        ################################################################################
        # Create #
        ################################################################################

        # preparing
        self._prepare_for_tests()

        # test files
        file1 = open("test_payloads/Bethoven_Bagatelle_25.pdf", "rb")
        file2 = open("test_payloads/Shopen_Frederik_Etud_op10_12.pdf", "rb")
        file3 = open("test_payloads/Rahmaninov_Sergeiy_Preludiya_op32_2.pdf", "rb")
        file4 = open("test_payloads/Never_Gonna_Give_You_Up.pdf", "rb")
        file5 = open("test_payloads/Griboedov_2_waltz.pdf", "rb")

        # test payloads
        test_payload1 = {
            "name": "Bagatelle 25",
            "file_pdf": file1,
            "description": "Bethoven",
            "user": 1,

        }
        test_payload2 = {
            "name": "Etud op10 12",
            "file_pdf": file2,
            "description": "Shopen Frederik",
            "user": 1,
        }
        test_payload3 = {
            "name": "Preludiya op32 2",
            "file_pdf": file3,
            "description": "Rahmaninov Sergeiy",
            "user": 2,
        }

        # response from server
        response = self.client.post(
            self.sheets_url,
            data=test_payload1,
            format="multipart",
        )
        # good/bad?
        self.assertEqual(response.status_code, 201)

        # response from server
        response = self.client.post(
            self.sheets_url,
            data=test_payload2,
            format="multipart",
        )
        # nice/cool?
        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            self.sheets_url,
            data=test_payload3,
            format="multipart",
        )
        self.assertEqual(response.status_code, 201)

        ################################################################################
        # Patch #
        ################################################################################

        test_update_data1 = {
            "name": "Fir",
        }

        test_update_data2 = {
            "name": "Spruce",
        }

        # response from server
        response = self.client.patch(
            self.sheets_url + "1/",
            data=test_update_data1,
        )
        # check good error
        self.assertEqual(response.status_code, 200)
        # check that name was changed
        self.assertEqual(response.data.get("name"), "Fir")
        # check that user is not changed
        self.assertEqual(response.data.get("description"), "Bethoven")

        # response from server
        response = self.client.patch(
            self.sheets_url + "2/",
            data=test_update_data2,
        )
        # check good error
        self.assertEqual(response.status_code, 200)
        # check that name was changed
        self.assertEqual(response.data.get("name"), "Spruce")
        # check that user is not changed
        self.assertEqual(response.data.get("description"), "Shopen Frederik")

        ################################################################################
        # Put #
        ################################################################################

        test_update_data1 = {
            "name": "Herringbone",
            "file_pdf": file4,
            "user": 1,
            "description": "Cool",
        }

        test_update_data2 = {
            "name": "Christmas Tree",
            "file_pdf": file5,
            "user": 2,
            "description": "Nice",
        }

        # response from server
        response = self.client.put(
            self.sheets_url + "1/",
            data=test_update_data1,
        )
        # check good error
        self.assertEqual(response.status_code, 200)
        # check that name and user were changed
        self.assertEqual(response.data.get("name"), "Herringbone")
        self.assertEqual(response.data.get("description"), "Cool")

        # response from server
        response = self.client.put(
            self.sheets_url + "2/",
            data=test_update_data2,
        )
        # check good error
        self.assertEqual(response.status_code, 200)
        # check that name and user were changed
        self.assertEqual(response.data.get("name"), "Christmas Tree")
        self.assertEqual(response.data.get("description"), "Nice")

        ################################################################################
        # Get #
        ################################################################################

        # response from server
        response = self.client.get(
            self.sheets_url,
        )
        # check good error
        self.assertEqual(response.status_code, 200)

        # check that we got data
        self.assertTrue(len(response.data) > 0)

        # response from server
        response = self.client.get(
            self.sheets_url + "1/",
        )
        # check bad error
        self.assertEqual(response.status_code, 200)
        # check that we got the first one
        self.assertEqual(response.data.get("name"), "Herringbone")

        ################################################################################
        # Delete #
        ################################################################################

        # response from server
        response = self.client.delete(
            self.sheets_url + "1/",
        )
        # alright?
        self.assertEqual(response.status_code, 204)

        # response from server
        response = self.client.delete(
            self.sheets_url + "2/",
        )
        # nice.
        self.assertEqual(response.status_code, 204)


class TestCategories(APITestCase):
    categories_url = "/api/v1/categories/"

    register_url = "/users/register/"
    login_url = "/users/login/"

    def _prepare_for_tests(self):
        reg_user1 = {
            "name": "fir",
            "email": "fir@fir.com",
            "password": "fir",
        }

        reg_user2 = {
            "name": "fir2",
            "email": "fir2@fir.com",
            "password": "fir2",
        }

        log_user1 = {
            "email": "fir@fir.com",
            "password": "fir",
        }

        # Register
        self.client.post(
            self.register_url,
            data=reg_user1,
        )
        self.client.post(
            self.register_url,
            data=reg_user2,
        )

        # Login
        self.client.post(
            self.login_url,
            data=log_user1,
        )

    def test_crud(self):
        ################################################################################
        # Create #
        ################################################################################

        # preparing
        self._prepare_for_tests()

        # test payloads
        test_payload1 = {
            "name": "Bagatelle 25",
            "slug": "bagatelle-25",
            "user": 1,
        }
        test_payload2 = {
            "name": "Etud op10 12",
            "slug": "etud-op10-12",
            "user": 1,
        }
        test_payload3 = {
            "name": "Preludiya op32 2",
            "slug": "preludiya-op32-2",
            "user": 2,
        }

        # response from server
        response = self.client.post(
            self.categories_url,
            data=test_payload1,
            format="multipart",
        )
        # bad/good?
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get("name"), "Bagatelle 25")

        # response from server
        response = self.client.post(
            self.categories_url,
            data=test_payload2,
            format="multipart",
        )
        # nice/cool/awesome?
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get("name"), "Etud op10 12")

        response = self.client.post(
            self.categories_url,
            data=test_payload3,
            format="multipart",
        )
        # very nice
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data.get("name"), "Preludiya op32 2")

        ################################################################################
        # Patch #
        ################################################################################

        test_update_data1 = {
            "name": "Spruce",
        }

        test_update_data2 = {
            "name": "Fir",
        }

        # response from server
        response = self.client.patch(
            self.categories_url + "1/",
            data=test_update_data1,
        )
        # check good error
        self.assertEqual(response.status_code, 200)
        # check that name was changed
        self.assertEqual(response.data.get("name"), "Spruce")
        # check that user is not changed
        self.assertEqual(response.data.get("slug"), "bagatelle-25")

        # response from server
        response = self.client.patch(
            self.categories_url + "2/",
            data=test_update_data2,
        )
        # check good error
        self.assertEqual(response.status_code, 200)
        # check that name was changed
        self.assertEqual(response.data.get("name"), "Fir")
        # check that user is not changed
        self.assertEqual(response.data.get("slug"), "etud-op10-12")

        ################################################################################
        # Put #
        ################################################################################

        test_update_data1 = {
            "name": "Herringbone",
            "slug": "cool",
            "user": 1,
        }
        test_update_data2 = {
            "name": "Christmas Tree",
            "slug": "nice",
            "user": 1,
        }

        # response from server
        response = self.client.put(
            self.categories_url + "1/",
            data=test_update_data1,
        )

        # check good error
        self.assertEqual(response.status_code, 200)
        # check that name and user were changed
        self.assertEqual(response.data.get("name"), "Herringbone")
        self.assertEqual(response.data.get("slug"), "cool")

        # response from server
        response = self.client.put(
            self.categories_url + "2/",
            data=test_update_data2,
        )
        # check good error
        self.assertEqual(response.status_code, 200)
        # check that name and user were changed
        self.assertEqual(response.data.get("name"), "Christmas Tree")
        self.assertEqual(response.data.get("slug"), "nice")

        ################################################################################
        # Get #
        ################################################################################

        # response from server
        response = self.client.get(
            self.categories_url,
        )
        # check good error
        self.assertEqual(response.status_code, 200)

        # check that we got data
        self.assertTrue(len(response.data) > 0)

        # response
        response = self.client.get(
            self.categories_url + "2/",
        )
        # check bad error
        self.assertEqual(response.status_code, 200)
        # check that we got the Herringbone
        self.assertEqual(response.data.get("name"), "Christmas Tree")

        ################################################################################
        # Delete #
        ################################################################################

        # response from server
        response = self.client.delete(
            self.categories_url + "1/",
        )
        # alright?
        self.assertEqual(response.status_code, 204)

        # response from server
        response = self.client.delete(
            self.categories_url + "2/",
        )
        # nice.
        self.assertEqual(response.status_code, 204)


class TestTags(APITestCase):
    tags_url = "/api/v1/tags/"

    register_url = "/users/register/"
    login_url = "/users/login/"

    def _prepare_for_tests(self):
        reg_user1 = {
            "name": "pine",
            "email": "pine@pine.com",
            "password": "pine",
        }

        reg_user2 = {
            "name": "pine2",
            "email": "pine2@pine.com",
            "password": "pine2",
        }

        log_user1 = {
            "email": "pine@pine.com",
            "password": "pine",
        }

        # Register
        self.client.post(
            self.register_url,
            data=reg_user1,
        )
        self.client.post(
            self.register_url,
            data=reg_user2,
        )

        # Login
        self.client.post(
            self.login_url,
            data=log_user1,
        )

    def test_crud(self):
        ################################################################################
        # Create #
        ################################################################################

        # preparing
        self._prepare_for_tests()


class TestAuthors(APITestCase):
    authors_url = "/api/v1/authors/"

    register_url = "/users/register/"
    login_url = "/users/login/"

    def _prepare_for_tests(self):
        reg_user1 = {
            "name": "maple",
            "email": "maple@maple.com",
            "password": "maple",
        }

        reg_user2 = {
            "name": "maple2",
            "email": "maple2@maple.com",
            "password": "maple2",
        }

        log_user1 = {
            "email": "maple@maple.com",
            "password": "maple",
        }

        # Register
        self.client.post(
            self.register_url,
            data=reg_user1,
        )
        self.client.post(
            self.register_url,
            data=reg_user2,
        )

        # Login
        self.client.post(
            self.login_url,
            data=log_user1,
        )

    def test_crud(self):
        ################################################################################
        # Create #
        ################################################################################

        # preparing
        self._prepare_for_tests()
