from django.contrib import admin
from category import models as MODELS_CATE

# Register your models here.

admin.site.register([
    MODELS_CATE.Category,
    MODELS_CATE.Article,
    MODELS_CATE.SubCategory
])