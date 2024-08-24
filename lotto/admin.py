from django.contrib import admin

# Register your models here.

#from lotto.models import GuessNumbers

from .models import GuessNumbers

admin.site.register(GuessNumbers)