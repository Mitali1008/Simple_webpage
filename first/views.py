from django.shortcuts import render
from first.models import photo_upload
from first.forms import photo_form
from first import views
# Create your views here.


def index(request):
    img = photo_upload.objects.all()
    return render(request, "first/home.html", {"img":img})

def upload_image(request):
    pic = request.FILES['image_load']
    print("loading..............")
    user = photo_upload(image=pic)
    user.save()
    img = photo_upload.objects.all()
    return render(request, "first/home.html", {"img":img})

    