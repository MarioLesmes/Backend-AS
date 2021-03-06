from django.contrib                 import admin
from django.urls                    import path
from authApp                        import views
from rest_framework_simplejwt.views import(TokenObtainPairView, TokenRefreshView)
urlpatterns = [
    path('admin/',                                          admin.site.urls),
    path('login/',                                          TokenObtainPairView.as_view()),
    path('refresh/',                                        TokenRefreshView.as_view()),
    path('user/',                                           views.UserCreateView.as_view()),
    path('user/<int:pk>/',                                  views.UserDetailView.as_view()),
    path('analisissuelos/remove/<int:user>/<int:pk>/',      views.AnalisisSuelosDeleteView.as_view()),
    path('analisissuelos/update/<int:user>/<int:pk>/',      views.AnalisisSuelosUpdateView.as_view()),
]
