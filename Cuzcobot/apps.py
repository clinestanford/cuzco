from django.apps import AppConfig
from django.db.models.signals import post_save

class CuzcobotConfig(AppConfig):
    name = 'Cuzcobot'

    def ready(self):
        from Cuzcobot.signals import executeOrder
        from Cuzcobot.models import Order
        post_save.connect(executeOrder, sender=Order)

