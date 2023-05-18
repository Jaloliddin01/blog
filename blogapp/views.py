from blog.models import Post
from django.views.generic import ListView, TemplateView

# Views
# About Page
class AboutView(TemplateView):
    template_name = "about.html"

# Posts Page
class PostListView(ListView):
    model = Post
    template_name = 'posts.html'

#additions
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


