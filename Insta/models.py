from django.db import models
from django.urls import reverse
from imagekit.models import ProcessedImageField


# Create your models here.
class Post(models.Model):
    title  = models.TextField(blank=True,null=True)
    image = ProcessedImageField(
        upload_to = 'static/images/posts',
        format = 'JPEG',
        blank=True, 
        null=True,
    )

    # 重定向提交表单的目标url
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
        # reverse会遍历所有urls，找一个post_detail的路径，args是传的参数
    
