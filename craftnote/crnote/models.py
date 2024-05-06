from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    #Заголовок.Максимальная длина заголовка
    Заголовок = models.CharField(max_length=100)

    #Описание. Атрибут задает необязательное поле
    Описание = models.TextField(blank=True)

    #Дата и время создания записи. Атрибут не позволит менять дату вручную
    Дата_создания = models.DateTimeField(auto_now_add=True)

    #Дата и время выполненной задачи
    Дата_выполнения = models.DateTimeField(null=True, blank=True)

    #Галочка о важной задачи
    Важно = models.BooleanField(default=False)

    #Привязка задачи к пользователю. ВАЖНО!
    Пользователь = models.ForeignKey(User, on_delete=models.CASCADE)

    #Отобразение заголовка на странице
    def __str__(self):
        return self.Заголовок