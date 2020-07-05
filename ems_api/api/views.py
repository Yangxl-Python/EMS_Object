import time

from django.http import JsonResponse
# from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.viewsets import ViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, \
    ListModelMixin, DestroyModelMixin

from api.models import User, Employee
from api.serializers import UserModelSerializer, EmployeeModelSerializer
from utils.response import APIResponse


class UserRegisterAPIView(CreateAPIView):
    serializer_class = UserModelSerializer


# class UserRegisterAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         user_data = request.data
#         print(user_data)
#         user_ser = UserModelSerializer(data=user_data)
#         user_ser.is_valid(raise_exception=True)
#         user_obj = user_ser.save()
#         if user_obj:
#             return APIResponse(data_message='success')
#         return APIResponse(data_message='fail')


class UserLoginViewSet(ViewSet):
    def login(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user_obj = User.objects.filter(username=username, password=password)
        if user_obj:
            return APIResponse(data_message=True)
        return APIResponse(data_message=False)


class EmployeeAPIView(CreateModelMixin, RetrieveModelMixin, ListModelMixin,
                      DestroyModelMixin, GenericAPIView):
    serializer_class = EmployeeModelSerializer
    queryset = Employee.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        emp_id = kwargs.get('id')
        if emp_id:
            res = self.retrieve(request, *args, **kwargs)
        else:
            res = self.list(request, *args, **kwargs)
        return res

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return APIResponse(data_message=True)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


def get_time(request):
    return JsonResponse({"time": time.strftime("%Y/%m/%d", time.localtime())})
