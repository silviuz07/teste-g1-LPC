from django.db import models

class Pessoa(models.Model):
    nome = models.TextField(max_length=32)
    email = models.TextField(max_length=64)

    def __str__(self):
        return self.nome

class PessoaFisica(Pessoa):
    cpf = models.TextField(max_length=11)

    def __str__(self):
        return super(PessoaFisica, self).__str__()

class Evento(models.Model):
    nome = models.TextField(max_length=32)
    sigla = models.TextField(max_length=6)
    data_inicio = models.DateField()
    realizador = models.ManyToManyField(Pessoa)
    descricao = models.TextField(max_length=360)

    def __str__(self):
        return self.nome

class Ingresso(models.Model):
    descricao = models.TextField(max_length=128)
    valor = models.FloatField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

class Inscricao(models.Model):
    pessoa = models.ManyToManyField(Pessoa)
    evento = models.ManyToManyField(Evento)
    ingresso = models.ManyToManyField(Ingresso)

    def __str__(self):
        return self.pessoa




