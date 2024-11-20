from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.username", read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_by', 'created_on', 'updated_on']  #'__all__'
        read_only_fields = ['created_by']

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return Post.objects.create(**validated_data)