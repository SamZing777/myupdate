import re
import datetime
import calendar

from django.contrib import admin
from django.utils import timezone

from .models import Update


@admin.register(Update)
class UpdateAdmin(admin.ModelAdmin):
	date_hierarchy = 'date_posted'
	date_hierarchy_drilldown = False
	list_display = ['informant', 'topic', 'matter', 'date_posted']


	def get_date_hierarchy_drilldown(self, year_lookup, month_lookup):
		"""Drill-down only on past dates."""

		today = timezone.now().date()

		if year_lookup is None and month_lookup is None:
		# Previous and Current year

			return (
			datetime.date(y, 1, 1)
			for y in range(today.year - 1, today.year + 1)
		)

		elif year_lookup is not None and month_lookup is None:
		# Past months of selected year till current month.

			this_month = today.replace(day=1)
			return (
			month for month in (
			datetime.date(int(year_lookup), month, 1)
			for month in range(1, 13)
			) 
				if month <= this_month
			)

		elif year_lookup is not None and month_lookup is not None:
			# Past days of selected month till current day.

			days_in_month = calendar.monthrange(year_lookup, month_lookup)[1]
			return (
			day for day in (
			datetime.date(year_lookup, month_lookup, i + 1)
			for i in range(days_in_month)
			) 
				if day <= today
	)

