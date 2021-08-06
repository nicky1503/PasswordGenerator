from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, "generator/home.html")


def password(request):
    characters = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get("Uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get("numbers"):
        characters.extend(list('1234567890'))

    if request.GET.get("SpecialCharacters"):
        characters.extend(list("!@#$%&*+=-/|"))

    length = int(request.GET.get('length', 12))
    password = ''

    for x in range(length):
        password += characters[random.randrange(len(characters))]

    return render(request, "generator/password.html", {"password": password})

