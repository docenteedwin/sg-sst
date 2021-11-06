# Generated by Django 3.2.8 on 2021-11-06 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aliado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('nit', models.CharField(max_length=255)),
                ('arl', models.CharField(max_length=255)),
                ('pago_seguridad_social', models.CharField(max_length=255)),
                ('seguridad_producto', models.CharField(max_length=255)),
                ('cumplimiento_arl', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Aliado',
                'verbose_name_plural': 'Aliados',
            },
        ),
        migrations.CreateModel(
            name='documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('uploadedFile', models.FileField(upload_to='media/')),
                ('dateTimeOfUpload', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=255)),
                ('nit', models.CharField(max_length=255)),
                ('georreferencia', models.CharField(max_length=255)),
                ('actividad_economica', models.CharField(max_length=255)),
                ('nivel_riesgo', models.CharField(max_length=255)),
                ('cant_trabajadores', models.CharField(max_length=255)),
                ('naturaleza_juridica', models.CharField(max_length=255)),
                ('telefono_contacto', models.CharField(max_length=255)),
                ('email_contacto', models.CharField(max_length=255)),
                ('tipo_empresa', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='permissions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Permission',
                'verbose_name_plural': 'Permissions',
            },
        ),
        migrations.CreateModel(
            name='permissions_role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_permission', models.IntegerField()),
                ('id_rol', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Permission_role',
                'verbose_name_plural': 'Permissions_role',
            },
        ),
        migrations.CreateModel(
            name='Politicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=100)),
                ('nit', models.CharField(max_length=20)),
                ('compromisos', models.TextField()),
                ('requisitos_legales', models.TextField()),
                ('objetivos', models.TextField()),
                ('comentarios', models.TextField()),
                ('firma', models.CharField(max_length=30)),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Politica',
                'verbose_name_plural': 'Politicas',
            },
        ),
        migrations.CreateModel(
            name='rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('first_surname', models.CharField(max_length=255)),
                ('second_surname', models.CharField(max_length=255)),
                ('identity_number', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('cellphone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('admin_status', models.CharField(max_length=255)),
                ('activity_status', models.CharField(max_length=255)),
                ('id_rol', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
