from rest_framework import serializers


def even_number(value):
    if value % 2 != 0:
        raise serializers.ValidationError('This field must be an even number.')
    

def char_validator(string, length, name):
    try:
        str(string)
    except:
        raise serializers.ValidationError(f'This string field must be a string. {name}')
    if len(string) > length:
        raise serializers.ValidationError(f'This string field must be no longer than an {length}. {name}')
    return string

def int_validator(number, length, name):
    try:
        int(number)
    except:
        raise serializers.ValidationError(f'This integer field must be a number. {name}')
    if len(number) > length:
        raise serializers.ValidationError(f'This integer must be lower than {length}. {name}')
    return number

class MultipleOf:
    def __init__(self, base):
        self.base = base

    def __call__(self, value):
        if value % self.base != 0:
            message = 'This field must be a multiple of %d.' % self.base
            raise serializers.ValidationError(message)