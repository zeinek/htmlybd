from django.db import models

# Create your models here.
class Raza(models.Model):
    idRaza = models.AutoField(primary_key=True,verbose_name="Código de la Raza")
    nombre = models.CharField(max_length=30, verbose_name="Nombre de la Raza",null=True, blank=False)

    def __str__(self):
        return self.nombre

class Mascota(models.Model):
    chip = models.IntegerField(primary_key=True, verbose_name="Código chip de la Mascota")
    nombreMascota = models.CharField(max_length=50, verbose_name="Nombre de la Mascota")
    edadMascota = models.IntegerField(verbose_name="Edad de la mascota", null=False, blank= False)
    colorPelo = models.CharField(max_length=30, verbose_name="Color de cabello de la mascota")
    foto = models.ImageField(upload_to="mascotas", null=True)
    raza = models.ForeignKey(Raza,on_delete= models.CASCADE)

    def __str__(self):
        return self.nombreMascota

    
