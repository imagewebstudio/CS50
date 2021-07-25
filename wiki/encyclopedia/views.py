import re
from django.core import serializers
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from . import util
import cgi
import difflib
import random
import markdown2
import html2markdown
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import json

def EntryPage(request, name):
    if util.get_entry(name):
        content = markdown2.markdown(util.get_entry(name))
        return render(request, "encyclopedia/index.html", {
            "entrycontent": content, 'etitle': name
            })
    else:
        return render(request, "encyclopedia/index.html", {
            "errorcode": 2, "entries": util.list_entries()
            })
def newEntry(request):
    return render(request, "encyclopedia/index.html", {
        "newentry": 1
    })

def saveEntry(request):
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = request.POST
        check = util.get_entry(form['title'])
        content = html2markdown.convert("<h1>"+form['title']+"</h1>"+"<p>"+form['content']+"</p>")
        title = form['title']
        if check == None:
            util.save_entry(title, content)
            return render(request, "encyclopedia/index.html", {
                "entrycontent": markdown2.markdown(util.get_entry(form['title'])), "errorcode": 3
                })
        return render(request, "encyclopedia/index.html", {
            "errorcode": 1, "etitle": form['title']
        })

def editC(request):
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
        etitle = request.POST.get('title')
        content = util.get_entry(etitle)
        return render(request, "encyclopedia/index.html", {
            "entrycontent": content , "revise": 1, "etitle": etitle,
            })


def updateEntry(request):
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
    # create a form instance and populate it with data from the request:
        form = request.POST
        title = form['title']
        contentf = form['contentf']
        util.save_entry(title, contentf)
    return EntryPage(request, form['title'])


def randomEntry(request):
    entries = util.list_entries()
    count = len(entries)
    return redirect('/'+entries[random.randint(0,count-1)])

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def Entrylookup(request):
    if request.method == 'GET':
        return redirect('/')
    elif request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = request.POST
        results = []

        name = form['entryname']
        if util.get_entry(name) == None:
            entries = util.list_entries()
            results = []
            for i in range(len(entries)-1):
                current_e = entries[i].replace(" ", "")
                if name.lower() in current_e.lower():
                    results.append(entries[i])
            return render(request, "encyclopedia/index.html", {
                "entrycontent": results, "results": 1, "errorcode": 4, "lname":name
            })

        else:
            return redirect('/'+name)
