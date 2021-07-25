
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from .models import User, Store, Inventory, Transactions, Register, Movement, Cashierlog, Reciept
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db import IntegrityError
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.core.files.images import ImageFile
from django.template.loader import render_to_string
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers
import json
import traceback
import sys
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def login_pos(request):
    return render(request, "pos_login.html")
@csrf_exempt
def lookup_name(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            items = Inventory.objects.filter(title__contains=name)
            if items:
                data = serializers.serialize("json", items)
                return HttpResponse(data)
            else:
                x = {"status": "empty"}
                data = json.dumps(x)
                return HttpResponse(data)
        except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                x = {"status": message}
                data = serializers.serialize("json", x)
                return HttpResponse(data)
    x = {"status": "failed2"}
    data = json.dumps(x)
    return HttpResponse(data)

@csrf_exempt
def rec_lookup(request):
    if request.method == "POST":
        data = json.loads(request.body)
        transaction = Transactions.objects.get(pk = data.get("reciept"))
        try:
            if transaction:
                return JsonResponse(transaction.serialize())
            else:
                x = {"status": "No Transaction Found"}
                data = json.dumps(x)
                return HttpResponse(data)
        except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                x = {"status": message}
                data = json.dumps(x)
                return HttpResponse(data)
    return

@csrf_exempt
def checkout(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user = User.objects.get(pk=request.user.id)
            cashier = data.get("cashier")
            register = data.get("register")
            reciept = data.get("reciept")
            reciept = Reciept.objects.create( text = reciept)
            total = data.get("total")
            itemlist = data.get("items")
            store = Store.objects.get(pk = data.get("store"))
            transaction = Transactions.objects.create( store = store, cashier = user, register = register, status = "valid", total = total)
            transaction.reciept.add(reciept)
            for upc in itemlist:
                newitem = Inventory.objects.get(barcode=upc)
                transaction.items.add(newitem)
            x = {"status": "Successful"}
            data = json.dumps(x)
            return HttpResponse(data)
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            x = {"status": message}
            data = json.dumps(x)
            return HttpResponse(data)
    x = {"status": "failed2"}
    data = json.dumps(x)
    return HttpResponse(data)

def pos_register(request, store):
    set_store = Store.objects.get(name = store)
    return render(request, "pos.html", {
    "Store": set_store
    })
@csrf_exempt
def lookup(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            upc = data.get("upc")
            item = Inventory.objects.get(barcode=upc)
            x = {"name": item.title, "price": item.price, "tax": item.tax, "discription": item.discription, "upc": item.barcode}
            data = json.dumps(x)
            return HttpResponse(data)
        except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                x = {"status": message}
                data = json.dumps(x)
                return HttpResponse(data)
    x = {"status": "failed2"}
    data = json.dumps(x)
    return HttpResponse(data)
def create_item(request, store):
    if request.method == "POST":
        try:
            set_store = Store.objects.get(name = store)
            new_item = Inventory.objects.create(status = request.POST["status"], barcode = request.POST["barcode"], title = request.POST["title"], image = request.POST["image"], discription = request.POST["discription"], tax = request.POST["tax"], price = request.POST["price"], store = set_store)
            new_item.save()
            return render(request, "inventory.html", {
            "Store": set_store, "Inventory": set_store.items.all(), "Message": "successful"
            })
            x = {"status": "successful"}
            return HttpResponse(x)
        except Exception as ex:
                template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                message = template.format(type(ex).__name__, ex.args)
                x = {"status": message}
                data = json.dumps(x)
                return HttpResponse(data)
    x = {"status": "failed"}
    data = json.dumps(x)
    return HttpResponse(data)
def store_settings(request, store, setting = "null" ):
    set_store = Store.objects.get(name = store)
    if not setting == "null":
        if setting == "Transactions":
            return render(request, "transactions.html", {
            "Store": set_store, "Transactions": set_store.transactions.all()
            })
        if setting == "Staff":
            return render(request, "staff.html", {
            "Store": set_store, "Staff": set_store.cashiers.all()
            })
        if setting == "Cashlog":
            return render(request, "cashlog.html", {
            "Store": set_store, "Cashlog": set_store.cashlog.all()
            })
        if setting == "Items":
            return render(request, "item_management.html", {
            "Store": set_store, "Items": Inventory.objects.all()
            })
        if setting == "Inventory":
            return render(request, "inventory.html", {
            "Store": set_store, "Inventory": set_store.items.all()
            })
    return render(request, "settings.html", {"Store": set_store})

@csrf_exempt
def settings_functions(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        if data.get('status') == "new_reciept":
            try:
                transaction = Transactions.objects.get(pk= data.get("t_id"))
                reciept = data.get("reciept")
                reciept = Reciept.objects.create(text = reciept)
                transaction.reciept.add(reciept)
                if transaction.status == "valid":
                    transaction.status = "1/R"
                else:
                    r_count = int(transaction.status.replace("/R", ""))
                    r_count = 1 + r_count
                    transaction.status = str(r_count)+"/R"
                transaction.save()
                x = {"status": "successful"}
                data = json.dumps(x)
                return HttpResponse(data)
            except Exception as ex:
                    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(ex).__name__, ex.args)
                    x = {"status": message}
                    data = json.dumps(x)
                    return HttpResponse(data)
        up_user = User.objects.get(pk= data.get('staff_id'))
        if data.get('status') == "update_staff":
            try:
                up_user.first_name = data.get('firstname')
                up_user.last_name = data.get('lastname')
                up_user.position = data.get('position')
                up_user.email = data.get('email')
                up_user.dob = data.get('dob')
                up_user.username = data.get('username')
                up_user.save()
                x = {"status": "successful"}
                data = json.dumps(x)
                return HttpResponse(data)
            except Exception as ex:
                    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
                    message = template.format(type(ex).__name__, ex.args)
                    x = {"status": message}
                    data = json.dumps(x)
                    return HttpResponse(data)
        if data.get('status') == "update_pswd":
            up_user.password = data.get('pin')
            up_user.save()
            if up_user.password == data.get('pin'):
                x = {"status": "successful"}
                data = json.dumps(x)
                return HttpResponse(data)
        if data.get('status') == "delete_user":
            up_user.delete()
            x = {"status": "successful"}
            data = json.dumps(x)
            return HttpResponse(data)
    x = {"status": "Failed"}
    data = json.dumps(x)
    return HttpResponse(data)

def stores(request, create = 0):
    user = User.objects.get(pk=request.user.id)
    if create:
        if create == 3:
            store = Store.objects.create(name = request.POST["store_name"], user = user )
            store.save()
    stores_list = user.stores.all()
    return render(request, "stores.html", {
            "Stores": stores_list
                })

def index(request):
    return render(request, "index.html")
def profile(request):
    user = User.objects.get(pk=request.user.id)
    return render(request, "profile.html", {
            "status": "Active", "membership": user.get_level_display(), "manager": user.first_name+" "+user.last_name , "stores": user.stores.all()
        })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
def register_cashier (request, store):
    if request.method == "POST":
        company = request.POST["company"]
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        position = request.POST["Position"]
        # Ensure password matches confirmation
        password = request.POST["pin"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, dob = request.POST["dob_date"])
            user.first_name = firstname
            user.last_name = lastname
            user.position = position
            user.company = company
            user.save()
            store_c = Store.objects.get(name = store.replace("_", " "))
            store_c.cashiers.add(user)
        except IntegrityError:
            return store_settings(request, store, setting = "Staff" )
    return store_settings(request, store, setting = "Staff" )

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        company = request.POST["companyname"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, dob = request.POST["dob_date"])
            user.first_name = firstname
            user.last_name = lastname
            user.position = 9
            user.company = company
            user.level = 3
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return render(request, "profile.html", {
            "status": "Active", "membership": user.level, "manager": user.full_name , "stores": user.stores.all()
        })
    else:
        return render(request, "register.html")
