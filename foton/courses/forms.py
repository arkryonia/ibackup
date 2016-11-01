# -*- coding: utf-8 -*-
# @Author: Reysh Tech
# @Date:   2016-09-04 09:35:25
# @Last Modified by:   pyoda
# @Last Modified time: 2016-09-04 11:30:44

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django import forms

from django.forms.models import inlineformset_factory


class OrderField(models.PositiveIntegerField):

	def __init__(self, for_fields = None, *args, **kwargs):
		self.for_fields = for_fields
		super(OrderField, self).__init__(*args, **kwargs)

	def pre_save(self, model_instance, add):
		if getattr(model_instance, self.attname) is None:
			try:
				qs = self.model.objects.all()
				if self.for_fields:
					query = {field: getattr(model_instance,  field) for field in self.for_fields}
					qs = qs.filter(**query)
				last_item = qs.latest(self.attname)
				value = last_item.order + 1
			except ObjectDoesNotExist:
				value = 0
			setattr(model_instance, self.attname, value)
			return value
		else:
			return super(OrderField, self).pre_save(model_instance, add)