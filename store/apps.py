from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'
<<<<<<< HEAD

    def ready(self) -> None:
        import store.signals.handlers
=======
>>>>>>> a77aecced6d01cf351118df2ea482b17fbe03da9
