from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("", views.TestView, name="test"),



    # account

    
    # dating pages
    path("home", views.HomePageview.as_view(), name="home"),
    path('qualification',views.QualificationPageView.as_view(),name="qualification"),
    path('discovery/',views.DiscoveryPageView.as_view(),name='discovery'),
    path('location/',views.LocationPageView.as_view(),name='location'),
    path('designation/',views.DesignationView.as_view(),name="designation"),
    path("matches/",views.MatchesView.as_view()),
    path("",views.Page6View.as_view()),
    path("hjbj",views.Page7View.as_view()),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
