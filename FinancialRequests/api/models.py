from django.db import models

# Create your models here.

class LoanApp(models.Model):
    lastupdated = models.DateTimeField(auto_now_add=True)
    RequestHeader = models.TextField()
    Business = models.TextField()
    Owners = models.TextField()
    CFApplicationData = models.TextField()

    def __str__(self):
        return '%s\n %s\n %s\n %s' % (self.requestheader, self.business, self.owners, self.cfapplicationdata)
