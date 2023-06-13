from django.db import models

class Collection(models.Model):
        title = models.CharField(max_length=255)
        
        
class promotion(models.Model):
    description = models.CharField(max_length=255)        


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    descriptions = models.TextField()
    unit_price = models.DecimalField(max_digits=6 ,decimal_places=2)
    invetory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    Collection = models.ForeignKey(Collection , on_delete=models.PROTECT )
    promotion = models.ManyToManyField(promotion)
    
class Customer(models.Model):
    membership_bronze = "B"
    membership_silver = "S"
    membership_gold = "G"
    
    membership_choices = [
        (membership_bronze , "BRONZE"),
        (membership_silver , "SILVER"),
        (membership_gold , "GOLD"),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    birth_day = models.DateField(null=True)
    membership = models.CharField(max_length=1 , choices=membership_choices, default=membership_bronze)
    
    
class Order(models.Model):
    payment_pending = "P"
    payment_complete = "C"
    payment_failed = "F"
    payment_status_choices=[
        (payment_pending , "Pending"),
        (payment_complete , "Complete"),
        (payment_failed , "Failed")    
    ]
    place_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=payment_status_choices , default=payment_pending)
    Customer = models.ForeignKey(Customer,on_delete= models.PROTECT)
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=models.PROTECT)
    Product = models.ForeignKey(Product , on_delete=models.prefetch_related_objects)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6 , decimal_places=2)
    
    
class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart , on_delete= models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
   
        
    