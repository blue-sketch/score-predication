from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from cric.views import home
from cric.views import login_page,register,logout_view,result,dash,profile,team,team_profile, ask_ai_page, proxy_llm,feedback,home_view,upcoming

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
    path("ask-ai_page/", ask_ai_page, name="ask_ai_page"), 
    path('feedback/', feedback, name='feedback'),
    path('home_view/',home_view,name="home_view"),
    path('upcoming/',upcoming,name="upcoming"),
    path('admin/', admin.site.urls),
    path("proxy_llm/", proxy_llm, name="proxy_llm"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()