from django.contrib import admin

# Register your models here.

from django.contrib import admin
from dmapp.models import MovieEntry, ParamEntry

# Register your models here.

class MovieEntryAdmin(admin.ModelAdmin):
  list_display = ('mID', 'mOriginalTitleTP', 'mDateUpdate',)
  list_filter = ('mCat', )
  ordering = ('mDateUpdate', )

class ParamEntryAdmin(admin.ModelAdmin):
  list_display = ('mName', 'mValue',)
  ordering = ('mName', )

admin.site.register(MovieEntry, MovieEntryAdmin)
admin.site.register(ParamEntry, ParamEntryAdmin)
