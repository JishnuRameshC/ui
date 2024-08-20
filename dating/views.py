from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def TestView(request):
    return render(request, 'index.html')


# SignUp
class SignupView(TemplateView):
    template_name='account/signup.html'


class LoginView(TemplateView):
    template_name='account/login.html'


class ProfessionView(TemplateView):
    template_name='account/profession.html'


class Rel_GoalView(TemplateView):
    template_name='account/relationship_goal.html'


class InterestView(TemplateView):
    template_name='account/interested.html'


# Group 
class CreateGroupView(TemplateView):
    template_name='groups/create_group.html'


class GroupListView(TemplateView):
    template_name = 'groups/groups.html'


# SubscriptionPlan
class SubscriptionPlanView(TemplateView):
    template_name = 'payment/subscription_plans.html'


class PaymentMethodsView(TemplateView):
    template_name = 'payment/payment_methods.html'


class AddPaymentMethodsView(TemplateView):
    template_name = 'payment/add_payment.html'


# Dating 
class FirstView(TemplateView):
    template_name = 'test.html'


class DiscoveryPageView(TemplateView):
    template_name = 'Dating/discover.html'


class HomePageview(TemplateView):
    template_name = 'Dating/home.html'


class QualificationPageView(TemplateView):
    template_name = 'Dating/qualification.html'


class LocationPageView(TemplateView):
    template_name = 'Dating/location.html'


class DesignationView(TemplateView):
    template_name = 'Dating/designation.html'


class MatchesView(TemplateView):
    template_name = 'Dating/matches.html'


class ViewedMyProfileView(TemplateView):
    template_name = 'Dating/viewed_my_profile.html'


class Page7View(TemplateView):
    template_name = 'Dating/page7.html'


class SpinWheelView(TemplateView):
    template_name = 'dating/spin.html'


# UserProfileFlow
class ChangePasswordView(TemplateView):
    template_name = 'User_profile_flow/change_password.html'


class ContactedView(TemplateView):
    template_name = 'User_profile_flow/contacted.html'


class EditMyProfileView(TemplateView):  
    template_name = 'User_profile_flow/edit_my_profile.html'


class MessageView(TemplateView):    
    template_name = 'User_profile_flow/message.html'


class SettingsView(TemplateView):   
    template_name = 'User_profile_flow/settings.html'


class ShortlistView(TemplateView):    
    template_name = 'User_profile_flow/shortlist.html'

class StoryView(TemplateView):    
    template_name = 'User_profile_flow/story.html'


class UpdateViewProfile(TemplateView):    
    template_name = 'User_profile_flow/update_profile.html'


class UpdateViewStory(TemplateView):    
    template_name = 'User_profile_flow/upgrade_to_view_story.html'  


class UserProfile(TemplateView):    
    template_name = 'User_profile_flow/user_profile.html'


class ShortlistedView(TemplateView):    
    template_name = 'User_profile_flow/shortlist.html'

