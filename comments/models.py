from django.db import models
from django.utils.translation import gettext as _
from users.models import User
from rooms.models import Room

# Cambiar la importación de JSONField
# from django.contrib.postgres.fields import JSONField  # Eliminar esta línea
from django.db.models import JSONField  # Agregar esta línea

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = JSONField(blank=True, null=True)  # JSONField estándar de Django
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.content)  # Convertir a cadena si es necesario
