import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import post
from django.core.management.base import BaseCommand


def export_csv(modeladmin, request, queryset):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="notacerta.csv"'
	writer = csv.writer(response)
	writer.writerow(['email', 'nome', 'ip', 'data_hora', 'check_empresa', 'empresa', 'check_ramo', 'ramo'])
	leads = queryset.values_list('email', 'name', 'ip', 'created_date', 'check_empresa', 'empresa', 'check_ramo', 'ramo')
	for lead in leads:
		writer.writerow(lead)
	return response
export_csv.short_description = 'Export to CSV'

class leadadmin(admin.ModelAdmin):
	actions = [export_csv]

admin.site.register(post, leadadmin)