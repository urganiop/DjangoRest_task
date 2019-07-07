from mainapp.models import Order
from rest_framework import viewsets
from mainapp.serializers import OrderSerializers
from rest_framework.response import Response



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('price')
    serializer_class = OrderSerializers
    
    
    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializers(queryset, many=True)
        return Response(serializer.data)
    
    
#    def create(self, request):
#        serialized = self.serializer_class(data=request.data)
#        if serialized.is_valid():
#            serialized.save()
#            return Response(status=HTTP_202_ACCEPTED)
#        else:
#           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
#    def update(self, request, pk=None):
#        instance = self.queryset.get(pk=kwargs.get('pk'))
#        instance.save()
#        
#        
#    def destroy(self, request, pk=None):
#        pass