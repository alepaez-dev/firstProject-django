from django.db import models

# Create your models here.

# id -> SERIAL autoincrement
# first_name -> string
# last_name -> string
# generation -> string
# email -> string
# phone -> string
# status -> (activo, dado de baja)
# address -> string
# size -> (s, m, l)
# created_at -> date
# updated_at -> date
# birthdate -> date

# Las clases(modelos) van capitalizadas -> Koder
# Los modelos heredan del modelo predeterminado de Django
# Cada modelo representa una tabla de SQL
# Cada propiedad de la clase(modelo) representa un atributo en la tabla

# LA foreign key se pone en la N en las relaciones 1 - N
# Cuando hay N - N, la FK se pone en el mas chico jerarquicamente -> mentors
#  1 generation - N koders
#  N mentors - N generations
#  1 bootcamp - N generations

# Todos los mentores que esten en el bootcamp de 'python'


class Bootcamp(models.Model):
    """Bootcamp model."""

    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Generation(models.Model):
    """Generation model."""

    number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    # Foreign Key
    bootcamp = models.ForeignKey(Bootcamp, models.PROTECT, related_name="generations")

    def __str__(self):
        return f"{self.number} {self.bootcamp.name}"


class Koder(models.Model):
    """Koder Model."""

    STATUSES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("finished", "Finished"),
    ]

    first_name = models.CharField(max_length=254)  # -> string
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    status = models.CharField(max_length=8, choices=STATUSES, default="active")
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # -> En cuanto se cree nos agrega la hora por automatico

    # Foreign keys
    # Related name buena practica -> Nombre del modelo en plural.
    generation = models.ForeignKey(Generation, models.PROTECT, related_name="koders")

    # Representar como nos regresan al koder.
    def __str__(self):
        return f"FirstName -> {self.first_name}, LastName -> {self.last_name}"


class Mentor(models.Model):
    """Mentor model."""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    # Foreign keys
    generations = models.ManyToManyField(Generation, related_name="mentors")

    def __str__(self):
        return f"id: {self.pk} {self.first_name} {self.last_name}"


# Koders pertenece a 1 generacion -> 1 generation - N koderss
# Mentores pertecene a varias generaciones -> N mentors - N generations
# Generaciones pertenecen a un bootcamp -> 1 bootcamp - N generations
