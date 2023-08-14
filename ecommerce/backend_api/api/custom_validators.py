from rest_framework import serializers


def even_number(value):
    if value % 2 != 0:
        raise serializers.ValidationError('This field must be an even number.')
    

def char_validator(string, length):
    try:
        str(string)
    except:
        raise serializers.ValidationError('This field must be a string.')
    if len(string) > length:
        raise serializers.ValidationError(f'This field must be no longer than an {length}.')


class MultipleOf:
    def __init__(self, base):
        self.base = base

    def __call__(self, value):
        if value % self.base != 0:
            message = 'This field must be a multiple of %d.' % self.base
            raise serializers.ValidationError(message)