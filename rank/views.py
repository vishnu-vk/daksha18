from django.shortcuts import render
from . models import Point,Result, Registration
from . forms import RegistrationForm
import csv
from django.http import HttpResponse

# Create your views here

def index(request):
	return render(request, 'index.html')

def event(request):
		return render(request, 'events.html')

def team(request):
		return render(request, 'team.html')

def register_page(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			new_data = form.save()
			return render(request, 'rank/register_success.html')
	else:
		form = RegistrationForm()
	return render(request, 'rank/register.html', {'form':form})


def score_view(request):

	queryset = Point.objects.all()
	context = {"score" : queryset }

	return render(request,"score.html",context)


#new
def result_view(request, name):

	queryset = Result.objects.all()
	context = {"result" : queryset }

	return render(request,"result_view.html",context)

def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="users.csv"'

    writer = csv.writer(response)
    writer.writerow(['full_name', 'year', 'department', 'phone', 'events'])

    lists = Registration.objects.all().values_list('full_name', 'year', 'department', 'phone', 'events')
    for entry in lists:
        writer.writerow(entry)

    return response
