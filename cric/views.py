from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Cricket 
import pickle
import pandas as pd

def dash(request):  
    return render(request,'dash.html')


def profile(request):
    return render(request,'profile.html')


def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect("home") 

        messages.error(request, "Invalid Username or Password")
        return redirect("login_page")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login_page")



def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Choose a different one.")
            return redirect("register")

        user = User.objects.create_user(
            first_name=first_name, last_name=last_name, username=username, password=password
        )  
        user.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect("login_page")  

    return render(request, "register.html")


def home(request):
    return render(request, "home.html")




def team(request):
    return render(request,'team.html')


def team_profile(request):
    return render(request,"team_profile.html")



try:
    with open('cric/pipe.pkl', 'rb') as model_file:
        pipe = pickle.load(model_file)
except FileNotFoundError:
    pipe = None


teams = [
    'Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa', 
    'England', 'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka'
]

cities = [
    'Colombo', 'Mirpur', 'Johannesburg', 'Dubai', 'Auckland', 'Cape Town', 
    'London', 'Pallekele', 'Barbados', 'Sydney', 'Melbourne', 'Durban', 
    'St Lucia', 'Wellington', 'Lauderhill', 'Hamilton', 'Centurion', 
    'Manchester', 'Abu Dhabi', 'Mumbai', 'Nottingham', 'Southampton', 
    'Mount Maunganui', 'Chittagong', 'Kolkata', 'Lahore', 'Delhi', 
    'Nagpur', 'Chandigarh', 'Adelaide', 'Bangalore', 'St Kitts', 'Cardiff', 
    'Christchurch', 'Trinidad'
]


def result(request):
    prediction = None
    error = None

    if request.method == 'POST':
        try:
            if not pipe:
                raise ValueError("Model file not found.")

            batting_team = request.POST.get('batting_team', '').strip()
            bowling_team = request.POST.get('bowling_team', '').strip()
            city = request.POST.get('city', '').strip()

            current_score = request.POST.get('current_score', '').strip()
            overs = request.POST.get('overs', '').strip()
            wickets = request.POST.get('wickets', '').strip()
            last_five = request.POST.get('last_five', '').strip()

            # Check for missing fields
            required_fields = [batting_team, bowling_team, city, current_score, overs, wickets, last_five]
            if any(not field for field in required_fields):
                error = 'All fields are required.'
            elif not (current_score.isdigit() and overs.replace('.', '', 1).isdigit() and 
                      wickets.isdigit() and last_five.isdigit()):
                error = 'Invalid input: Please enter valid numbers.'
            else:
                current_score = int(current_score)
                overs = float(overs)
                wickets = int(wickets)
                last_five = int(last_five)

                if overs == 0:
                    error = 'Invalid input: Overs cannot be zero.'
                else:
                    balls_left = 120 - (overs * 6)
                    wickets_left = 10 - wickets
                    crr = current_score / overs

                    input_df = pd.DataFrame({
                            'batting_team': [batting_team],
                            'bowling_team': [bowling_team],
                            'city': [city],
                            'current_score': [current_score],
                            'balls_left': [balls_left],
                            'wicket_left': [wickets_left],  # Changed from 'wickets_left'
                            'current_run_rate': [crr],  # Changed from 'crr'
                            'last_five': [last_five]
                    })

                    result = pipe.predict(input_df)
                    prediction = int(result[0])

        except Exception as e:
            error = f'An error occurred: {e}'

    return render(request, 'index.html', {
        'teams': sorted(teams), 'cities': sorted(cities),
        'prediction': prediction,
        'error': error
    })


