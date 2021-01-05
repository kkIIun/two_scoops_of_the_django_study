from django.shortcuts import render
from store.exceptions import OutOfStock,CorruptedDatabase
from django.db import transaction

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
