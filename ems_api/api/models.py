from django.db import models
from ems_api import settings


class User(models.Model):
    gender_choices = (
        (0, 'male'),
        (1, 'female'),
    )

    username = models.CharField(max_length=20)
    real_name = models.CharField(max_length=10)
    password = models.CharField(max_length=32)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    status = models.BooleanField(default=False)
    register_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bz_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Employee(models.Model):
    emp_name = models.CharField(max_length=10)
    age = models.SmallIntegerField()
    img = models.ImageField(upload_to='pic', default='pic/1.jpg')
    salary = models.DecimalField(decimal_places=2, max_digits=8)

    @property
    def img_url(self):
        return f'http://127.0.0.1:8000/{settings.MEDIA_URL}{self.img}'

    class Meta:
        db_table = 'bz_employee'
        verbose_name = '员工'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.emp_name
