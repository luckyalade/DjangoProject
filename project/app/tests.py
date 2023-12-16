from django.test import TestCase
from .models import SignUp
# Create your tests here.


class SignUpModelTest(TestCase):

  @classmethod
  def setUpTestData(cls):
    cls.signup = SignUp.objects.create(
        firstName="Lucky",
        lastName="Alade"
    )

  def test_field(self):
    self.assertIsInstance(self.signup.firstName, str)
    self.assertIsInstance(self.signup.lastName, str)
