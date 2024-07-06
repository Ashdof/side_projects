from django.apps import AppConfig


class AshpensersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ashpensers'

    def ready(self):
        import ashpensers.signals
