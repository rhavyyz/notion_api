from django.db import models

# Create your models here.

class Post(models.Model):
    username = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True)
   
    @property
    def like_qtd(self):
        return Like.objects.filter(post__id=self.id).count()


class Comment(models.Model):
    username = models.CharField(max_length=100)
    post = models.ForeignKey(
                             Post, 
                             on_delete=models.CASCADE, 
                             null=True,
                             blank = True
                            )   
    comment = models.ForeignKey(
                             'self',
                             related_name='+',
                             on_delete=models.CASCADE, 
                             null=True,
                             blank = True
                            )
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True)
 
    @property
    def like_qtd(self):
        print(self.id)
        return Like.objects.filter(comment__id=self.id).count()


class Like(models.Model):
    post = models.ForeignKey(
                             Post, 
                             on_delete=models.CASCADE, 
                             null=True,
                             blank = True
                            )   
    comment = models.ForeignKey(
                             Comment, 
                             on_delete=models.CASCADE, 
                             null=True,
                             blank = True
                            )

    username = models.CharField(max_length=100)

    class Meta:
        unique_together = [['post', 'username'], ['comment', 'username']]
