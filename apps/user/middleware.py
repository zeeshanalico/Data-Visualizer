from django.http import HttpResponse
import logging

def decode_request(get_response):
    def middleware(request):
        print("Before the view")
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Example log messages
        logging.debug("This is a debug message.")

        response = get_response(request)

        print("After the view")

        return response
    return middleware
