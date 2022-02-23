from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect

monthly_challenges = {
    "january":"january",
    "february":"february",
    "march":"march",
    "april":"april",
    "may":"may",
    "june":"june",
    "july":"july",
    "august":"august",
    "september":"september",
    "october":"october",
    "november":"november",
    "december": "december"
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
  
def monthly_challenge_by_number(request, month):
    # take the keys of monthly_challenges and make it a list
    months = list(monthly_challenges.keys())
    # chekc to see if month is greated than the length of months 
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    forward_month = months[month - 1]
    # the purpose here is that the number (month) comes in as int and then we use it to 
    # look for that number in the list if it mathces than redirect it using HttpResponseRedirect()
    return HttpResponseRedirect("/challenges/" + forward_month)
    
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Not that month")
#########
