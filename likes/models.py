<<<<<<< HEAD
from django.conf import settings
from django.db import models
=======
from django.db import models
from django.contrib.auth.models import User
>>>>>>> a77aecced6d01cf351118df2ea482b17fbe03da9
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class LikedItem(models.Model):
<<<<<<< HEAD
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
=======
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = models.GenericIPAddressField()
>>>>>>> a77aecced6d01cf351118df2ea482b17fbe03da9
