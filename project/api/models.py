from django.core.exceptions import ValidationError
from django.db import models
from django.utils.html import normalize_newlines

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


    def clean(self):
        if self.comment is None and self.post is None:
            raise ValidationError("Comment require a reference to a comment or a post")
        if self.comment is not None and self.post is not None:
            raise ValidationError("Comment cannot reference a other comment and a post at the same time")

    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.clean()
        return super().save(*args, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


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

    def clean(self):
        if self.comment is None and self.post is None:
            raise ValidationError("Like require a reference to a comment or a post")
        if self.comment is not None and self.post is not None:
            raise ValidationError("Like cannot reference a other comment and a post at the same time")
    
    class Meta:
        unique_together = [['post', 'username'], ['comment', 'username']]
    
    def save(self, *args, force_insert=False, force_update=False, using=None, update_fields=None):
        self.clean()
        return super().save(*args, force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

