from django.apps import AppConfig


class AlphaTradeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alpha_trade'

    def ready(self):
        from . import updater
        updater.start()
