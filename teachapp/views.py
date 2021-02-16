from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import SignUpForm
from .models import Teachers

from django.http import JsonResponse, HttpResponse

import pandas as pd
import csv
import json
import os

# Create your views here.

def home(request):
    return render(request, 'home.html')

def teachers_list(request, *args, **kwargs):
    search = request.GET.get('search[value]')
    draw = int(request.GET.get('draw', 0))
    length = int(request.GET.get('length', 10))
    start = int(request.GET.get('start', 0))
    teachers = Teachers.objects.all()
    if search:
        teachers = Teachers.objects.filter(Q(first_name__istartswith=search)| Q(subject_taught__icontains=search))
    total = teachers.count()

    queryset = teachers[start:start+length]
    context={"data":list(queryset.values()), "recordsTotal":total, "recordsFiltered": total}
    return JsonResponse(context)

def profile(request, id):
    teacher = get_object_or_404(Teachers, id=id)
    subjects_taught = teacher.subject_taught
    subjects = subjects_taught.split(",")
    context = {"teacher": teacher, "subjects": subjects}
    return render(request, 'profile.html', context)


def populate(request):
    if Teachers.objects.all():
        return redirect('/teachers/home')
    df = pd.read_csv(os.path.join(os.getcwd(),"Teachers.csv"))
    print(df)
    # to remove empty NaN rows
    df=df.dropna()
    # Adds a column  M1_list forming a list of elements
    df['M1_list'] = df['Subjects taught'].apply(lambda x: x.split(","))
    # Adds a column count giving the number of subjects
    df['count']=df.M1_list.str.len()
    df = df[df['count'] <= 5]
    # drops the columns M1_list, count
    df.drop(["M1_list", "count"], axis = 1, inplace = True)
    row_iter = df.iterrows()
    objs = [Teachers(
        first_name = row['First Name'],
        last_name = row['Last Name'],
		profile_picture = row['Profile picture'],
        email_address  = row['Email Address'],
        phone_number = row['Phone Number'],
        room_number  = row['Room Number'],
        subject_taught = row['Subjects taught']
    )
    for index, row in row_iter
    ]
    Teachers.objects.bulk_create(objs)
    return redirect('/teachers/home')

@login_required
def csv_database_write(request):

    # Get all data from UserDetail Databse Table
    teachers = Teachers.objects.all()

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="teachers_directory.csv"'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name', 'Profile picture',
	 'Email Address', 'Phone Number', 'Room Number', 'Subjects Taught'])

    for teacher in teachers:
        writer.writerow([teacher.first_name, teacher.last_name, check(teacher.profile_picture), teacher.email_address,
		teacher.phone_number, teacher.room_number, teacher.subject_taught])
    return response


def check(profile_picture):
	if profile_picture=='default_teacher.png':
		return ' '
	return profile_picture

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/teachers/home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
