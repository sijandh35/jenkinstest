from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey



# class QuestionManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset()

#     def all_objects(self):
#         return super().get_queryset()

#     def superadmin(self):
#         return self.all_objects().filter(author__username='root')


# class Comment(models.Model):
#   author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
#   body = models.TextField(blank=True)
#   content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,blank=True,null=True)
#   object_id = models.PositiveIntegerField()
#   content_object = GenericForeignKey()
  
#   objects = QuestionManager()
  
# class Post(models.Model):
#   author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
#   title = models.CharField(max_length=75)
#   slug = models.SlugField(unique=True)
#   body = models.TextField(blank=True)
#   comments = GenericRelation('Comment')

# class Picture(models.Model):
#   author = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
#   image = models.ImageField()
#   caption = models.TextField(blank=True)
#   comments = GenericRelation('Comment')


class StockLog(models.Model):
    stock_name = models.CharField(max_length=500,blank=True,null=True)
    json = models.JSONField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,blank=True,null=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return str(self.stock_name) +'  At date:  ' + str(self.updated)


class StockName(models.Model):
    name = models.CharField(max_length=1000,blank=True,null=True)
    log = GenericRelation('StockLog')

    def __str__(self):
        return self.name
    