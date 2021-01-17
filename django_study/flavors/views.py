from django.shortcuts import render
# from store.exceptions import OutOfStock,CorruptedDatabase
from django.db import transaction
from .models import Flavor
from django.views.generic import ListView,DetailView,UpdateView,CreateView
from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .forms import FlavorForm
from account.models import CustomUser

# try:
#   return Flavor.objects.get
# except Flavor.DoesNotExist:
#   msg = "We are out of {}".format(req)
#   raise OutOfStock(msg)
    
# except Flavor.MultipleObjectsReturned:
#   msg = "Multiple items have SKU {}. Please fix!".format(req)
#   raise CorruptedDatabase(msg)

@transaction.atomic
def transaction_test1(arg1, arg2):
    #start transaction
    a.save()

    b.save()
    #end transaction

def transaction_test2(arg1, arg2):
    
    a.save()    # 항상 save 처리됨, 예외가 발생할 경우 에러 발생

    with transaction.atomic():
        #start transaction
        b.save()
        c.save()
        #end transaction

class TitleSearchMixin(object):
    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get("q")
        if q:
            return queryset.filter(title__icontains =q)
        return Flavor.objects.all()

class FlavorListView(TitleSearchMixin,ListView):
    model = Flavor
    context_object_name = 'tests'


class FlavorMixin(object):
    
    def test(self):
        body = self.object.body
        title = self.object.title
        id = self.object.id
        return{
            "title" : title,
            "body" : body,
            "id" : id
        }

class FlavorDetailView(LoginRequiredMixin,FlavorMixin,DetailView):
    model = Flavor
    login_url = "/sign/in"

# class FlavorResultsView(FlavorDetailView):
#     template_name = "tastings/detail.html"
    
# class FlavorUpdateView(UpdateView):

class FlavorActionMixin(object):
    model = Flavor
    fields = ('title','body')
    redirect_field_name = "/flavor"

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("detail",
            kwargs={"pk": self.object.pk})

class FlavorCreateView(LoginRequiredMixin,FlavorActionMixin,CreateView):
    login_url = "/sign/in"
    success_msg = "create!"
    
class FlavorUpdateView(LoginRequiredMixin,FlavorActionMixin,UpdateView):
    login_url = "/sign/in"
    success_msg = "update!"
    
    
