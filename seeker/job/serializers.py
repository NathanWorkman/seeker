"""Serializers."""
from rest_framework import serializers

from seeker.job.models import Job


class JobSerializer(serializers.ModelSerializer):

    id = serializers.HyperlinkedRelatedField(
        view_name="job_detail", read_only=True
    )

    class Meta:
        """Endpoint fields."""

        model = Job
        fields = '__all__'
