from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from lp_solver import views  # Adjust the import path as needed

urlpatterns = [
    path('', views.home, name='home'),
    path('form/<str:method>/', views.form, name='form'),
    path('solve_graphical/', views.solve_graphical, name='solve_graphical'),
    path('solve_simplex/', views.solve_simplex, name='solve_simplex'),
    path('solve_transportation/', views.solve_transportation, name='solve_transportation'),
]

# Add this only in your main `urls.py`, not in `settings.py`
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
