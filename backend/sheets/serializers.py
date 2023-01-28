from rest_framework import serializers

from .models import Author, Category, Sheet, Tag
# from .services import get_current_user


class SheetSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Sheet
        exclude = ("photo", )

    # def save(self, **kwargs):
    #     user = None
    #     request = self.context.get("request")
    #
    #     print(get_current_user(request))
    #     if get_current_user(request):
    #         user = get_current_user(request)


class AuthorSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Author
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Tag
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = "__all__"
