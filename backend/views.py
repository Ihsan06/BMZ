from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
# from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
# from django.contrib.auth.decorators import login_required

from .models import User, Project, Country, Country_New, Country_Change, Project_New


# Create your views here.


def index(request):
    return render(request, 'backend/index.html', {
        "countries": Country.objects.all(),
        "projects": Project.objects.all(),

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
            return render(request, "backend/login.html", {
                "message": "Invalid username and/or password."
            })

    else:
        return render(request, "backend/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Passwort muss matchen
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "backend/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "backend/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "backend/register.html")


def country_management(request):
    return render(request, 'backend/country.html', {
        "countries": Country.objects.all()
    })


def new_country(request):
    if request.method == "POST":
        form = Country_New(request.POST)
        if form.is_valid():
            try:
                form.save()
                return render(request, "backend/country.html", {
                    "form": form,
                    "message_country": "Land erfolgreich angelegt."
                })

            except IntegrityError:
                return render(request, "backend/country.html", {
                    "message_country": "Land bereits vergeben."
                })


def change_country(request):
    if request.method == "POST":
        Country.objects.filter(id=request.POST['id']).update(country_name=request.POST['country_name'])
        Country.objects.filter(id=request.POST['id']).update(iso_code=request.POST['iso_code'])
        return render(request, "backend/country.html", {
            "countries": Country.objects.all(),
            "message_country": "Land erfolgreich angelegt."
        })


def new_project(request):
    if request.method == "POST":
        form = Project_New(request.POST)
        form.save()
        return render(request, "backend/index.html", {
            "countries": Country.objects.all(),
            "form": form,
            "message_project": "Projekt erfolgreich angelegt."
        })


def change_project(request):
    if request.method == "POST":
        Project.objects.filter(id=request.POST['id']).update(country_name=request.POST['project_name'])
        Project.objects.filter(id=request.POST['id']).update(iso_code=request.POST['description'])
        Project.objects.filter(id=request.POST['id']).update(iso_code=request.POST['country'])
        Project.objects.filter(id=request.POST['id']).update(iso_code=request.POST['start_project'])
        Project.objects.filter(id=request.POST['id']).update(iso_code=request.POST['end_project'])
        Project.objects.filter(id=request.POST['id']).update(iso_code=request.POST['budget_project'])
        Project.objects.filter(id=request.POST['id']).update(iso_code=request.POST['spend_budget_project'])

        return render(request, "backend/index.html", {
            "projects": Project.objects.all(),
            "message_project": "Projekt erfolgreich geändert."
        })


