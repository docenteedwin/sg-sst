from django.db import models

# Create your models here.

class users(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_surname = models.CharField(max_length=255)
    second_surname = models.CharField(max_length=255)
    identity_number = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    cellphone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    admin_status = models.CharField(max_length=255)
    activity_status = models.CharField(max_length=255)
    id_rol = models.CharField(max_length=255)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.user_name


class rol(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.name


class permissions(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Permission"
        verbose_name_plural = "Permissions"

    def __str__(self):
        return self.name


class permissions_role(models.Model):
    id_permission = models.IntegerField()
    id_rol = models.IntegerField()

    class Meta:
        verbose_name = "Permission_role"
        verbose_name_plural = "Permissions_role"

    def __str__(self):
        return self.id_rol

