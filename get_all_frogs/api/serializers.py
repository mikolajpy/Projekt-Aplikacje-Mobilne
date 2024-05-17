from rest_framework import serializers
from rest_framework import serializers
from django.shortcuts import get_object_or_404
from get_all_frogs.models import StoreComment, Zabka, User

class ZabkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zabka
        fields = ['id','localization','name','created_at']


class CommSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreComment
        fields = '__all__'

    def validate(self, data):
        store_value = data.get('store')
        user_value = data.get('user')
        parent_value = data.get('parent')

        # Sprawdzenie istnienia sklepu
        if not Zabka.objects.filter(id=store_value.id).exists():
            raise serializers.ValidationError("Podany sklep nie istnieje.")
        
        # Sprawdzenie istnienia użytkownika
        if not User.objects.filter(id=user_value.id).exists():
            raise serializers.ValidationError("Podany użytkownik nie istnieje.")

        # Sprawdzenie istnienia rodzica (jeśli podany)
        if parent_value and not StoreComment.objects.filter(id=parent_value.id).exists():
            raise serializers.ValidationError("Podany rodzic nie istnieje.")

        # Sprawdzenie, czy pole parent jest różne od null i jednocześnie próbuje dodać pole Ocena
        if parent_value is not None and data.get('Ocena') is not None:
            raise serializers.ValidationError("Ocena can only be added if parent is null.")

        # Sprawdzenie, czy użytkownik ma już główny komentarz dla danego sklepu
        if parent_value is None:
            existing_comments = StoreComment.objects.filter(store=store_value, user=user_value, parent__isnull=True)
            if existing_comments.exists():
                raise serializers.ValidationError("Użytkownik ma już komentarz dla tego sklepu.")
        
        return data

    def create(self, validated_data):
        parent_value = validated_data.get('parent')
        store_value = validated_data.get('store')
        user_value = validated_data.get('user')

        # Sprawdzenie istnienia sklepu
        if not Zabka.objects.filter(id=store_value.id).exists():
            raise serializers.ValidationError("Podany sklep nie istnieje.")
        
        # Sprawdzenie istnienia użytkownika
        if not User.objects.filter(id=user_value.id).exists():
            raise serializers.ValidationError("Podany użytkownik nie istnieje.")

        # Sprawdzenie istnienia rodzica (jeśli podany)
        if parent_value and not StoreComment.objects.filter(id=parent_value.id).exists():
            raise serializers.ValidationError("Podany rodzic nie istnieje.")

        # Sprawdzenie, czy pole parent jest różne od null i jednocześnie próbuje dodać pole Ocena
        if parent_value is not None and validated_data.get('Ocena') is not None:
            raise serializers.ValidationError("Ocena can only be added if parent is null.")

        # Sprawdzenie, czy użytkownik ma już główny komentarz dla danego sklepu
        if parent_value is None:
            existing_comments = StoreComment.objects.filter(store=store_value, user=user_value, parent__isnull=True)
            if existing_comments.exists():
                raise serializers.ValidationError("Użytkownik ma już komentarz dla tego sklepu.")

        return super().create(validated_data)
