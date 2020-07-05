from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError

from api.models import User, Employee


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'real_name', 'password', 'gender')
        extra_kwargs = {
            'username': {
                'max_length': 20,
                'min_length': 2,
                'error_messages': {
                    'max_length': '用户名长度不能超过20',
                    'min_length': '用户名至少2个字符'
                }
            },
            'real_name': {
                'max_length': 10,
                'min_length': 2,
                'error_messages': {
                    'max_length': '真实姓名长度不能超过10',
                    'min_length': '真实姓名至少2个字符'
                }
            },
            'password': {
                'max_length': 32,
                'min_length': 6,
                'write_only': True,
                'error_messages': {
                    'max_length': '密码长度不能超过32',
                    'min_length': '密码至少6个字符'
                }
            },
        }

    def validate_username(self, value):
        user_obj = User.objects.filter(username=value)
        if user_obj:
            raise ValidationError('用户名已存在')
        return value


class EmployeeModelSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'emp_name', 'age', 'img', 'salary', 'img_url')
        extra_kwargs = {
            'emp_name': {
                'max_length': 10,
                'min_length': 2,
                'error_messages': {
                    'max_length': '员工姓名不能超过10个字符。',
                    'min_length': '员工姓名至少两个字符。'
                }
            },
            'age': {
                'max_value': 60,
                'min_value': 18,
                'error_messages': {
                    'max_value': '年龄不能超过60岁。',
                    'min_value': '年龄不能小于18岁。'
                }
            },
            'salary': {
                'max_digits': 8,
                'decimal_places': 2,
                'error_messages': {
                    'max_digits': '工资不能过八位数（包括小数）。',
                    'decimal_places': '最多两位小数。'
                }
            },
            'img': {
                'write_only': True
            },
            'img_url': {
                'read_only': True
            }
        }

    def validate_emp_name(self, value):
        emp_obj = Employee.objects.filter(emp_name=value)
        if emp_obj and self.context.get('request').method != 'PATCH':
            raise ValidationError('员工已存在')
        return value
