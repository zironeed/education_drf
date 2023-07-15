from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Course_name')
    preview = models.ImageField(upload_to='course_image', verbose_name='Course_preview', **NULLABLE)
    description = models.TextField(verbose_name='Course_description')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Lesson_name')
    description = models.TextField(verbose_name='Lesson_description')
    preview = models.ImageField(upload_to='lesson_image', verbose_name='Lesson_preview', **NULLABLE)
    video_url = models.URLField(verbose_name='Lesson_video', **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'
