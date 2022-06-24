from django.contrib import admin
from .models import *

admin.site.register(MyUser)
admin.site.register(Contact)
admin.site.register(Chart)
admin.site.register(Pro)
admin.site.register(Team)

