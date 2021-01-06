from django.shortcuts import render
from .apps import PredictorConfig
from django.http import JsonResponse
from rest_framework.views import APIView
from  .models import *
from django.contrib import messages

#class call_model(APIVIew):
def image(request):
    if request.method == 'POST':
        img = request.POST['file'] 

        if img is not None:
            
            img = Info(image=img)
            img.save()
            messages.success(request, 'Image Uploaded! Press Go!')
            return render(request, 'index.html')
        
        else:
            return render(request, 'index.html')


    return render(request, 'index.html')  

def get(self, request):
        if request.method   == 'GET':

            #get sound ftom request
            sound = request.GET.get('sound')

            #vectorize sound
            vector = PredictorConfig.vectorizer.transform([sound])

            #predict based on vector
            prediction = PredictorConfig.regressor.predict(vector)[0]

            #build response
            response = {'dog': prediction}

            #return response
            return JsonResponse(response) 
            #zfz
        