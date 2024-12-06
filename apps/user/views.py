from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .middleware import decode_request
import json
@method_decorator(decode_request, name="dispatch")
class CreateUserView(View):
    def post(self, request, *args, **kwargs):
        # try:
            data = json.loads(request.body)
            print('__________________________________')
            print('__________________________________')
            print(data)
            print('__________________________________')
            print('__________________________________')
            print(request)
            print('__________________________________')
            print('__________________________________')
            user = User.objects.create(
                name=data.get("name"),
                email=data.get("email"),
                tel_no=data.get("tel_no"),
                location=data.get("location"),
                website=data.get("website"),
                city=data.get("city"),
                state=data.get("state"),
                role=data.get("role"),
                zip_code=data.get("zip_code"),
                category=data.get("category"),
                description=data.get("description"),
            )
        #     return JsonResponse({"message": "User created successfully", "id": '3'}, status=201)
        # except Exception as e:
        #     return JsonResponse({"error": str(e)}, status=400)
# Get All Users
class GetUsersView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all().values()
        return JsonResponse({"users": list(users)}, status=200, safe=False)
