from django.shortcuts import render
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from .models import Lesson, Exercise

# Views
class LessonView(APIView):
    def get(self, request):
        lessons = [model_to_dict(lesson) for lesson in Lesson.objects.all()]
        for lsn in lessons:
            date = dateFormatter(str(lsn['date_posted']).split(' ')[0])
            lsn['date_posted_str'] = date
            lsn['date_posted'] = str(lsn['date_posted'])[:10]
        return Response(lessons)
        

class ExerciseView(APIView):
    def get(self, request):
        exercises = [model_to_dict(exercise) for exercise in Exercise.objects.all()]
        for exer in exercises:
            date = dateFormatter(str(exer['date_posted']).split(' ')[0])
            exer['date_posted_str'] = date
            exer['date_posted'] = str(exer['date_posted'])[:10]
        return Response(exercises)
    
# Additional funtions
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
