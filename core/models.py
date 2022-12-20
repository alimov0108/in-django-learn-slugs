from django.db import models

class Post(models.Model):
    nomi = models.CharField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    rasm_url = models.CharField(max_length=255)
    tarif = models.TextField()

    def __str__(self) -> str:
        return self.nomi