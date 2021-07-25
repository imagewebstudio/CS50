from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
import json
from .models import User, Listing, Category, Bid, Comment

def update_items():
    today = timezone.now()
    try:
        items = Listing.objects.all().filter(ends__year=today.year, ends__month=today.month, ends__day=today.day)
    except ObjectDoesNotExist:
        return
    for item in items:
        item.active = 'no'
        try:
            winingbid = item.bids.latest('id')
            winner = winingbid.user
            item.winningbidder = winner
            item.save()
        except:
            item.save()
def end_auction(request):
    item = Listing.objects.get(pk = json.load(request)['item_id'])
    wish = item.wishlist.all()
    comments = Comment.objects.all().filter(listing = item)
    bids = Bid.objects.all().filter(listing = item)
    creator = item.creator
    item.ends = timezone.now()
    item.save()
    return render(request, "auctions/item/item.html",
    {"Item": item, "itemwish": wish, "comments": comments, "Bids": bids, "message": "1"})


def viewcart(request):
    user = request.user
    return render(request, "auctions/index.html",
    { "ItemWon": Listing.objects.all().filter(winningbidder=user)})

def index(request):
    update_items()
    return render(request, "auctions/index.html",
    { "Listing": Listing.objects.all().filter(active="yes")})

def viewitem(request, item_id):
    update_items()
    item = Listing.objects.get(pk = item_id)
    wish = item.wishlist.all()
    comments = Comment.objects.all().filter(listing = item)
    bids = Bid.objects.all().filter(listing = item).order_by('price')
    creator = item.creator
    return render(request, "auctions/item/item.html",
    { "Item": item, "itemwish": wish, "comments": comments, "Bids": bids.reverse(), "Creator": creator} )

def wish(request):
    user = User.objects.get(pk=request.user.id)
    item = Listing.objects.get(pk = json.load(request)['item_id'])
    wish = item.wishlist.all()
    if user in wish:
        user.wishlist.remove(item)
        x = { "wish": "not"}
        data = json.dumps(x)
        return HttpResponse(data)
    else:
        user.wishlist.add(item)
        x = { "wish": "made"}
        data = json.dumps(x)
        return HttpResponse(data)

def newcomment(request):
    if request.method == "POST":
        newcomment = request.POST["comment"]
        itemid = request.POST["Item_id"]
        item = Listing.objects.get(pk=itemid)
        user = request.user
        Comment.objects.create(user=user, text= newcomment, listing= item )
        return viewitem(request, itemid)



def newbid(request):
    user = request.user
    bid = request.POST["bidnumber"]
    itemid = request.POST["item_id"]
    item = Listing.objects.get(pk=itemid)
    wish = item.wishlist.all()
    comments = Comment.objects.all().filter(listing = item)
    bids = Bid.objects.all().filter(listing = item).order_by('price')
    try:
        bid = int(bid)
    except ValueError:
        return render(request, "auctions/item/item.html",
        {"Item": item, "itemwish": wish, "comments": comments, "Bids": bids.reverse(), "message": "VALUE ERROR: You must enter a  valid number/integer."})
    try:
        currentbid = Bid.objects.filter(listing= item).latest('id')
    except ObjectDoesNotExist:
        if bid >= item.startprice:
            Listing.objects.filter(pk=itemid).update(currentprice=bid)
            Bid.objects.create(price=bid, listing= item, user= user)
            return render(request, "auctions/item/item.html",
            {"Item": item, "itemwish": wish, "comments": comments, "Bids": bids.reverse(), "message": "success"})
        return render(request, "auctions/item/item.html",
        {"Item": item, "itemwish": wish, "comments": comments, "Bids": bids.reverse(), "message": "ERROR: Bid must be greater or equal to starting price."})
    if bid > currentbid.price:
        Listing.objects.filter(pk=itemid).update(currentprice=bid)
        Bid.objects.create(price=bid, listing= item, user= user)
        return render(request, "auctions/item/item.html",
        {"Item": item, "itemwish": wish, "comments": comments, "Bids": bids.reverse(), "message": "success"})
    return render(request, "auctions/item/item.html",
    {"Item": item, "itemwish": wish, "comments": comments, "Bids": bids.reverse(), "message": "UNKNOWN ERROR: Could not place bid. Bid must be a number greater then current bid." })

def catpage(request):
    Category.objects.all()
    return render(request, "auctions/index.html",
    {"Catpage": Category.objects.all()})


def viewcat(request, catname):
    items = Listing.objects.all().filter(active="yes", category=catname)
    count = items.count
    return render(request, "auctions/index.html",
    { "Listing":items , "thiscat":count})

def newitem(request):
    if request.method == "POST":
        newlisting = Listing.objects.get_or_create(title = request.POST["title"],
        image = request.POST["image"],
        creator = request.user,
        description = request.POST["description"],
        currentprice = request.POST["price"],
        startprice = request.POST["price"],
        ends = request.POST["End_date"])
        if newlisting:
            cat = Category.objects.get(pk = request.POST["cat"])
            lis = Listing.objects.get(title = request.POST["title"])
            cat.listings.add(lis)
            return render(request, "auctions/index.html",
            { "Listing": Listing.objects.all()})
        else:
            return render(request, "auctions/index.html",
            {"Category": Category.objects.all(), "message": "Item Item Creation failed"})
    else:
        return render(request, "auctions/index.html",
        {"Listing": Listing.objects.all()})

def newlisting(request):
    return render(request, "auctions/index.html",
    { "Category": Category.objects.all()})


def wishlist(request):
    user = request.user
    return render(request, "auctions/index.html",
            {"Wish": user.wishlist.all()})


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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."    })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
