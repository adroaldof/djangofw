from django.template.response import TemplateResponse
from datetime import datetime


def home(request):
    today = datetime.today()
    price = 43856.68
    return TemplateResponse(request, 'index.html', {
        'today': today,
        'price': price
    })
