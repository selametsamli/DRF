from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from comment.models import Comment


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['created', ]  # bütün fieldleri kabul ediyoruz created hariç

    def validate(self, attrs):
        if (attrs["parent"]):
            if attrs['parent'].post != attrs['post']:
                raise serializers.ValidationError('Someting went wrong')
        return attrs