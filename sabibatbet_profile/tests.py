from django.test import TestCase

# Create your tests here.
class sabibatbetProfileUnitTest(TestCase):
	def test_sabibatbet_profile_url_is_exist(self):
		response = Client().get('/sabibatbet_profile/')
		self.assertEqual(response.status_code, 200)

	def test_lab7_using_index_func(self):
		found = resolve('/sabibatbet_profile/')
		self.assertEqual(found.func, index)
