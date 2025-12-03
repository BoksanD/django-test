from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView, TemplateView
from etl.models import Client,InsurenceType,Subscription
from django.db.models import Q,ExpressionWrapper, DurationField,F
import subprocess
import webbrowser
from django.contrib import messages
from django.shortcuts import redirect
from django.utils import timezone
from .subscription_form import SubscriptionForm

# Create your views here.

class LaunchUtilityView(TemplateView):
    template_name = "etl/launch_utility.html"
    
    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        
        if action == 'open_url':
            url = request.POST.get('url', 'https://www.example.com')
            try:
                webbrowser.open(url)
                messages.success(request, f'Opened URL: {url}')
            except Exception as e:
                messages.error(request, f'Error opening URL: {str(e)}')
        
        elif action == 'run_python':
            script_path = request.POST.get('script_path', '')
            try:
                # For security, you should validate the script_path
                result = subprocess.run(
                    ['python', script_path],
                    capture_output=True,
                    text=True,
                    timeout=30
                )
                messages.success(request, f'Script output: {result.stdout}')
                if result.stderr:
                    messages.warning(request, f'Errors: {result.stderr}')
            except Exception as e:
                messages.error(request, f'Error running script: {str(e)}')
        
        return redirect('launch-utility')

class ClientListView(ListView):
    model = Client
    template_name = "etl/client_list.html"
    context_object_name = "clients"
    paginate_by = 5
    
    def get_queryset(self):
        queryset = Client.objects.all().order_by("reg_date")
        search_query = self.request.GET.get('search', '')
        
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(reg_date__icontains=search_query)
            )
        
        # Filter by active status
        status_filter = self.request.GET.get('status', '')
        if status_filter == 'active':
            queryset = queryset.filter(is_active=True)
        elif status_filter == 'inactive':
            queryset = queryset.filter(is_active=False)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['status_filter'] = self.request.GET.get('status', '')
        return context

class ClientCreateView(CreateView):
    model = Client
    template_name = "etl/client_form.html"
    fields = ['name','reg_date','is_active']
    success_url = reverse_lazy('client-list')

class ClientUpdateView(UpdateView):
    model = Client
    template_name = "etl/client_form.html"
    fields = ['name','reg_date','is_active']
    success_url = reverse_lazy('client-list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = "etl/client_confirm_delete.html"
    success_url = reverse_lazy('client-list')

class InsurenceListView(ListView):
    model = InsurenceType
    template_name = "etl/insurence_list.html"
    context_object_name = "insurences"

class InsurenceCreateView(CreateView):
    model = InsurenceType
    template_name = "etl/insurence_form.html"
    fields = ['name','price','expires_in_days']
    success_url = reverse_lazy('insurence-list')

class InsurenceUpdateView(UpdateView):
    model = InsurenceType
    template_name = "etl/insurence_form.html"
    success_url = reverse_lazy('insurence-list')
class InsurenceDeleteView(DeleteView):
    model = InsurenceType
    template_name = "etl/insurence_confirm_delete.html"
    success_url = reverse_lazy('insurence-list')
class SubscriptionListView(ListView):
    model = Subscription
    template_name = "etl/subscription_list.html"
    context_object_name = "subscriptions"
    paginate_by = 5
    
    def get_queryset(self):
        queryset = Subscription.objects.annotate(
    days_left=ExpressionWrapper(F('valid_till') - timezone.now(), output_field=DurationField())
).order_by('days_left')
        search_query = self.request.GET.get('search', '')
        
        if search_query:
            queryset = queryset.filter(
                Q(payment_method__icontains=search_query) |
                Q(client__name__icontains=search_query) |
                Q(insurence__name__icontains = search_query)
            )
        
        status_filter = self.request.GET.get('expired', '')
        now = timezone.now()

        if status_filter == 'active':
            queryset = queryset.filter(valid_till__gt=now)
        elif status_filter == 'expired':
            queryset = queryset.filter(valid_till__lt=now)
        
        return queryset


class SubscriptionCreateView(CreateView):
    model = Subscription
    template_name = "etl/subscription_form.html"
    form_class = SubscriptionForm
    success_url = reverse_lazy('subscription-list')
    
class SubscriptionUpdateView(UpdateView):
    model = Subscription
    template_name = "etl/subscription_form.html"
    fields = ['payment_method','client','insurence','starts_at']
    success_url = reverse_lazy('subscription-list')
class SubscriptionDeleteView(DeleteView):
    model = Subscription
    template_name = "etl/subscription_confirm_delete.html"
    success_url = reverse_lazy('subscription-list')