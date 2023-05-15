from django.db import models
from typing import List
from django.utils import timezone
from django.utils.translation import gettext_lazy

from src.domain.entities.account import UserEntity

class User(models.Model):
    name        = models.CharField(gettext_lazy('name'), max_length=100, blank=True)
    surname     = models.CharField(gettext_lazy('surname'), max_length=100, blank=True, null=True)
    username    = models.CharField(gettext_lazy('username'), max_length=20, blank=True)
    email       = models.EmailField(gettext_lazy('email'), db_index=True, unique=True)
    phone       = models.CharField(gettext_lazy('phone'),max_length=15, unique=True)
    password    = models.CharField(gettext_lazy('password'), max_length=64)
    is_active   = models.BooleanField(gettext_lazy('active'), default=True)
    last_login  = models.DateTimeField(gettext_lazy('last login'), default=timezone.now)
    date_joined = models.DateTimeField(gettext_lazy('date joined'), default=timezone.now)
    
    class Meta:
        verbose_name = gettext_lazy('user')
        verbose_name_plural = gettext_lazy('users')
        ordering = ('email',)
        
    def __str__(self) -> str:
        return str(self.map())
        
    def map(self, fields: List[str] = None) -> UserEntity:
        fields = fields or [str(field) for field in UserEntity.__dataclass_fields__]
        attrs = {field: getattr(self, field) for field in fields}
        return UserEntity(**attrs)