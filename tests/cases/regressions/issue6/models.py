# Regression data model for issue #6
from django.db import models


class Specimen(models.Model):
    # Field name made lowercase.
    aliquot_id = models.DecimalField(decimal_places=0, max_digits=16,
                                     db_column='ALIQUOT_ID',
                                     primary_key=True)

    class Meta:
        db_table = 'specimen'
        verbose_name = 'specimen'
        verbose_name_plural = 'specimens'


class Subject(models.Model):
    study_id = models.TextField(primary_key=True, db_column='study_id')

    class Meta:
        db_table = 'subject'
        verbose_name = 'subject'
        verbose_name_plural = 'subjects'


class Link(models.Model):
    aliquot_id = models.ForeignKey(Specimen, db_column='ALIQUOT_ID',
                                   primary_key=True)
    study_id = models.ForeignKey(Subject, db_column='study_id')

    class Meta:
        db_table = 'link'
