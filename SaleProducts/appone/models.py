from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.


# Create your models here.
# (id,fullName,Password(Encrepted form), Active, Role,MobileNo, Email (Optional), createdDate, UpdatedDate)
class User(models.Model):
   # id=models.IntegerField()
    fullname = models.CharField(max_length=30)
    username=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30,unique=True)
    active = models.BooleanField(max_length=30,default=True)
    role =  models.CharField(max_length=100,default="admin")
    mobileNo= models.BigIntegerField(blank=True, null=True, default='0')
    email =  models.EmailField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
   # products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='customers')

    class Meta:
        db_table = 'User_INFO'


#(Id, ProductName, Description, price, curency,images,createdDate, salerId(User having role saler), QTY)
class Product(models.Model):
   # id=models.IntegerField()
    productName = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    #curency=
    image = models.ImageField(upload_to='img', blank=True, null=True)
    quantity = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)])
    created_date = models.DateTimeField(auto_now_add=True)
    #salerId=

    class Meta:
        db_table = "PRODUCT_INFO"

#(id, RoleName(Admin,User,Saler,Buyer), isActive)
'''''class Role(models.Model):
    Id=
    roleName=
    isActive=

    class Meta:
        db_table = "Role_INFO"'''