import uuid

from django.db import models


class DataFile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to='core/datafile/file')

    date_added = models.DateTimeField(auto_now_add=True, db_index=True)
    date_changed = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_added', )

    def __str__(self):
        return f'{self.id}'
