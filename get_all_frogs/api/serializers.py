from rest_framework import serializers
from get_all_frogs.models import (
    StoreComment, Zabka, User , Achievements , AssignedAcievments , VisitedZabkas
)

class ZabkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zabka
        fields = ['id','localization','name']


class CommSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = StoreComment
        fields = ['id', 'parent', 'store', 'user', 'comment', 'Ocena', 'created_at']
        extra_kwargs = {
            'store': {'required': True},
            'comment': {'required': True}
        }

    def validate(self, data):
        request = self.context['request']
        user = request.user

        # Walidacja dla głównych komentarzy (bez parent)
        if data.get('parent') is None:
            store_id = data.get('store').id if data.get('store') else None

            # Sprawdzenie, czy istnieje już główny komentarz użytkownika do danego sklepu
            if StoreComment.objects.filter(user=user, store=store_id, parent__isnull=True).exists():
                raise serializers.ValidationError("User can only create one main comment per store.")

            # Dodatkowa walidacja dla oceny w głównym komentarzu
            if 'Ocena' not in data or data['Ocena'] is None:
                raise serializers.ValidationError("Main comment must include a rating.")

        # Walidacja dla subkomentarzy (z parent)
        else:
            # Sprawdzenie, czy dodawany jest komentarz do komentarza głównego
            if data['parent'].parent is not None:
                raise serializers.ValidationError("Cannot add a subcomment to another subcomment.")

            # Sprawdzenie, czy subkomentarze nie zawierają oceny
            if 'Ocena' in data and data['Ocena'] is not None:
                raise serializers.ValidationError("Subcomments cannot include a rating.")

        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'date_joined']

class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = ['achievment_id','achievement_name']

class AssignedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedAcievments
        fields = ['achievment_id', 'achievement_owner']

class VisitedSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitedZabkas
        fields = ['zabka','visitor']

