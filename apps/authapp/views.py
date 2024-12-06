from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .middleware import decode_request
from django.utils.decorators import method_decorator
from models import User  # Make sure to import your User model correctly
import json

@method_decorator(decode_request, name='dispatch')
class AuthView(View):
    
    def get(self, request):
        # Query to retrieve all users
        # users = User.objects.all()  
        
        # # Convert the queryset to a list of dictionaries
        # users_list = []   
        # for user in users:
        #     users_list.append({
        #         'id': user.id,  # or whatever fields you want to include
        #         'username': user.name,  # example field
        #         'email': user.email,  # example field
        #         # Add other fields as necessary
        #     })
        
        # Return a JsonResponse instead of HttpResponse
        return JsonResponse([{'id':1}], safe=False)  # Use safe=False to allow lists to be returned
