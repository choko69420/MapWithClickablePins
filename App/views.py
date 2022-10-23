from django.shortcuts import render

# Create your views here.
from .models import Post, Pin
import json


def pin_to_str(pin):
    return f'{pin.latitude},{pin.longitude}'


def index(request):
    if request.method != 'GET':
        pass

    pins = Pin.objects.all()
    # jsonify pins
    pins = [pin.serialize() for pin in pins]
    pins = json.dumps(pins)
    context = {
        'pins': pins,
    }
    return render(request, 'App/index.html', context)
