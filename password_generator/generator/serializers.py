from rest_framework.serializers import ModelSerializer

from generator.models import ListPasswords


class ListPasswordSerializer(ModelSerializer):

    class Meta:
        model = ListPasswords
        fields = "__all__"