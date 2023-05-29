from rest_framework import serializers
from .models import School , Student



class OnlySrudentSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city','school']
        # read_only_fields = []

        

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)

    def validate_roll(self,value):
        if value >= 90:
            raise serializers.ValidationError("Seat is Full")
        return value
    
    def validate(self,data):
        nm = data.get('name')
        ct = data.get('city')
        rl = data.get('roll')

        if isinstance(nm,str) == False:
            raise serializers.ValidationError('Must be a string')

        if nm.lower() == 'abc' and ct.lower() != 'xyz':
            raise serializers.ValidationError('City is not valid')
        return data
class SchoolListSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id','name','location']





class StudentListSerializer(serializers.ModelSerializer):
    school = SchoolListSerializer()

    class Meta:
        model = Student
        fields = ['id','name','roll','city','school']

    def create(self, validated_data):
        return Student.objects.create(**validated_data)