from django.contrib import admin
from .models import Tutor,Comments,Courses,Chapters,Lecture,Orders

admin.site.register(Comments)
admin.site.register(Courses)
admin.site.register(Tutor)
admin.site.register(Chapters)
admin.site.register(Lecture)
admin.site.register(Orders)
