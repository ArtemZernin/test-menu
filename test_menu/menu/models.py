from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
    url = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ('url',)
