from django.urls import path
from rest_framework.routers import DefaultRouter

from lms.apps import LmsConfig
from lms.views import CourseViewSet, LessonListAPIView, LessonCreateAPIView, LessonDestroyAPIView, \
    LessonUpdateAPIView, LessonRetrieveAPIView, CourseCountListAPIView, PaymentListAPIView, \
    PaymentRetrieveAPIView, PaymentCreateAPIView, PaymentUpdateAPIView, PaymentDestroyAPIView, \
    SubscribeListView, SubscribeCreateView, SubscribeDestroyView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lessons/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_get'),
    path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

    path('courses/count/', CourseCountListAPIView.as_view(), name='courses_count'),

    path('payment/create/', PaymentCreateAPIView.as_view(), name='lesson_create'),
    path('payments/', PaymentListAPIView.as_view(), name='lesson_list'),
    path('payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='lesson_update'),
    path('payment/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='lesson_get'),
    path('payment/delete/<int:pk>/', PaymentDestroyAPIView.as_view(), name='lesson_delete'),

    path('courses/subscribe/list/', SubscribeListView.as_view(), name='subscribe_list'),
    path('courses/subscribe/create/', SubscribeCreateView.as_view(), name='subscribe_create'),
    path('courses/subscribe/delete/<int:pk>/', SubscribeDestroyView.as_view(), name='subscribe_destroy'),
] + router.urls
