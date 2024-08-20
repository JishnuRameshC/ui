from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("", views.TestView, name="test"),
    # account
    path("login", views.LoginView.as_view(), name="login"),
    path("signup", views.SignupView.as_view(), name="signup"),
    path("profession", views.ProfessionView.as_view(), name="profession"),
    path("rel_goal", views.Rel_GoalView.as_view(), name="rel_goal"),
    path("interest", views.InterestView.as_view(), name="interest"),
    
    path("create_group", views.CreateGroupView.as_view(), name="create_group"),
    path("groups", views.GroupListView.as_view(), name="groups"),
    path("subscription_plan", views.SubscriptionPlanView.as_view(), name="subscription_plan"),
    path("payment_methods", views.PaymentMethodsView.as_view(), name="payment_methods"),
    path("add_payment", views.AddPaymentMethodsView.as_view(), name="add_payment"),
    
    # dating pages
    path("home", views.HomePageview.as_view(), name="home"),
    path('qualification',views.QualificationPageView.as_view(),name="qualification"),
    path('discovery/',views.DiscoveryPageView.as_view(),name='discovery'),
    path('location/',views.LocationPageView.as_view(),name='location'),
    path('designation/',views.DesignationView.as_view(),name="designation"),
    path("matches/",views.MatchesView.as_view()),
    path("viewed_my_profile/",views.ViewedMyProfileView.as_view()),
    path("hjbj",views.Page7View.as_view()),
    path('spin/',views.SpinWheelView.as_view(),name="spin"),

    path("change_password",views.ChangePasswordView.as_view()),
    path("contacted",views.ContactedView.as_view()),
    path("edit_profile",views.EditMyProfileView.as_view()),
    path("message",views.MessageView.as_view()),
    path("settings",views.SettingsView.as_view()),
    path("story",views.StoryView.as_view()),
    path("update_profile",views.UpdateViewProfile.as_view()),
    path("update_story",views.UpdateViewStory.as_view()),
    path("user_profile",views.UserProfile.as_view()),
    path("shortlist",views.ShortlistedView.as_view()),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
