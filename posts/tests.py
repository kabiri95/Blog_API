from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@email.com',
            password='secret',
        )
        cls.post = Post.objects.create(
            title='A good title',
            author=cls.user,
            body='Nice body content',
        )
    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.title, 'A good title')
        self.assertEqual(self.post.body, 'Nice body content')
        self.assertEqual(str(self.post), 'A good title')