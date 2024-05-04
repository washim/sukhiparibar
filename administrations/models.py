from django.db import models


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    address = models.TextField()
    leader_name = models.CharField(max_length=256)
    mobile = models.CharField(blank=True, null=True, max_length=256)
    day = models.CharField(blank=True, null=True, max_length=256)

    class Meta:
        managed = False
        db_table = 'groups'

    def __str__(self):
        return self.name


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(Group, db_column='group_id', on_delete=models.CASCADE, verbose_name='Group Name')
    bookno = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=256)
    address = models.TextField()
    mobile = models.CharField(blank=True, null=True, max_length=256)
    product_no = models.CharField(max_length=256)
    product_name = models.CharField(max_length=256)
    product_price = models.FloatField()
    advance_paid = models.FloatField()
    advance_paid_date = models.DateTimeField()
    gurdian = models.CharField(max_length=256)
    total_emi_no = models.IntegerField()
    emi_amount = models.FloatField()

    class Meta:
        managed = False
        db_table = 'customers'

    @property
    def emi_paid(self):
        total_emi_paid = Emi.objects.filter(cid=self.id).aggregate(models.Sum('amount'))
        return total_emi_paid['amount__sum'] if total_emi_paid['amount__sum'] else 0

    @property
    def emi_pending(self):
        product_price = self.product_price if self.product_price else 0
        advance_paid = self.advance_paid if self.advance_paid else 0
        return product_price - advance_paid - self.emi_paid

    def __str__(self):
        return str(self.bookno) + f'({self.name})'


class Emi(models.Model):
    id = models.AutoField(primary_key=True)
    cid = models.ForeignKey(Customer, db_column='cid', on_delete=models.CASCADE, verbose_name='Book No')
    amount = models.FloatField()
    due_dt = models.DateField('Date')

    class Meta:
        managed = False
        db_table = 'emis'

    def __str__(self):
        return ''