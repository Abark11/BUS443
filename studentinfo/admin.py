from django.contrib import admin
from studentinfo.models import Studentdetails
from studentinfo.models import Coursedetails
from studentinfo.models import Enrollmentdetails



# Register your models here.

admin.site.register(Studentdetails)

admin.site.register(Coursedetails)

admin.site.register(Enrollmentdetails)

