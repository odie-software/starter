from factory.declarations import LazyAttribute, PostGenerationMethodCall, SubFactory
from factory.django import DjangoModelFactory
from factory.faker import Faker
from faker import Faker as realFaker

from ..models import CustomUser, RoleChoices

fake = realFaker()


class CustomUserFactory(DjangoModelFactory):
    class Meta:  # pyright: ignore [reportIncompatibleVariableOverride]
        model = CustomUser

    role = RoleChoices.USER
    email = Faker("email")
    username = Faker("user_name")
    password = PostGenerationMethodCall("set_password", "realpassword")

