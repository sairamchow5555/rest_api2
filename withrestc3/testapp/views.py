from django.shortcuts import render
from rest_framework.views import APIView
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
# class EmployeeListAPIView(APIView):
#     def get(self,request,format=None):
#         qs = Employee.objects.all()
#         serializer = EmployeeSerializer(qs,many=True)
#         return Response(serializer.data)
#
# class EmployeeListAPIView(ListAPIView):
#     #queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     def get_queryset(self):
#         qs = Employee.objects.all()
#         name = self.request.GET.get('ename')
#         if name is not None:
#             qs = qs.filter(ename__icontains=name)
#         return qs
#
# class EmployeeCreateAPIView(CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# class EmployeeRetrieveAPIView(RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# class EmployeeUpdateAPIView(UpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# class EmployeeDestroyAPIView(DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# class EmployeeListCreateAPIView(ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# class EmployeeRetrieveDestroyAPIView(RetrieveDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# class EmployeeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class EmployeeListCreateModelMixins(CreateModelMixin,ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class EmployeeRetrieveUpdateDestroyModelMixins(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,APIView):
    def put(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):
        return self.partial_update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)
