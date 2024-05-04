from rest_framework import serializers
from .models import JobCategory,JobPost

class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = '__all__'

class JobPostSerializer(serializers.ModelSerializer):
    job_category = serializers.PrimaryKeyRelatedField(queryset=JobCategory.objects.all())
    
    class Meta:
        model = JobPost
        fields = ['job_title', 'job_category']

    def validate_job_category(self, value):
        if not JobCategory.objects.filter(pk=value.pk).exists():
            raise serializers.ValidationError("Invalid category")
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        job_post = JobPost.objects.create(poster=user, **validated_data)
        return job_post
# ...............