from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
class MyException(MiddlewareMixin):
    def process_exception(self,request,exception):
        return HttpResponse('Exception is caused')

