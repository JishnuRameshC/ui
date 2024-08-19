from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def TestView(request):
    return render(request, 'index.html')

# flowclass 
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

class Page6View(TemplateView):
    template_name = 'Dating/page6.html'

class Page7View(TemplateView):
    template_name = 'Dating/page7.html'



# SignUp

# class SignupView(TemplateView):
#     template_name='account/signup.html'

# class LoginView(TemplateView):
#     template_name='account/login.html'
    
# class ProfessionView(TemplateView):
#     template_name='account/profession.html'
    
# class Rel_GoalView(TemplateView):
#     template_name='account/relationship_goal.html'
    
# class InterestView(TemplateView):
#     template_name='account/interested.html'
    
# class CreateGroupView(TemplateView):
#     template_name='groups/create_group.html'
    
# class SubscriptionPlanView(TemplateView):
#     template_name = 'payment/subscription_plans.html'

# class PaymentMethodsView(TemplateView):
#     template_name = 'payment/payment_methods.html'

# class AddPaymentMethodsView(TemplateView):
#     template_name = 'payment/add_payment.html'
    
# class GroupListView(TemplateView):
#     template_name = 'groups/groups.html'
