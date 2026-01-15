from django.contrib import admin
from .models import Tutor,Comments,Courses,Chapters,Lecture

admin.site.register(Comments)
admin.site.register(Courses)
admin.site.register(Tutor)
admin.site.register(Chapters)
admin.site.register(Lecture)
