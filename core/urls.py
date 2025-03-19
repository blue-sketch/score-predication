from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from cric.views import home
from cric.views import login_page,register,logout_view,result,dash,profile,team,team_profile

urlpatterns = [
    path('',dash,name="dash"),
    path('home/', home, name="home"),
    path('login_page/',login_page,name="login_page"),
    path('logout_view/', logout_view, name='logout'),
    path('register/',register,name="register"),
    path('result/',result,name="result"),
    path('profile/',profile,name="profile"),
    path('team/', team, name="team"),
    path('team_profile/',team_profile,name="team_profile"),
    # path('live_score/', live_score, name='live_score'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()