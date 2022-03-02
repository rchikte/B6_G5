from django.db import models
# from functools import reduce
# Create your models here.

class ActiveStudManager(models.Manager):
    def get_queryset(self): 
        return super(ActiveStudManager,self).get_queryset().filter(is_active=1)

class InActivestudManager(models.Manager):
    def get_queryset(self):
        return super(InActivestudManager,self).get_queryset().filter(is_active=0)

class Student(models.Model):
    name = models.CharField(max_length = 100)
    marks = models.FloatField()
    subject = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100,null=True)
    age = models.IntegerField()
    is_active =models.BooleanField(default=True)
#     active_objects = ActiveStudManager()
#     inactive_objects = InActivestudManager()
    objects = models.Manager()


    class Meta:
        db_table = "student"

    def __str__(self):
        return f"{self.name}"


class Common_field:
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.__dict__

    class Meta:
        abstract = True

class College(Common_field):
    address = models.CharField(max_length=100)
    
    class Meta:
        db_table = "College"


class Principal(Common_field):
    # college = models.OneToOneField(College,on_delete=models.CASCADE,null=True)


    class Meta:
        db_table = "Principle"


