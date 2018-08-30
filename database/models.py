from django.db import models
from django.utils import timezone


class Recourse(models.Model):
    created_date = models.DateTimeField(
            default=timezone.now)
    operator = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField(null=True)
    STATUS = (
        ('new', 'Новое обращение'),
        ('inwork', 'В работе'),
        ('done', 'Выполнено'),
        ('refused', 'Отказано'),
    )
    status = models.CharField(max_length=200, choices=STATUS)
    text = models.TextField()
    comment = models.TextField(blank=True)

    def publish(self):
        self.created_date = timezone.now()
        self.save()
