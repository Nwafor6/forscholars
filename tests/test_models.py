from django.test import TestCase
from django.contrib.auth import get_user_model

class UserMangerTests(TestCase):
	def test_case_user(self):
		user=get_user_model()
		user=User.objects.create_user(email="name@gmail.com", password="foo")
		self.assertEqual(user.email, "name@gmail.com")
		self.assertTrue(user.is_active)
		self.assertFalse(user.is_staff)
		self.assertFalse(user.is_superuser)


		with self.assertRaises(TypeError):
			User.objects.create_user()
		with self.assertRaises(TypeError):
			User.objects.create_user(email="")
		with self.assertRaises(ValueError):
			User.objects.create_user(email="", password="foo")

	def test_create_superuser(self):
		user=get_user_model()
		adminUser=User.objects.create_user(email="super@gmail.com", password="123456")

		self.assertEqual(adminUser.email, "super@gmail.com")
		self.assertTrue(adminUser.is_active)
		self.assertTrue(adminUser.is_staff)
		self.assertTrue(adminUser.is_superuser)