from django.contrib import admin
from .models import *
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'test_score','ranking','last_updated_time']
  #  list_per_page = 40

    search_fields = ['name', 'ranking']


class TestingAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'last_updated_time']
    search_fields = ['title']

class ScoreAdmin(admin.ModelAdmin):
    list_display = ['student', 'test', 'score']
    search_fields = ['student__name', 'test__title']

class StemAdmin(admin.ModelAdmin):
    list_display = ['title','testing','number']
    search_fields = ['title', 'testing__title']
  #  list_per_page = 20

class OptionAdmin(admin.ModelAdmin):
    list_display = ['stem', 'comment']
    search_fields = ['stem__title']
 #   list_per_page = 20

class FillinAdmin(admin.ModelAdmin):
    list_display = ['stem', 'number']
    search_fields = ['stem__title','number']
    list_per_page = 20

class StandardAdmin(admin.ModelAdmin):
    list_display = ['id','perfectly', 'good','passably']

admin.site.register(Student, StudentAdmin)
admin.site.register(Testing, TestingAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Stem, StemAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Fillin, FillinAdmin)
admin.site.register(Standard, StandardAdmin)

admin.site.site_header = 'административный центр'
admin.site.site_title = 'админ'