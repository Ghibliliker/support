from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from tickets.models import Comment, Ticket
from users.serializers import CustomUserSerializer


class TicketCreateSerializer(serializers.ModelSerializer):
    """Serializer for create or update tickets"""
    image = Base64ImageField(required=False)

    class Meta:
        model = Ticket
        fields = ('name', 'text', 'image')

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return TicketListSerializer(
            instance, context=context
        ).data


class TicketListSerializer(serializers.ModelSerializer):
    """Serializer for get tickets"""
    comments = serializers.SerializerMethodField(read_only=True)
    author = CustomUserSerializer()

    class Meta:
        model = Ticket
        fields = '__all__'

    def get_comments(self, obj):
        queryset = Comment.objects.filter(ticket=obj)
        return CommentListSerializer(queryset, many=True).data


class TicketStatusSerializer(serializers.ModelSerializer):
    """Serializer for update tickets status"""
    class Meta:
        model = Ticket
        fields = ('status',)


class CommentCreateSerializer(serializers.ModelSerializer):
    """Serializer for create or update comments"""
    image = Base64ImageField(required=False)

    class Meta:
        model = Comment
        fields = ('text', 'image')

    def to_representation(self, instance):
        request = self.context.get('request')
        context = {'request': request}
        return CommentListSerializer(
            instance, context=context
        ).data


class CommentListSerializer(serializers.ModelSerializer):
    """Serializer for get comments"""
    author = CustomUserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
