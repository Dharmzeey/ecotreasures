import uuid
from django.db import models
from user.models import Seller

class PlasticType(models.Model):
  name = models.CharField(max_length=20)
  image = models.ImageField(upload_to="plastic_type")
  def __str__(self):
    return self.name
    
class Category(models.Model):
  name = models.CharField(max_length=20)
  image = models.ImageField(upload_to="category")
  def __str__(self):
    return self.name

class Store(models.Model):
  owner = models.OneToOneField(Seller, on_delete=models.SET_NULL, related_name="store_owner", null=True)
  def __str__(self):
    return f"{self.owner}"

class Item(models.Model):
  PRODUCT_CATEGORY = (
    ('AC', 'ACCESSORIES'),
    ('AW', 'ART WORK'),
    ('FA', 'FASHION'),
    ('HO', 'HOUSEHOLD'),
    ('FU', 'FURNITURE')
  )
  PLASTIC_TYPE = (
    (1, 'PET'),
    (2, 'HDPE'),
    (3, 'PVC'),
    (4, 'LDPE'),
    (5, 'PP'),
    (6, 'PS'),
    (7, 'O')
  )
  PLASTIC_STATE = (
    (1, 'RECYCLED'),
    (2, 'UPCYCLED')
  )
  uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
  seller = models.ForeignKey(Seller, on_delete=models.SET_NULL, related_name="product_vendor", null=True)
  store = models.ForeignKey(Store, on_delete=models.SET_NULL, related_name="product_store", null=True)
  title = models.CharField(max_length=50)
  description = models.TextField()
  thumbnail = models.ImageField(upload_to="products/%Y/%m")
  price = models.DecimalField(max_digits=15, decimal_places=2)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="item_category")
  type = models.ForeignKey(PlasticType, on_delete=models.SET_NULL, null=True, related_name="item_type")
  state = models.IntegerField(choices=PLASTIC_STATE)
  
  def __str__(self):
    return self.title

class ItemImage(models.Model):
  item = models.ForeignKey(Item, on_delete=models.CASCADE,related_name="item_image")
  image = models.ImageField(upload_to="products/%Y/%m")
  
  def __str__(self):
    return f"{self.item}"
  
  