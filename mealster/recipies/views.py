from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet


class FavoriteRecipesView(ListModelMixin,
                          CreateModelMixin,
                          DestroyModelMixin,
                          GenericViewSet):
    def list(self, request, *args, **kwargs):
        pass #get all favorites

    def create(self, request, *args, **kwargs):
        pass #save as favorite

    def destroy(self, request, *args, **kwargs):
        pass #delete from favorites


class RandomRecipiesView(ListModelMixin,
                         GenericViewSet):
    def list(self, request, *args, **kwargs):
        pass #if no args -> get random recipie, else -> get list with chosen ingr


class BannedIngredientsView(ListModelMixin,
                            CreateModelMixin,
                            DestroyModelMixin,
                            GenericViewSet):
    def list(self, request, *args, **kwargs):
        pass #get all banned

    def create(self, request, *args, **kwargs):
        pass #add to banned

    def destroy(self, request, *args, **kwargs):
        pass #del from banned
