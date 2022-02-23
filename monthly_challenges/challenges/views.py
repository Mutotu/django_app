from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect, response
from django.urls import reverse

monthly_challenges = {
    "january":"january, Django",
    "february":"february, Dondon",
    "march":"march, Gym",
    "april":"april, Bootcamp",
    "may":"may, Flask",
    "june":"june, Chef",
    "july":"july, Algorithm",
    "august":"august, Jobs",
    "september":"september, Indeed",
    "october":"october, Linkedin",
    "november":"november, Python",
    "december": "december, JavaScript"
}
# Create your views here.


# def index(request):
#     return HttpResponse("This works")
# def feb(request):
#     return HttpResponse('This is Feb')

# def monthly_challenge_by_number(request, month):
#     return HttpResponse(month)


# def monthly_challenge(request, month):
#     challenge_text = None
#     if month == 'january':
#         challenge_text = "january"
#     elif month == 'february':
#         challenge_text = 'february'
#     elif month == 'march':
#         challenge_text = 'march'    
#     else:
#         return HttpResponseNotFound("Not that month")
        
#     return HttpResponse(challenge_text)
  ############  
  
  
  
def index(request):
    # response_data = "<ul><li><a href='/challenges/january'>January</a></li></ul>"
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{month.capitalize()}</></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)
  
def monthly_challenge_by_number(request, month):
    # take the keys of monthly_challenges and make it a list
    months = list(monthly_challenges.keys())
    # chekc to see if month is greated than the length of months 
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    forward_month = months[month - 1]
    # the purpose here is that the number (month) comes in as int and then we use it to 
    # look for that number in the list if it mathces than redirect it using HttpResponseRedirect()
    redirect_path = reverse("month-challenge", args=[forward_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)
    
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("Not that month")
#########
