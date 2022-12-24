from gettext import gettext

from django.db.models import Model, BooleanField
from django.utils.functional import lazy

# python manage.py sqlmigrate APP名称 0001

gettext_lazy = lazy(gettext, str)
class Test(Model):
    is_dps_order_isolate = BooleanField(gettext_lazy('私密代理是否订单隔离'), default=False,
                                               help_text=gettext_lazy('勾选后，则会使用新版规则'))
    is_dps_order_isolate1 = BooleanField(gettext_lazy('私密代理是否订单隔离'), default=False,
                                               help_text=gettext_lazy('勾选后，则会使用新版规则'))

    class Meta:
        db_table='test'
