from django.contrib import admin
from .models import District, AccountType, Material, Branch,Gender


# Register your models here.
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(District, DistrictAdmin)


class AccountTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(AccountType, AccountTypeAdmin)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Material, MaterialAdmin)


class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'district']


admin.site.register(Branch, BranchAdmin)
class GenderAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Gender, GenderAdmin)