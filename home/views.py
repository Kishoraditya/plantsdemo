from django.http import JsonResponse
from django.conf import settings
from .models import Plant, LandingPage
from .firebase import get_firebase_app
from django.shortcuts import render
from firebase_admin import storage
import json
from firebase_admin import credentials, db

def landing_page(request):
    page = LandingPage.objects.first()

    if request.method == 'POST':
        
        plant_name = request.POST.get('plant-name')
        plant_description = request.POST.get('plant-description')
        plant_location = request.POST.get('plant-location')
        plant_image = request.FILES.get('plant-image')

        # Upload the image to Firebase Storage
        firebase_app = get_firebase_app()
        bucket = storage.bucket(name='plantsdemo-6bb9b.appspot.com')
        blob = bucket.blob(plant_image.name)
        blob.upload_from_file(plant_image)
        image_url = blob.public_url

        # Save the plant data to the database
        plant = Plant.objects.create(
            name=plant_name,
            description=plant_description,
            location=plant_location,
            image_url=image_url
        )
        plant_object = {
            'name': plant_name,
            'description': plant_description,
            'location': plant_location,
            'image_url': image_url
        }
        # Store the plant object in Firebase Realtime Database
        #database = db.reference()
        database = firebase_app.database()
        plants_ref = database.ref('plants')
        plants_ref.push(plant_object)
        
        data = database.child('plants').get()
        print(data)

        return JsonResponse({'message': 'Plant data saved successfully'})

    return render(request, 'home/landing_page.html', {'page': page})