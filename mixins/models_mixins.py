import uuid

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.safestring import mark_safe


class PKMixin(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          help_text="Unique ID",
                          editable=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Description(models.Model):
    description = models.CharField(max_length=255,
                                   default='Description',
                                   help_text='Description')

    class Meta:
        abstract = True


class Image(models.Model):
    image = models.ImageField(upload_to='Images', default='default.jpg')

    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))
        return ""

    class Meta:
        abstract = True


class UserModel(models.Model):
    user = models.ForeignKey(get_user_model(),
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True)

    class Meta:
        abstract = True
# Да, я знаю что смысла в этом мало.
# Но блин, дай поигратся, я настоящего множественного наследования 12 лет не видел )))))))
