from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from .models import GarbageCollectionRequests, Garbages, GarbageVault
from .forms import GarbageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import datetime


# user transactions 

@login_required(login_url="SignIn")
def request_collection(request):
    requs = GarbageCollectionRequests.objects.filter(collection_status = False, requested_by = request.user)
    if request.method == "POST":
        req = GarbageCollectionRequests(requested_by = request.user)
        req.save()
        return redirect("add_items_to_request", pk= req.id)
    return render(request,"request_collection.html", context={"requs":requs})

def add_items_to_request(request, pk):
    req = get_object_or_404(GarbageCollectionRequests,id =pk)
    garbages = req.garbage_request.all()
    form = GarbageForm()
    if request.method == "POST":
        form = GarbageForm(request.POST)
        if form.is_valid():
            garbage = form.save(commit=False)
            garbage.request = req
            garbage.save()
            messages.success(request, "item added to request")
            return redirect("add_items_to_request", pk = pk)
        else:
            messages.error(request, "Something wrong")
            return redirect("add_items_to_request", pk = pk)


    context = {
        "req":req,
        "form":form,
        "garbages":garbages
    }
    return render(request, 'add_items_to_request.html',context)


def delete_garbage_from_request(request,pk):
    garbage = get_object_or_404(Garbages, id = pk)
    req_id = garbage.request.id

    garbage.delete()
    messages.success(request, "garbage deleted....")
    return redirect("add_items_to_request", pk = req_id)


def history(request):
    req = GarbageCollectionRequests.objects.filter(requested_by = request.user, visibility = False)
    context ={
        "req":req
    }
    return render(request,"history.html",context)

def my_requests(request):
    req = GarbageCollectionRequests.objects.filter(requested_by = request.user, collection_status = True, visibility = True)
    context ={
        "req":req
    }
    return render(request,"myrequests.html",context)




# admin fuctions

def collection_requests_admin(request):
    req = GarbageCollectionRequests.objects.all()
    context = {"req":req}
    return render(request,"admin/collection_requests.html",context)

def view_collection_request_single(request,pk):
    req = get_object_or_404(GarbageCollectionRequests,id =pk)
    drivers = User.objects.filter(groups__name= "driver")
    garbages = req.garbage_request.all()
    context = {
        "req":req,
        "garbages":garbages,
        "drivers":drivers
    }
    return render(request,"admin/single_request.html",context)


def assign_driver(request,pk):
    req = get_object_or_404(GarbageCollectionRequests,id =pk)
    if request.method == "POST":
        driver = request.POST["driver"]
        date = request.POST["datetime"]

        req.driver = get_object_or_404(User, id=driver)
        req.collection_date_time = date
        req.garbage_status = "driver assigned"
        req.updated_staff = request.user
        req.save()

        messages.success(request,"Driver assigned for collection")
        return redirect(view_collection_request_single, pk = pk )
    

def vault_admin(request):
    vault = GarbageVault.objects.all()
    if request.method == "POST":
        vaultname = request.POST["vault"]
        cat = request.POST["garbage_category"]
        va = GarbageVault(
            vault_name = vaultname,
            garbage_category = cat
        )
        va.save()
        messages.success(request,"Vault Created")
        return redirect("vault_admin")
    context = {
        "vault":vault
    }
    return render(request,'admin/vault.html',context)


# driver functionalities 
@login_required(login_url="SignIn")
def driver_collection_requests(request):
    req = GarbageCollectionRequests.objects.filter(driver = request.user, collection_status = False).order_by("collection_date_time")

    context = {
        "req":req
    }
    return render(request, "staff/collection_request_driver.html",context)


def driver_collected_garbages(request):
    req = GarbageCollectionRequests.objects.filter(driver = request.user, collection_status = True,visibility=True).order_by("collection_date_time")

    context = {
        "req":req
    }
    return render(request, "staff/collected_driver.html",context)


def mark_collection_in_progress(request,pk):
    req = get_object_or_404(GarbageCollectionRequests, id = pk)
    req.garbage_status = "in_progress"
    req.save()
    return redirect("driver_collection_requests")


def mark_collection_collected(request,pk):
    req = get_object_or_404(GarbageCollectionRequests, id = pk)
    req.garbage_status = "collected"
    req.collected_time = datetime.datetime.now()
    req.collection_status = True
    req.save()
    return redirect("driver_collection_requests")

from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import F

def send_to_vault(request, pk):
    # Get the GarbageCollectionRequest instance
    garbage_request = get_object_or_404(GarbageCollectionRequests, id=pk)
    
    # Get all garbage items associated with the request
    garbages = Garbages.objects.filter(request=garbage_request)
    
    for garbage in garbages:
        category = garbage.garbage_item
        weight = garbage.weight
        
        # Check if a vault exists for the category
        vaults = GarbageVault.objects.filter(garbage_category=category)
        
        if vaults.exists():
            # Randomly select one vault to add the weight
            vault = vaults.order_by('?').first()
            vault.total_weight = F('total_weight') + weight
            vault.save()
        else:
            # Create a new vault if none exists
            GarbageVault.objects.create(
                vault_name=f"{category.capitalize()} Vault {GarbageVault.objects.filter(garbage_category=category).count() + 1}",
                garbage_category=category,
                total_weight=weight
            )
    
    # Update garbage collection request status
    garbage_request.garbage_status = 'recycled'
    garbage_request.visibility =False
    garbage_request.save()

    messages.success(request, "Garbage successfully sent to the vaults.")
    return redirect('driver_collection_requests')  # Redirect to request details page or any appropriate view



# staff functions

def collection_requests_staff(request):
    req = GarbageCollectionRequests.objects.all()
    context = {"req":req}
    return render(request,"staff/collection_requests.html",context)

def view_collection_request_single_staff(request,pk):
    req = get_object_or_404(GarbageCollectionRequests,id =pk)
    drivers = User.objects.filter(groups__name= "driver")
    garbages = req.garbage_request.all()
    context = {
        "req":req,
        "garbages":garbages,
        "drivers":drivers
    }
    return render(request,"staff/single_request.html",context)


def assign_driver_staff(request,pk):
    req = get_object_or_404(GarbageCollectionRequests,id =pk)
    if request.method == "POST":
        driver = request.POST["driver"]
        date = request.POST["datetime"]

        req.driver = get_object_or_404(User, id=driver)
        req.collection_date_time = date
        req.garbage_status = "driver assigned"
        req.updated_staff = request.user
        req.save()

        messages.success(request,"Driver assigned for collection")
        return redirect(view_collection_request_single_staff, pk = pk )
    