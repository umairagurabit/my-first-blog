from django.urls import resolve
from django.test import TestCase
from blog.views import post_list

# Create your tests here.
class HomePageTest(TestCase):

    def test_root_url_resolves_to_post_list_view(self):
        found = resolve('/')
        self.assertEqual(found.func, post_list)

    def test_add_new_cv_data(self):
        request = HttpRequest()
        response = post_list(request)
        html = response.content.decode('utf8')
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Minchangs blog</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
