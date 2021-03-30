from django.test import TestCase

# Create your tests here.
class CountriesTests(TestCase):
    def test_country_text(self):
        client = client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter country code")