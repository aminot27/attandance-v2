from django.db import models

from master_serv.models.base_model_manager import BaseModelManager

status_types = (
    ("CREATED", "CREATED"),
    ("UPDATED", "UPDATED"),
    ("DELETED", "DELETED"),
    ("ACTIVE", "ACTIVE"),
    ("INACTIVE", "INACTIVE"),

)


class BaseModel(models.Model):
    created = models.DateTimeField('Created',
                                   auto_now_add=True,
                                   help_text='Date time on which the object was created.')
    modified = models.DateTimeField('Modified',
                                    auto_now=True,
                                    help_text='Date time on which the object was last modified.')
    status = models.CharField('Status', max_length=15, choices=status_types, help_text='Current register status',
                              default=status_types[0][0])
    objects = BaseModelManager()

    class Meta:
        """Meta option."""
        abstract = True
        # get_latest_by = 'created'
        # ordering = ['-created', '-modified']
