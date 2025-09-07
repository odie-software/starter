from django.test import TestCase

from accounts.models import CustomUser, RoleChoices

from .factories import CustomUserFactory

class UserModelTests(TestCase):
    def setUp(self) -> None:
        self.obj: CustomUser = CustomUserFactory()

    def testDefaultRoleIsUser(self) -> None:
        self.assertEqual(self.obj.role, RoleChoices.USER)