from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        request = self.context["request"]
        validated_data["author"] = request.user
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ["id", "post", "author", "content", "created_at", "updated_at"]
        read_only_fields = ["author"]

    def create(self, validated_data):
        request = self.context["request"]
        validated_data["author"] = request.user
        validated_data["post"] = self.context["post"]
        return super().create(validated_data)