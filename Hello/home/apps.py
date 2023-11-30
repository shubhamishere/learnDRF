from django.apps import AppConfig

#this is out "home" app that we have made under Hello django project
class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
