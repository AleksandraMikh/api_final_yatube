# TODO:  Напишите свой вариант

from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import (FollowSerializer,
                          PostSerializer,
                          CommentSerializer,
                          GroupSerializer)
from posts.models import Post, Group
from .permissions import IsOwnerOrReadOnly
from .exceptions import CustomValidationError


class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing posts.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsOwnerOrReadOnly,
                          IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing comments.
    """
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,
                          IsAuthenticatedOrReadOnly)
    pagination_class = None

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, pk=post_id)
        return post.comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        post=get_object_or_404(Post,
                                               pk=self.kwargs['post_id']))


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    pagination_class = None


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    # mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):

    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = None
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follows.all()

    def perform_create(self, serializer):
        serializer.is_valid()
        if serializer.validated_data['following'] == self.request.user:
            raise CustomValidationError(
                "Follow wasn't created because "
                "user can't be followed by himself.")
        serializer.save(user=self.request.user)
