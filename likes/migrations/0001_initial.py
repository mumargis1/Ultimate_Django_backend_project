<<<<<<< HEAD
# Generated by Django 3.2.4 on 2021-06-08 14:44
=======
# Generated by Django 4.2.2 on 2023-07-01 06:53
>>>>>>> a77aecced6d01cf351118df2ea482b17fbe03da9

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
<<<<<<< HEAD
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
=======
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
>>>>>>> a77aecced6d01cf351118df2ea482b17fbe03da9
    ]

    operations = [
        migrations.CreateModel(
            name='LikedItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
<<<<<<< HEAD
=======
                ('content_object', models.GenericIPAddressField()),
>>>>>>> a77aecced6d01cf351118df2ea482b17fbe03da9
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
