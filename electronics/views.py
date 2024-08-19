from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import NotFound, ValidationError

from .models import Factory, Network, Prod_net, Prod_fact, Prod_sell, Product
from .paginators import ItemPaginator
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = ItemPaginator

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            supplier = data.pop('supplier_choice')
            supplier_id = data.pop('supplier_id')
        except:
            raise ValidationError('Поставщик должен быть прикреплен')
        instance = self.get_serializer(data=data)
        instance.is_valid(raise_exception=True)
        new_product = Product.objects.create(instance)
        match supplier:
            case 'factory':
                supplier = Factory.objects.filter(id=supplier_id)
                if supplier.exists():
                    supplier = supplier.first()
                else:
                    raise ValidationError('Идентификатор поставщика не соответствует ни одному поставщику завода')
                prod_fact = Prod_fact.objects.create(
                    product=new_product, supplier=supplier
                )
                prod_fact.save()
            case 'network':
                supplier = Network.objects.filter(id=supplier_id)
                if supplier.exists():
                    supplier = supplier.first()
                else:
                    raise ValidationError("Идентификатор поставщика не соответствует ни одному поставщику сети")
                prod_net = Prod_net.objects.create(
                    product=new_product, supplier=supplier
                )
                prod_net.save()
            case 'seller':
                supplier = Network.objects.filter(id=supplier_id)
                if supplier.exists():
                    supplier = supplier.first()
                else:
                    raise ValidationError('Идентификатор поставщика не соответствует ни одному продавцу-поставщику')
                prod_sell = Prod_sell.objects.create(
                    product=new_product, supplier=supplier
                )
                prod_sell.save()
            case _:
                raise ValidationError('Выберите правильного поставщика')
        new_product.save()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        output = []
        serializer = self.get_serializer(queryset, many=True)
        for product in serializer.data:
            pass
