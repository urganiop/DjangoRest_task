from rest_framework import serializers
from mainapp.models import Order


class OrderSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('description','price')