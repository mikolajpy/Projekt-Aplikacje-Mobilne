from rest_framework.serializers import ModelSerializer
from.models import Advocate

#to odpowiada na zamianę formatu danych


class AdvocateSerializer(ModelSerializer):
    class Meta:
        model = Advocate
        fields = '__all__'      #'username', 'password'
