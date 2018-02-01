# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class plugins(models.Model):
    ID = models.IntegerField(primary_key=True, auto_created=True)
    product = models.CharField(name="Product", max_length=50)
    bugid = models.CharField(name="BugID", max_length=20)
    rulestring = models.CharField(name="RuleString", max_length=200)
    rca = models.CharField(name="RCA", max_length=600)



