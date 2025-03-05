from django.db import models

class TeamMember(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    position = models.CharField(max_length=100, verbose_name="Должность")
    bio = models.TextField(verbose_name="Информация о себе")
    experience = models.TextField(verbose_name="Опыт работы")
    photo = models.ImageField(upload_to='team_photos/', verbose_name="Фото")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Член команды"
        verbose_name_plural = "Члены команды"
        

class ContactRequest(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="Полное имя")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.full_name} - {self.email}"

    class Meta:
        verbose_name = "Запрос на контакт"
        verbose_name_plural = "Запросы на контакт"