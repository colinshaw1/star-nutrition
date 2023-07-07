from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'


    # overwrite ready method and import the signals
    def ready(self):
        import checkout.signals
