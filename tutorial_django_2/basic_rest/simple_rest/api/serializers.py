from rest_framework import serializers

from simple_rest.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    # Creating url method to ensure valid url is created
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = BlogPost
        fields = ["url", "pk", "user", "title", "content", "timestamp"]
        read_only_fields= ["user",]
        # Can get around field by setting default value in actual view logic

    # Can create specific validation techniques with restApi framework using validate
    def validate_title(self, value):
        qs = BlogPost.objects.filter(title__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError("The Title mst be unique")
        return value

    # Method to return actual url included in api using specific object information
    def get_url(self, obj):
        return obj.get_url()
