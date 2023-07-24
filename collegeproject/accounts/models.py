from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
class Person(models.Model):
    name = models.CharField(max_length=124)
    dob=models.CharField(max_length=20,null=True)
    age=models.IntegerField()
    gen=(('other',"OTHER"),('male',"MALE"),('female',"FEMALE"))
    gender=models.CharField(max_length=10,choices=gen,default='user')
    phone_number=models.CharField(max_length=20,null=True,blank=True)
    email=models.EmailField(max_length=100,null=True,blank=True)
    address=models.TextField(max_length=260,blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, blank=True, null=True)
    purpose=(('select',"SELECT"),('enquiry',"ENQUIRY"),('place order',"PLACE ORDER"),('return',"RETURN"),('payment',"PAYMENT"),('other',"OTHER"))
    purpose=models.CharField(max_length=20,choices=purpose,default='user')

    def __str__(self):
        return self.name