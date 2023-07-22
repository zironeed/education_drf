from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name='Course_name')
    preview = models.ImageField(upload_to='course_image', verbose_name='Course_preview', **NULLABLE)
    description = models.TextField(verbose_name='Course_description')
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='Course', on_delete=models.CASCADE, **NULLABLE,
                               related_name='lesson')
    name = models.CharField(max_length=150, verbose_name='Lesson_name')
    description = models.TextField(verbose_name='Lesson_description')
    preview = models.ImageField(upload_to='lesson_image', verbose_name='Lesson_preview', **NULLABLE)
    video_url = models.URLField(verbose_name='Lesson_video', **NULLABLE)
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'


class Payment(models.Model):

    class PaymentType(models.TextChoices):
        Cash = 'CASH'
        Transfer = 'TRANSFER'

    user = models.CharField(max_length=100, verbose_name='User_name')
    payment_date = models.DateField(verbose_name='Payment_date')
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, related_name='lesson',
                               verbose_name='Lesson', **NULLABLE)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name='course',
                               verbose_name='course', **NULLABLE)
    payment_sum = models.IntegerField(verbose_name='Payment_summ')
    payment_type = models.CharField(max_length=100, choices=PaymentType.choices)
