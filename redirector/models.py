from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator
from hashids import Hashids
from django.conf import settings
from encrypted_model_fields.fields import EncryptedCharField

hashids = Hashids(salt=settings.SALT_KEY, min_length=8)

class UrlShrinked(models.Model):
    url=EncryptedCharField(validators=[URLValidator()], max_length=200)
    shrinked_code=models.CharField(max_length=30,unique=True,editable=False)

    def publish(self):
        self.created_date = timezone.now()
        self.shrinked_code = hashids.encode(self.id)
        self.save()

    def __str__(self):
        return self.shrinked_code
