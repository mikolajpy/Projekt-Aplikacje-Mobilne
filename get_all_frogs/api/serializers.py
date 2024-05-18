from rest_framework import serializers
from get_all_frogs.models import StoreComment, Zabka, User

class ZabkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zabka
        fields = ['id','localization','name']


class CommSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')  # Użytkownik jest tylko do odczytu

    class Meta:
        model = StoreComment
        fields = ['id', 'parent','store' ,'user', 'comment', 'Ocena', 'created_at']
        extra_kwargs = {
            'store': {'required': True},
            'comment': {'required': True}
        }

    def validate(self, data):
        # Sprawdzenie, czy użytkownik próbuje stworzyć główny komentarz, gdy już taki istnieje
        if 'parent' not in data or data['parent'] is None:
            if 'Ocena' not in data or data['Ocena'] is None:
                raise serializers.ValidationError("Main comment must include a rating.")
            
            # Sprawdzenie, czy istnieje już główny komentarz użytkownika do danego sklepu
            user = self.context['request'].user
            if StoreComment.objects.filter(user=user, parent__isnull=True).exists():
                raise serializers.ValidationError("User can only create one main comment per store.")

        else:
            # Sprawdzenie, czy dodawany jest komentarz do komentarza głównego
            if data['parent'].parent is not None:
                raise serializers.ValidationError("Cannot add a subcomment to another subcomment.")

            if 'Ocena' in data and data['Ocena'] is not None:
                raise serializers.ValidationError("Subcomments cannot include a rating.")

        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'date_joined', 'last_login']
