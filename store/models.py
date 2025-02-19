from django.db import models

# Create your models here.
class Promotion(models.Model):    
    description = models.CharField(max_length= 255)  
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length= 255)   
    featured_product = models.ForeignKey('Product', on_delete= models.SET_NULL, null=True, related_name='+')

class Product(models.Model):
    title = models.CharField(max_length= 255)
    slug = models.SlugField()
    description = models.TextField()
    price = models.DecimalField(max_digits= 6, decimal_places= 2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now= True)
    collection = models.ForeignKey(Collection,on_delete = models.PROTECT)
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEMEBERSHIP_BRONZE = 'B'
    MEMEBERSHIP_SILVER = 'S'
    MEMEBERSHIP_GOLD = 'G'

    MEMEBERSHIP_CHOICES = [
        (MEMEBERSHIP_BRONZE , 'Bronze'),
        (MEMEBERSHIP_SILVER , 'Silver'),
        (MEMEBERSHIP_GOLD , 'Gold')

    ] 
    first_name = models.CharField (max_length= 100)
    last_name = models.CharField (max_length= 100)
    email = models.CharField(max_length= 100, unique= True)
    phone = models.CharField (max_length= 20)
    birth_date = models.DateField(null= True)
    memebership = models.CharField(max_length=1 , choices = MEMEBERSHIP_CHOICES, default= MEMEBERSHIP_BRONZE)
    class Meta:
        db_table = 'store_customers'
        indexes = [
            models.Index(fields= ['first_name','last_name'])
        ]


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'

    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING , 'Pending'),
        ( PAYMENT_STATUS_COMPLETE , 'Complete'),
        ( PAYMENT_STATUS_FAILED , 'Failed')

    ] 
    placed_at = models.DateTimeField (auto_now_add= True)    
    payment_status = models.CharField(max_length=1, choices= PAYMENT_STATUS_CHOICES, default= PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(Customer, on_delete= models.PROTECT)

class Address (models.Model):
    street = models.CharField(max_length= 255)
    city = models.CharField(max_length= 255)
    zip = models.CharField(max_length=10, null=True)
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)

class OrderItems(models.Model):
    order = models.ForeignKey (Order,on_delete = models.PROTECT)
    product = models.ForeignKey (Product,on_delete = models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits= 6, decimal_places= 2)

class Cart(models.Model):
    created_at = models.DateTimeField (auto_now_add= True)    

class CartItems(models.Model):
    cart = models.ForeignKey(Cart,on_delete = models.CASCADE)
    prodcut = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.PositiveSmallIntegerField()