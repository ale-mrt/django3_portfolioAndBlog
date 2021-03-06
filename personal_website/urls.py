from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from portfolio import views

# collezione degli url raggiungibili nell'app, collegati alle views delle singole app
urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", views.home, name="home"),
    path("", views.home, name="home"),
    path('blog/', include('blog.urls')),
    path("portfolio_archive/", views.portfolio_archive, name="portfolio_archive"),
    path("<int:project_id>/", views.project, name="project"),
    path("bio/", views.bio, name="bio"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)