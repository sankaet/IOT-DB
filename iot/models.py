from django.db import models
import uuid

# Create your models here.
class Client(models.Model):
    """
    Default client implementation.
    Expected fields:
    * :attr:`name`
    * :attr:`client_id`
    * :attr:`client_secret`
    """
    name = models.CharField(max_length=255,blank=True)
    client_id = models.CharField(max_length=255,blank = True)
    client_secret = models.CharField(max_length=255,blank = True)

    def set_client_creds(self):
        has_id = True
        while has_id:
            client_id = '{0}-{1}'.format('id',str(uuid.uuid4()))
            if not Client.objects.filter(client_id=client_id).exists():
                has_id = False
        self.client_id = client_id
        self.client_secret = '{0}-{1}'.format('secret',str(uuid.uuid4()))
        self.save()