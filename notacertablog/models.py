from django.db import models
from django.utils import timezone

STATE_CHOICES = (
	('AC', 'Acre'),
	('AL', 'Alagoas'),
	('AP', 'Macapá'),
	('AM', 'Amazonas'),
	('BA', 'Bahia'),
	('CE', 'Ceará'),
	('DF', 'Distrito Federal'),
	('ES', 'Espírito Santo'),
	('GO', 'Goiás'),
	('MA', 'Maranhão'),
	('MT', 'Mato Grosso'),
	('MS', 'Mato Grosso do Sul'),
	('MG', 'Minas Gerais'),
	('PA', 'Pará'),
	('PB', 'Paraíba'),
	('PR', 'Paraná'),
	('PE', 'Pernambuco'),
	('PI', 'Piauí'),
	('RJ', 'Rio de Janeiro'),
	('RS', 'Rio Grande do Sul'),
	('RO', 'Rondônia'),
	('RR', 'Roraima'),
	('SC', 'Santa Catarina'),
	('SP', 'São Paulo'),
	('SE', 'Sergipe'),
	('TO', 'Tocantins'),
)

CHECK_CHOICES = (
	('s', 'Sim'),
	('n', 'Não'),
)

class post(models.Model):
	check_empresa = models.CharField(max_length=3, null=True, choices=CHECK_CHOICES, default=CHECK_CHOICES[0][0])
	empresa = models.CharField(max_length=50, blank=True, null=True)
	check_ramo = models.CharField(max_length=3, null=True, choices=CHECK_CHOICES, default=CHECK_CHOICES[0][0])
	ramo = models.CharField(max_length=50, blank=True, null=True)
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=200)
	cidade = models.CharField(max_length=50, default='')
	estado = models.CharField(max_length=50, choices=STATE_CHOICES)
	ip = models.CharField(max_length=15)
	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.created_date = timezone.now()
		self.save()

	def __str__(self):
		return self.name