from rest_framework import serializers
from router_api.models import router_details


class RouterSerializer(serializers.ModelSerializer):
    class Meta:
        model = router_details
        fields = '__all__'
