from django.db import models

# This Django models module defines a "Contact" class, representing contact information
# stored in the database. It includes fields for name, email, phone, message description,
# and date. The class also overrides the "str" method to provide a string representation 
# of a Contact object, returning the name. This model allows for storing contact details 
# submitted through a form on the website. When combined with Django's migration commands
# like "makemigrations" and "migrate," it facilitates seamless database management,
# enabling the creation and application of schema changes efficiently.

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
# the whole game is here to add this all files to the data base
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()


# to see who register (to chnage the object name in migration)
    def __str__(self):
        return self.name
    