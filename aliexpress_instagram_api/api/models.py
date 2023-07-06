from django.db import models

class AliExpressItem(models.Model):
    image = models.ImageField(upload_to='aliexpress_images')
    text = models.TextField()
    
    