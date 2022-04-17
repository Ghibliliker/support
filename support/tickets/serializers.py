from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from tickets.models import Comment, Ticket
from users.serializers import CustomUserSerializer


class TicketCreateSerializer(serializers.ModelSerializer):

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
    comments = serializers.SerializerMethodField(read_only=True)
    author = CustomUserSerializer()

    class Meta:
        model = Ticket
        fields = '__all__'

    def get_comments(self, obj):
        queryset = Comment.objects.filter(ticket=obj)
        return CommentListSerializer(queryset, many=True).data


class TicketStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ('status',)


class CommentCreateSerializer(serializers.ModelSerializer):

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

    author = CustomUserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
