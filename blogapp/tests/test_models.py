from django.test import TestCase
from django.urls import reverse

from blogapp.models import Article, Category
from django.contrib.auth.models import User


class ArticleModelTestCase(TestCase):
    def setUp(self) -> None:
        user = User.objects.create_superuser('admin123', '', 'admin123')
        category = Category.objects.create(name='test_category')
        self.post = Article.objects.create(
            title='test_title',
            body="test_body",
            category=category,
            author=user
        )

    def test_str_representation(self):
        self.assertEqual(self.post.__str__(), self.post.title)

    def test_auto_populate_modified_time(self):
        self.assertIsNotNone(self.post.modify_time)

        old_post_modify_time = self.post.modify_time
        self.post.body = '新的测试内容'
        self.post.save()
        self.post.refresh_from_db()
        self.assertTrue(self.post.modify_time > old_post_modify_time)

    def test_auto_populate_excerpt(self):
        self.assertIsNotNone(self.post.excerpt)
        self.assertTrue(0 < len(self.post.excerpt) <= 54)

    def test_get_absolute_url(self):
        expected_url = reverse('blogapp:detail', kwargs={'pk': self.post.pk})
        self.assertEqual(self.post.get_absolute_url(), expected_url)

    def test_increase_views(self):
        self.post.increase_views()
        self.post.refresh_from_db()
        self.assertEqual(self.post.views, 1)

        self.post.increase_views()
        self.post.refresh_from_db()
        self.assertEqual(self.post.views, 2)

