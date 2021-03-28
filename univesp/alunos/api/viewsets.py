from rest_framework import viewsets
from alunos.api import serializers
from alunos import models

class AlunoViewSet(viewsets.ModelViewSet):
	serializer_class = serializers.AlunoSerializer
	queryset = models.Aluno.objects.all()
	