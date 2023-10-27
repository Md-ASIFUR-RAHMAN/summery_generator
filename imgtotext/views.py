from django.shortcuts import render
from imgtotext.noun_verb import extract_dialogue_info_from_image,For_noun_verb_adj
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class SentenceAnalysisView(APIView):
    def post(self, request):
        sentence = request.data.get('sentence', '')

        nouns,adjectives,verbs = For_noun_verb_adj(sentence)

        analysis = {
            "sentence": sentence,
            "nouns": nouns,
            "adjectives": adjectives,
            "verbs": verbs,
        }
        return Response(analysis, status=status.HTTP_200_OK)


def Home(request):
    return render(request, 'base.html')

def Collect_noun_and_verb(request):
    if request.method == 'GET':
        return render(request, 'image_upload_page.html')

    if request.method == 'POST':
        if 'image' in request.FILES:
            uploaded_image = request.FILES['image']

            fs = FileSystemStorage(location=os.path.join(settings.STATICFILES_DIRS[0], 'UPLOAD'))
            saved_path = fs.save(uploaded_image.name, uploaded_image)

            result_dict = extract_dialogue_info_from_image(os.path.join(settings.STATICFILES_DIRS[0], 'UPLOAD', saved_path))

        return render(request, 'separate_results.html', {'dialogue_info': result_dict})