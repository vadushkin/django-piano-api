from rest_framework import serializers

from .models import Sheet


class SheetSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Sheet
        exclude = ("photo",)
