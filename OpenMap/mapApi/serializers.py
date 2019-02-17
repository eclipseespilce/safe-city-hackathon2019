from rest_framework import serializers
from mapApi.models import *


class GroupRelatedField(serializers.RelatedField):
    def to_representation(self, obj):
        return str(obj.pk)

    def to_internal_value(self, str_id):
        return Group.objects.get(id=int(str_id))


class StatusRelatedField(serializers.RelatedField):
    def to_representation(self, obj):
        return str(obj.pk)

    def to_internal_value(self, str_id):
        return Status.objects.get(id=int(str_id))


class CategoryRelatedField(serializers.RelatedField):
    def to_representation(self, obj):
        return str(obj.pk)

    def to_internal_value(self, str_id):
        return Category.objects.get(id=int(str_id))


class IntToStringField(serializers.IntegerField):
    def to_representation(self, int_id):
        return str(int_id)

    def to_internal_value(self, str_id):
        return int(str_id)


class CategorySerializer(serializers.ModelSerializer):
    id = IntToStringField()
    class Meta:
        model = Group
        fields = ('id', 'name', 'description')
        read_only_fields = ('id',)


class StatusSerializer(serializers.ModelSerializer):
    id = IntToStringField()
    class Meta:
        model = Group
        fields = ('id', 'name', 'description')
        read_only_fields = ('id',)


class GroupSerializer(serializers.ModelSerializer):
    photoUrl = serializers.SerializerMethodField()
    id = IntToStringField()
    class Meta:
        model = Group
        fields = ('id', 'name', 'description', 'photoUrl')
        read_only_fields = ('id',)

    def get_photoUrl(self, group):
        request = self.context.get('request')
        photo_url = group.image.url
        return request.build_absolute_uri(photo_url)


class MapPointSerializer(serializers.ModelSerializer):
    id = IntToStringField(required=False)
    photoUrl = serializers.CharField(source='image_url', required=False)
    group = GroupRelatedField(queryset=Group.objects.all())
    category = CategoryRelatedField(queryset=Category.objects.all())
    status = StatusRelatedField(queryset=Status.objects.all())

    class Meta:
        model = MapPoint
        fields = ('id', 'description', 'photoUrl', 'group', 'category',
                  'status', 'latitude', 'longitude')
        read_only_fields = ('id',)
