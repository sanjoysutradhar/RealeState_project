from rest_framework import serializers
from .models import Realtor


# serializers for realtor
class RealtorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Realtor
        # fields=['name','photo','desc','email','is_mvp','phone','message','contact_date']
        fields = '__all__'
