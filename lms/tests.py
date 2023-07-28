from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from config.settings import AUTH_USER_MODEL

from lms.models import Lesson, Course, Subscribe
from users.models import User


class LmsTestCase(APITestCase):

    def setUp(self):
        self.user = User(email='test@mail.ru')
        self.user.set_password('12345')
        self.user.save()

        user_data = {
            'email': 'test@mail.ru',
            'password': '12345'
        }

        response = self.client.post(
            '/users/api/token/',
            user_data
        )

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

        self.lesson = Lesson.objects.create(
            name='TestLesson',
            description='TestLesson',
            video_url='https://www.youtube.com/watch?v=4xDzrJKXOOY'
        )

        self.course = Course.objects.create(
            name='TestCourse',
            description='TestCourse'
        )

    def test_create_lesson(self):
        data = {
            'name': 'TestCreate',
            'description': 'TestCreate',
            "video_url": "https://www.youtube.com/watch?v=4xDzrJKXOOY"
        }

        response = self.client.post(
            "/lms/lessons/create/",
            data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(Lesson.objects.filter(name='TestCreate').exists())

    def test_list_lesson(self):
        response = self.client.get('/lms/lessons/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_validate_lesson(self):
        data = {
            'name': 'TestVal',
            'description': 'TestVal',
            'video_url': 'https://vk.com'
        }

        response = self.client.post('/lms/lessons/create/', data)

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_delete_lesson(self):
        obj = Lesson.objects.create(
            name='TestLesson1',
            description='TestLesson1',
            video_url='https://www.youtube.com/watch?v=4xDzrJKXOOY1'
        )

        url = reverse('lms:lesson_delete', kwargs={'pk': obj.id})

        response = self.client.delete(url)

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

    def test_create_subscribe(self):
        data = {
            'id': 1,
            'is_subscribed': False,
            "user": self.user.pk,
            "course": self.course.pk
        }

        response = self.client.post('/lms/courses/subscribe/create/', data)
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertTrue(Subscribe.objects.all().exists())

    def test_list_subscribe(self):
        response = self.client.get('/lms/courses/subscribe/list/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
