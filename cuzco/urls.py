
from django.contrib import admin
from django.urls import path
from Cuzcobot.views import pairs

from Cuzcobot.views import pairs, fillThirtyDays

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('trade/', ),
    #path('buy/', ),
    #path('sell/'),
    #path('history/'),
    path('pairs/', pairs),
    #path('test')
    #path('test'),
    path('last30days/', fillThirtyDays),
]
