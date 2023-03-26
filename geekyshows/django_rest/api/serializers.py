from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields ='__all__'
    #     extra_kwargs = {'name':{'read_only':True}}
    # def validate_roll(self, value):
    #     if value >= 200:
    #         raise serializers.ValidationError("Seats Are Full")
    #     return value
    # def validate(self,data):#Object level Validation
    #     nm=data.get('name')
    #     ct=data.get('city')
    #     if nm.lower() == 'rohit' and ct.lower() != 'cumilla':
    #         raise serializers.ValidationError('City must be Ranchi')
    #     return data 



#Validators
# def starts_with_r(value):
#         if value[0].lower() != 'r':
#             raise serializers.ValidationError('Name Should start with R')
#         return value
# class StudentSerializer(serializers.Serializer):
#     name=serializers.CharField(max_length=100, validators=[starts_with_r])
#     roll =serializers.IntegerField()
#     city=serializers.CharField(max_length=100)
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         instance.name=validated_data.get('name',instance.name)#this means if the user gives us name then take it or keep the data same as is in database
#         instance.roll=validated_data.get('roll',instance.roll)
#         instance.city=validated_data.get('city',instance.city)
#         instance.save()
#         return instance
#     def validate_roll(self, value):#Field level Validation
#         if value >= 200:
#             raise serializers.ValidationError('Seats Full')
#         return value
#     def validate(self,data):#Object level Validation
#         nm=data.get('name')
#         ct=data.get('city')
#         if nm.lower() == 'rohit' and ct.lower() != 'ranchi':
#             raise serializers.ValidationError('City must be Ranchi')
#         return data 















# from rest_framework import serializers
# from .models import Student
# #Validators
# def starts_with_r(value):
#         if value['0'].lower() != 'r':
#             raise serializers.ValidationError('Name Should start with R')
#         return value
        
# class StudentSerializer(serializers.Serializer):
    
#     name=serializers.CharField(max_length=100, validators=[starts_with_r])
#     roll =serializers.IntegerField()
#     city=serializers.CharField(max_length=100)
    
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)
#     def update(self, instance, validated_data):
        
#         instance.name=validated_data.get('name',instance.name)#this means if the user gives us name then take it or keep the data same as is in database
        
#         instance.roll=validated_data.get('roll',instance.roll)
#         instance.city=validated_data.get('city',instance.city)
#         instance.save()
#         return instance
#     def validate_roll(self,value):#(field level validation)this function will be autometically invoked when we validate data by is_valid function.And the function format is validata_fieldname
#         if value >= 200:
#             raise serializers.ValidationError('Seat Full!')
#         return value
#     def validate(self,data):#this is object level validation.when you have to do validation for multiple field then you use object level validation.In this one it says if name is rayhan then city must be cumilla.
#         nm=data.get('name')
#         ct=data.get('city')
#         if nm.lower() == 'rayhan' and ct.lower() !='cumilla':
#             raise serializers.ValidationError('City must be Cumilla for User Rayhan')
#         return data
        
        
    