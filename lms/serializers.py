from rest_framework import serializers
from lms.models import Lesson, Course, Payment, Subscribe
from lms.my_validators import validator_url


class CourseCountSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()

    def get_lesson_count(self, instance):
        return instance.lesson.count()

    class Meta:
        model = Course
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(many=True, read_only=True)
    video_url = serializers.URLField(validators=[validator_url])
    description = serializers.CharField(validators=[validator_url])
    name = serializers.CharField(validators=[validator_url])

    class Meta:
        model = Lesson
        fields = '__all__'


class SubscribeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscribe
        fields = ('is_subscribed',)


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(many=True, read_only=True)
    payment = PaymentSerializer(many=True, read_only=True)
    # subscribe = SubscribeSerializer(read_only=True)
    subscribe = serializers.SerializerMethodField()

    description = serializers.CharField(validators=[validator_url])
    name = serializers.CharField(validators=[validator_url])

    def get_subscribe(self, obj):
        request = self.context.get('request')


    class Meta:
        model = Course
        fields = '__all__'
