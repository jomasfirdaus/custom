from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from custom.models import *
from import_export import resources

# Register your models here.
class CountryResource(resources.ModelResource):
    class Meta:
        model = Country
class CountryAdmin(ImportExportModelAdmin):
    resource_class = CountryResource
admin.site.register(Country, CountryAdmin)

class DonorResource(resources.ModelResource):
    class Meta:
        model = Donor
class DonorAdmin(ImportExportModelAdmin):
    resource_class = DonorResource
admin.site.register(Donor, DonorAdmin)

class BranchResource(resources.ModelResource):
    class Meta:
        model = Branch
class BranchAdmin(ImportExportModelAdmin):
    resource_class = BranchResource
admin.site.register(Branch, BranchAdmin)

class MunisipiuResource(resources.ModelResource):
    class Meta:
        model = Munisipiu
class MunisipiuAdmin(ImportExportModelAdmin):
    resource_class = MunisipiuResource
admin.site.register(Munisipiu, MunisipiuAdmin)

class PostuResource(resources.ModelResource):
    class Meta:
        model = Postu
class PostuAdmin(ImportExportModelAdmin):
    resource_class = PostuResource
admin.site.register(Postu, PostuAdmin)

class SukuResource(resources.ModelResource):
    class Meta:
        model = Suku
class SukuAdmin(ImportExportModelAdmin):
    resource_class = SukuResource
admin.site.register(Suku, SukuAdmin)

class UnitResource(resources.ModelResource):
    class Meta:
        model = Unit
class UnitAdmin(ImportExportModelAdmin):
    resource_class = UnitResource
admin.site.register(Unit, UnitAdmin)

class LevelResource(resources.ModelResource):
    class Meta:
        model = Level
class LevelAdmin(ImportExportModelAdmin):
    resource_class = LevelResource
admin.site.register(Level, LevelAdmin)

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
admin.site.register(Category, CategoryAdmin)

class RequestSetResource(resources.ModelResource):
    class Meta:
        model = RequestSet
class RequestSetAdmin(ImportExportModelAdmin):
    resource_class = RequestSetResource
admin.site.register(RequestSet, RequestSetAdmin)

class MissionResource(resources.ModelResource):
    class Meta:
        model = Mission
class MissionAdmin(ImportExportModelAdmin):
    resource_class = MissionResource
admin.site.register(Mission, MissionAdmin)

class CarResource(resources.ModelResource):
    class Meta:
        model = Car
class CarAdmin(ImportExportModelAdmin):
    resource_class = CarResource
admin.site.register(Car, CarAdmin)

class PositionResource(resources.ModelResource):
    class Meta:
        model = Position
class PositionAdmin(ImportExportModelAdmin):
    resource_class = PositionResource
admin.site.register(Position, PositionAdmin)

class NivelResource(resources.ModelResource):
    class Meta:
        model = Nivel
class NivelAdmin(ImportExportModelAdmin):
    resource_class = NivelResource
admin.site.register(Nivel, NivelAdmin)

class GradeResource(resources.ModelResource):
    class Meta:
        model = Grade
class GradeAdmin(ImportExportModelAdmin):
    resource_class = GradeResource
admin.site.register(Grade, GradeAdmin)

class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department
class DepartmentAdmin(ImportExportModelAdmin):
    resource_class = DepartmentResource
admin.site.register(Department, DepartmentAdmin)