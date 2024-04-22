from django.db import models
from django.utils.translation import gettext_lazy as _


class Contact(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"Name: {self.name}"


class NamesMan(Contact):
    class Meta:
        verbose_name = _("Man")
        verbose_name_plural = _("Men")

    @property
    def gender(self):
        return 'male'


class NamesWoman(Contact):
    class Meta:
        verbose_name = _("Woman")
        verbose_name_plural = _("Women")

    @property
    def gender(self):
        return 'female'
