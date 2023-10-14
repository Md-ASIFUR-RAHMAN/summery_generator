from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from imgtotext.noun_verb import extract_dialogue_info_from_image
from io import BytesIO
from PIL import Image
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files import File
import os

# Create your views here.

def Home(request):

    return render(request,'base.html')


def image_compress_save(image, img_name):
    im = Image.open(image)  # or self.files['image'] in your form
    # destroy color pew pew
    im = im.convert('RGB')
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    compressed_image = File(im_io, name=img_name)
    FileSystemStorage(location=os.path.join(settings.STATICFILES_DIRS[0], 'UPLOAD')).save(img_name,
                                                                                                    compressed_image)
def Collect_noun_and_verb(request):

    if request.method == 'GET':
        return render(request, 'image_upload_page.html')
    if request.method == 'POST':

        converted = 'converted.jpg'

        image_compress_save(request.FILES['image'],converted)


        result_dict = extract_dialogue_info_from_image("C:/Users/asifu/OneDrive/Desktop/ocr_python/summery/static/UPLOAD/converted.jpg")
        print(result_dict)

        return HttpResponse("Collected")
