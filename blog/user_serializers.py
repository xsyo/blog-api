from djoser import serializers



class UserSerializer(serializers.UserSerializer):
    '''Расширяет базовый сериализатор UserSerializer'''
    class Meta(serializers.UserSerializer.Meta):
        fields = serializers.UserSerializer.Meta.fields + ('first_name', 'last_name')

class UserCreateSerializer(serializers.UserCreateSerializer):
    '''Расширяет базовый сериализатор UserCreateSerializer'''
    class Meta(serializers.UserCreateSerializer.Meta):
        fields = serializers.UserCreateSerializer.Meta.fields + ('first_name', 'last_name')