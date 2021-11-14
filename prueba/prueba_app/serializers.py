from rest_framework import serializers

from prueba_app.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Producto
		fields = ('id', 'name', 'stock', 'price', 'paused')