from django.contrib import admin
from life.models import *

# Register your models here.
admin.site.register(Group)
admin.site.register(Thread)
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Choice)