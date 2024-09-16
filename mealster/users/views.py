from rest_framework.mixins import CreateModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet


class UserViewSet(CreateModelMixin,
                  UpdateModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):
    def create(self, request, *args, **kwargs):
        pass #create new user

    def update(self, request, *args, **kwargs):
        pass #update user info

    def destroy(self, request, *args, **kwargs):
        pass #delete user
