from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)  # soft_delete 
    deleted_at = models.DateTimeField(null=True, blank=True)
    class Meta:
        abstract = True   # MODELO NÃO SERÁ CRIADO NO BANCO DE DADOS 



class Client(BaseModel):
    name = models.CharField(max_length=255, db_index=True) # db_index=True -> melhora a consulta no bando de dados
    email = models.EmailField(unique=True) 
    birth_date = models.DateField()

    objects = models.Manager()

    # "deleta" a instância
    def delete(self):
        self.is_deleted = True
        self.save()

    # restaura a instância
    def restore(self):
        self.is_deleted = False
        self.save()


class ClientQuerySet(models.QuerySet):
    def activate(self):
        return self.filter(is_deleted=False)
    

class ClientManager(models.Manager):
    def get_queryset(self):
        return ClientQuerySet(self.model, using=self._db)
    
    def activate(self):
        return self.get_queryset().activate()