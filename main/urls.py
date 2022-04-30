from django.urls import path
from . import views
from users.views import redirect_login_view, registration_view, logout_view, login_view


app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', registration_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('provider/',views.provider_home,name='provider'),
    path('vehicles/',views.vehicles,name='vehicles'),
    path('bookings/',views.bookings,name='bookings'),
    path('book/<int:id>',views.book,name='book'),
    path('add_vehicle/',views.add_vehicle,name='add_vehicle'),
    path('login_required/',redirect_login_view,name='redirect_login'),
    path('removeVehicle/<int:id>',views.remove_vehicle,name='remove_vehicle'),
]