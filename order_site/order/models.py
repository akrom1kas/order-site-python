from django.db import models
from datetime import date
from PIL import Image

class Customer(models.Model):
    first_name = models.CharField('Name', max_length=100)
    last_name = models.CharField('Surname', max_length=100)
    email = models.EmailField('Email', max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name', 'email']

    def get_absolute_url(self):
        return reverse('customer-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.email} '

class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products', default='python.png')
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    Product= models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    Customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    date = models.DateField(("Date"), default=date.today)

    LOAN_STATUS = (
        ('a', 'Nupirkti'),
        ('p', 'Rezervuoti'),
    )
    Status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='a',
        help_text='Statusas',
    )
    def __str__(self):
        return str(self.Customer)


class ProductOrder(models.Model):
    Order = models.ForeignKey('Customer', on_delete=models.SET_NULL, null=True)
    product =  models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


    def __str__(self):
        return str(self.Order)

