from rest_framework import serializers

from .models import Channel, ChannelCategory


class ChannelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Channel
		fields = ('name', 'uuid')


class ChannelDetailSerializer(serializers.ModelSerializer):
	categories_tree = serializers.ReadOnlyField()

	class Meta:
		model = Channel
		fields = ('name', 'uuid', 'categories_tree')


class ChannelCategorySerializer(serializers.ModelSerializer):
	get_parent = serializers.ReadOnlyField()

	class Meta:
		model = ChannelCategory
		fields = ('name', 'uuid', 'get_parent', 'channel')