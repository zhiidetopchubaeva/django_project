from rest_framework import serializers

from Test1.models import Post
from Test2.models import Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        dict_['user'] = instance.user.username
        dict_['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return dict_

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['post']

    def to_representation(self, instance):
        dict_ = super().to_representation(instance)
        dict_['user'] = instance.user.username
        return dict_