from django.db import models

# Create your models here.
class LoanApp(models.Model):
    lastupdated = models.DateTimeField(auto_now_add=True)
    RequestHeader = models.TextField()
    Business = models.TextField()
    Owners = models.TextField()
    CFApplicationData = models.TextField()

    def __str(self):
        return self.Business