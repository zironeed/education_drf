from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from lms.paginators import LmsPagination
from lms.serializers import CourseSerializer, LessonSerializer, CourseCountSerializer, PaymentSerializer, \
    SubscribeSerializer
from lms.models import Course, Lesson, Payment, Subscribe

from permissions import IsOwner, IsModerator, UserPermission


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated, UserPermission]
    pagination_class = LmsPagination

    def perform_create(self, serializer):
        new_class = serializer.save()
        new_class.owner = self.request.user
        new_class.save()


class LessonListAPIView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateAPIView(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = LmsPagination
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_class = serializer.save()
        new_class.owner = self.request.user
        new_class.save()


class LessonUpdateAPIView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonRetrieveAPIView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | IsModerator]


class LessonDestroyAPIView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class CourseCountListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCountSerializer


class PaymentListAPIView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['lesson', 'course', 'payment_type']
    ordering_fields = ['payment_date']


class PaymentCreateAPIView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentUpdateAPIView(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentRetrieveAPIView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentDestroyAPIView(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class SubscribeListView(ListAPIView):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    permission_classes = [IsOwner | IsModerator]


class SubscribeCreateView(CreateAPIView):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    permission_classes = [IsOwner | IsModerator]

    def perform_create(self, serializer):
        new_sub = serializer.save()
        new_sub.owner = self.request.user
        new_sub.save()


class SubscribeDestroyView(DestroyAPIView):
    serializer_class = SubscribeSerializer
    queryset = Subscribe.objects.all()
    permission_classes = [IsOwner | IsModerator]
