from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import NameSerializers
# Create your views here.
class TestAPIView(APIView):
    def get(self,request,*args,**kwargs):
        colors = ['Red','Orange','Black','Green','Pink']
        return Response({'msg':'Good Morning have a Nice Day','colors':colors}) #to convert python dict to json

    def post(self,request,*args,**kwargs):
        serializer = NameSerializers(data = request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'Hello {}, Have a good day'.format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status = 404)

    def put(self,request,*args,**kwargs):
        return Response({'msg':'This is from PUT method'})

    def delete(self,request,*args,**kwargs):
        return Response({'msg':'This is from DELETE method'})

    def patch(self,request,*args,**kwargs):
        return Response({'msg':'This is from PATCH method'})

from rest_framework.viewsets import ViewSet
class TestViewSet(ViewSet):
    def list(self,request):
        colors = ['Red','Orange','Black','Green','Pink']
        return Response({'msg':'Good Nigth have a Nice Sleep','colors':colors}) #to convert python dict to json

    def create(self,request):
        serializer = NameSerializers(data = request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            msg = 'Hello {}, good Night have a sweet dreams'.format(name)
            return Response({'msg':msg})
        else:
            return Response(serializer.errors,status = 404)

    def retrieve(self,request,pk=None):
        return Response({'msg':'This response from RETRIEVE method'})

    def update(self,request,pk=None):
        return Response({'msg':'This response from UPDATE method'})

    def partial_update(self,request,pk=None):
        return Response({'msg':'This response from PARTIAL UPDATE method'})

    def destroy(self,request,pk=None):
        return Response({'msg':'This response from DESTROY method'})
