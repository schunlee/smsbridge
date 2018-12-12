import json

from django.http import HttpResponse

# Create your views here.
from .models import Message


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def add_sms_message(request):
    if request.method == "POST":
        try:
            title = request.POST.get('title', '')
            description = request.POST.get('desp', '')
            q = Message.objects.create(title=title, desp=description)
            q.save()
        except Exception, msg:
            resp = {'status': 500, 'detail': msg}
        else:
            resp = {'status': 200, 'detail': 'Get success'}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        resp = {'status': 504, 'detail': 'Method not valid'}
        return HttpResponse(json.dumps(resp), content_type="application/json")


@csrf_exempt
def get_sms_message(request):
    if request.method == "GET":
        try:
            results = list()
            queryset = Message.objects.all()
            for msg in queryset:
                import datetime
                # datetime.datetime.strftime()
                results.append({"title": msg.title,
                                "desp": msg.desp,
                                "msg_date": msg.msg_date.date().strftime("%Y-%m-%d")})
        except Exception, msg:
            pk = msg
            resp = {'status': 500, 'detail': msg}
        else:
            resp = {'status': 200, 'detail': results}
        return HttpResponse(json.dumps(resp), content_type="application/json")
