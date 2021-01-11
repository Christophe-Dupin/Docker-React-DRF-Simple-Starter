from rest_framework import serializers
from app.posts import models

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "body",
            "created_at",
            "updated_at",
        )
        model = models.Post
