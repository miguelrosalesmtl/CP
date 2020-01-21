from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class ShoppingCartConfig(AppConfig):

    name = 'shopping_cart'
    verbose_name = _('ShoppingCart')

    def ready(self):
        import shopping_cart.signals # noqa