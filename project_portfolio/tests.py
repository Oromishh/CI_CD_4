from django.test import TestCase


class TemplateTest(TestCase):
    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
    
    def test_blog_single(self):
        response = self.client.get('/blog-single')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog-single.html')
    
    def test_portfolio_details(self):
        response = self.client.get('/portfolio-details')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio-details.html')


