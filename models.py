from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class Country(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Country Name")
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Countrycreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Countryupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Countrydeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='01-Data-Custom-Country'


class Donor(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Donor Name")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=False, related_name="Donorcountry")
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Donorcreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Donorupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Donordeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='02-Data-Custom-Donor'


class Branch(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Branch Name")
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Branchcreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Branchupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Branchdeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='03-Data-Custom-Branch'


class Munisipiu(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Munisipiu Name")
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Munisipiucreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Munisipiuupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Munisipiudeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='04-Data-Custom-Munisipiu'


class Postu(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Postu Name")
    munisipiu = models.ForeignKey(Munisipiu, on_delete=models.CASCADE, null=True, blank=False, related_name="Postucountry")
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Postucreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Postuupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Postudeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='05-Data-Custom-Postu'


class Suku(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Suku Name")
    postu = models.ForeignKey(Postu, on_delete=models.CASCADE, null=True, blank=False, related_name="Sukucountry")
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Sukucreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Sukuupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Sukudeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='06-Data-Custom-Suku'


class Unit(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Unit Name")
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Unitcreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Unitupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Unitdeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='06-Data-Custom-Unit'


class Level(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Level Name")
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Levelcreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Levelupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Leveldeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='07-Data-Custom-Level'


class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Category Name")
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Categorycreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Categoryupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Categorydeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='08-Data-Custom-Category'


class RequestSet(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=False, related_name="RequestSetrequestorder")
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=True, blank=False, related_name="RequestSetlevel")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=False, related_name="RequestSetrequestcategory")
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="RequestSetcreatedby")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="RequestSetupdatedby")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="RequestSetdeletedby")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.category.name}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='09-Data-Purchase_Request-Request_Set'


class Mission(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name="Mission Name")
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Missioncreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Missionupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Missiondeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='10-Data-Custom-Mission'


class Car(models.Model):
    vehicle_number = models.CharField(max_length=100, null=False, blank=False, verbose_name="Vehicle Number")
    vehicle_type = models.CharField(max_length=100, null=False, blank=False, verbose_name="Type of Vehicle")
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Carcreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Carupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Cardeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.vehicle_number}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='11-Data-Custom-Car'



class Grade(models.Model):
    name = models.CharField(max_length=100)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Gradecreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Gradeupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Gradedeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='11-Data-Custom-Grade'


class Nivel(models.Model):
    name = models.CharField(max_length=100)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Nivelcreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Nivelupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Niveldeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.name}'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='11-Data-Custom-Nivel'


class Department(models.Model):
    code = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=100)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Departmentcreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Departmentupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Departmentdeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.name} ({0.code})'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='11-Data-Custom-Department'

class Position(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, null=True, blank=True)
    
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Positioncreatedbys")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Positionupdatetedbys")
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="Positiondeletedbys")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        template = '{0.name} ({0.code})'
        return template.format(self)
    
    def delete(self, user):
        self.deleted_at = str(timezone.now())
        self.deleted_by = user
        self.save()

    default_objects = models.Manager()  # The default manager
    objects = ActiveManager()

    class Meta:
        verbose_name_plural='11-Data-Custom-Position'


# Add the auditlog
#auditlog.register(Country)