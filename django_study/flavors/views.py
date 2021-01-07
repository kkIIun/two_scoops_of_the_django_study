from django.shortcuts import render
# from store.exceptions import OutOfStock,CorruptedDatabase
from django.db import transaction
from .models import Flavor
from django.views.generic import ListView,DetailView,UpdateView,CreateView
from django.shortcuts import reverse

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

class FlavorListView(ListView):
    model = Flavor
    context_object_name = 'tests'

    def get_queryset(self):
        return Flavor.objects.published()

class FlavorDetailView(DetailView):
    model = Flavor
    context_object_name = 'test'

# class FlavorResultsView(FlavorDetailView):
#     template_name = "tastings/detail.html"
    
# class FlavorUpdateView(UpdateView):

class FlavorCreateView(CreateView):
    model = Flavor
    fields = ('title','body')
    
    def get_success_url(self):
        return reverse("detail",
            kwargs={"pk": self.object.pk})
    
class FlavorUpdateView(UpdateView):
    model = Flavor
    fields = ('title','body')

    def get_success_url(self):
        return reverse("detail",
            kwargs={"pk": self.object.pk})