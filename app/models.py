from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

STATE_CHOICES = (
    ('Adana', 'Adana'),
    ('Adıyaman', 'Adıyaman'),
    ('Afyonkarahisar', 'Afyonkarahisar'),
    ('Ağrı', 'Ağrı'),
    ('Aksaray', 'Aksaray'),
    ('Amasya', 'Amasya'),
    ('Ankara', 'Ankara'),
    ('Antalya', 'Antalya'),
    ('Ardahan', 'Ardahan'),
    ('Artvin', 'Artvin'),
    ('Aydın', 'Aydın'),
    ('Balıkesir', 'Balıkesir'),
    ('Bartın', 'Bartın'),
    ('Batman', 'Batman'),
    ('Bayburt', 'Bayburt'),
    ('Bilecik', 'Bilecik'),
    ('Bingöl', 'Bingöl'),
    ('Bitlis', 'Bitlis'),
    ('Bolu', 'Bolu'),
    ('Burdur', 'Burdur'),
    ('Bursa', 'Bursa'),
    ('Çanakkale', 'Çanakkale'),
    ('Çankırı', 'Çankırı'),
    ('Çorum', 'Çorum'),
    ('Denizli', 'Denizli'),
    ('Diyarbakır', 'Diyarbakır'),
    ('Düzce', 'Düzce'),
    ('Edirne', 'Edirne'),
    ('Elazığ', 'Elazığ'),
    ('Erzincan', 'Erzincan'),
    ('Erzurum', 'Erzurum'),
    ('Eskişehir', 'Eskişehir'),
    ('Gaziantep', 'Gaziantep'),
    ('Giresun', 'Giresun'),
    ('Gümüşhane', 'Gümüşhane'),
    ('Hakkari', 'Hakkari'),
    ('Hatay', 'Hatay'),
    ('Iğdır', 'Iğdır'),
    ('Isparta', 'Isparta'),
    ('İstanbul', 'İstanbul'),
    ('İzmir', 'İzmir'),
    ('Kahramanmaraş', 'Kahramanmaraş'),
    ('Karabük', 'Karabük'),
    ('Karaman', 'Karaman'),
    ('Kars', 'Kars'),
    ('Kastamonu', 'Kastamonu'),
    ('Kayseri', 'Kayseri'),
    ('Kırıkkale', 'Kırıkkale'),
    ('Kırklareli', 'Kırklareli'),
    ('Kırşehir', 'Kırşehir'),
    ('Kilis', 'Kilis'),
    ('Kocaeli', 'Kocaeli'),
    ('Konya', 'Konya'),
    ('Kütahya', 'Kütahya'),
    ('Malatya', 'Malatya'),
    ('Manisa', 'Manisa'),
    ('Mardin', 'Mardin'),
    ('Mersin', 'Mersin'),
    ('Muğla', 'Muğla'),
    ('Muş', 'Muş'),
    ('Nevşehir', 'Nevşehir'),
    ('Niğde', 'Niğde'),
    ('Ordu', 'Ordu'),
    ('Osmaniye', 'Osmaniye'),
    ('Rize', 'Rize'),
    ('Sakarya', 'Sakarya'),
    ('Samsun', 'Samsun'),
    ('Siirt', 'Siirt'),
    ('Sinop', 'Sinop'),
    ('Sivas', 'Sivas'),
    ('Şanlıurfa', 'Şanlıurfa'),
    ('Şırnak', 'Şırnak'),
    ('Tekirdağ', 'Tekirdağ'),
    ('Tokat', 'Tokat'),
    ('Trabzon', 'Trabzon'),
    ('Tunceli', 'Tunceli'),
    ('Uşak', 'Uşak'),
    ('Van', 'Van'),
    ('Yalova', 'Yalova'),
    ('Yozgat', 'Yozgat'),
    ('Zonguldak', 'Zonguldak'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_customer'

CATEGORY_CHOICES = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'app_product'


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"

    class Meta:
        db_table = 'app_cart'
     
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Order {self.id} - {self.status}"

    class Meta:
        db_table = 'app_orderplaced'
     
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
    
    
