from unittest import TestCase

from django.urls import resolve

# from accounts.views import (
#     AddressViewSet,
#     ClientViewSet,
#     ContactViewSet,
# )


# class TestUrls(TestCase):
#     def testClientResolves(self) -> None:
#         resolver = resolve("/api/v1/clients/")
#         self.assertEqual(resolver.func.cls, ClientViewSet)

#     def testContactResolves(self) -> None:
#         resolver = resolve("/api/v1/contacts/")
#         self.assertEqual(resolver.func.cls, ContactViewSet)

#     def testAddressResolves(self) -> None:
#         resolver = resolve("/api/v1/addresses/")
#         self.assertEqual(resolver.func.cls, AddressViewSet)
