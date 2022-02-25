from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone = models.CharField(max_length=255, verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return self.name


class ShoppingCenter(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name='Работник')

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговые точки'

    def __str__(self):
        return self.name


class Visit(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    shopping_center = models.ForeignKey(ShoppingCenter, on_delete=models.CASCADE, verbose_name='Торговая точка')
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        verbose_name = 'Посещение'
        verbose_name_plural = 'Посещении'

    def __str__(self):
        return self.shopping_center.name
