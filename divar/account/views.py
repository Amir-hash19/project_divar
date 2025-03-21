from django.shortcuts import render, redirect
from django.http.response import HttpResponse, FileResponse
import os
import json
from account.models import Account
from django.views.decorators.csrf import csrf_exempt


def home_view(request):
    return render(request, "account/base.html")



def download_file(request):
    file = os.path.join("/home/amirykta/Desktop/projects/divar/divar/account/cookies.pdf")
    return FileResponse(
        open(file, "rb"),
        as_attachment=True
    )
    

@csrf_exempt
def register_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        created_user = Account.objects.create(
            username = data.get("username"),
            email = data.get("email"),
            mobile = data.get("mobile"),
        )
        return HttpResponse(f"{created_user.id} User created succesfully")
    
    