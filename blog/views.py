from django.shortcuts import render
from rest_framework.response import Response
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from .models import Post

# Create your views here.

class PostView(APIView):
    def get(self, request):
        posts = [model_to_dict(post) for post in Post.objects.all()]
        for pst in posts:
            date = dateFormatter(str(pst['date_posted']).split(' ')[0])
            pst['date_posted_str'] = date
            pst['date_posted'] = str(pst['date_posted'])[:10]
        print(posts[0]['date_posted'])
        return Response(posts)
    
def dateFormatter(date):
    months = {
        '01': 'January',
        '02': 'February',
        '03': 'March',
        '04': 'April',
        '05': 'May',
        '06': 'June',
        '07': 'July',
        '08': 'August',
        '09': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December',
    }
    d = date.split('-')
    if d[2][0] == '0':
        d[2] = d[2][1:]
    return f"{d[2]} {months[d[1]]}, {d[0]}"