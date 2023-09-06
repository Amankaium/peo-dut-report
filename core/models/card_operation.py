from django.db import models


class CardOperation(models.Model):
    date = models.DateTimeField('Дата', auto_now_add=True)
    station = models.ForeignKey(to=Station, on_delete=models.CASCADE)
    card = models.ForeignKey(to=Card, on_delete=models.CASCADE)
    fuel_type = models.ForeignKey(to=FuelType, on_delete=models.CASCADE)
    operation_type = models.ForeignKey(to=OperationType, on_delete=models.CASCADE)
    balance_before = models.DecimalField('Баланс до', max_digits=19, decimal_places=10)
    balance_after = models.DecimalField('Баланс после', max_digits=19, decimal_places=10)
    dose = models.DecimalField('Доза', max_digits=19, decimal_places=10)
    price_som = models.DecimalField('Цена, сом', max_digits=19, decimal_places=10)
    sum_som = models.DecimalField('Сумма, сом', max_digits=19, decimal_places=10)

    class Meta:
        verbose_name = 'Операция по карте'
        verbose_name_plural = 'Операции по карте'