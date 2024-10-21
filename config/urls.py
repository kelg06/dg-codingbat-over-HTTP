from django.contrib import admin
from django.urls import path

from app.views import near_hundred ,string_splosion , cat_dog , lone_sum

urlpatterns = [
    path("warmup-1/near-hundred/<n>",near_hundred),
    path("warmup-2/string-splosion/<str>",string_splosion),
    path("string-2/cat-dog/<str>",cat_dog),
    path("logic-2/lone-sum/<a>/<b>/<c>",lone_sum ),
    path('admin/', admin.site.urls),
]
