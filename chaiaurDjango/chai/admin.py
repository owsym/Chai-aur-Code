from django.contrib import admin
from .models import ChaiVarity, ChaiReview, Store, ChaiCertificate


# Inline for ChaiReview
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReview
    extra = 0


# Inline for ChaiCertificate (OneToOne)
class ChaiCertificateInline(admin.StackedInline):
    model = ChaiCertificate
    extra = 0


# Admin for ChaiVarity
class ChaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'date_added', 'type', 'description')
    inlines = [ChaiReviewInline, ChaiCertificateInline]


# Admin for Store (standalone)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_variety',)


# Admin for Certificate (standalone, optional)
class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('certificate_number', 'user', 'date_issued', 'valid_until')


# Register your models
admin.site.register(ChaiVarity, ChaiVarityAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
