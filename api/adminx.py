# from django.contrib import admin
from .models import APILoan
import xadmin

# Register your models here.



class APILoanAdmin:


    search_fields = ['name', 'phone']
    list_display = APILoan().list_field
    ordering = ['-create_time']
xadmin.site.register(APILoan,APILoanAdmin)


