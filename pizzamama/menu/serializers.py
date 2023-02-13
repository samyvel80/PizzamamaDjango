from rest_framework import serializers
from .models import Pizza
from rest_framework.reverse import reverse

class PizzaSerializer(serializers.ModelSerializer):
    #url = serializers.SerializerMethodField()
    url = serializers.HyperlinkedIdentityField(view_name='menu:update', lookup_field='pk')
    class Meta:
        model = Pizza
        fields = ('pk','url', 'nom', 'ingredients', 'prix', 'vegetarienne')
    def validate_nom(self, value):# check doublon du name
        request= self.context.get('request')
        qs = Pizza.objects.filter(nom__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"la produit {value} existé déjà")
        return value

'''
    def get_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("menu:update", kwargs={'pk':obj.pk}, request=request)
   '''


class PizzaSerializerApiView(serializers.ModelSerializer):
    #url = serializers.SerializerMethodField()
    #url = serializers.HyperlinkedIdentityField(view_name='menu:update', lookup_field='pk')
    class Meta:
        model = Pizza
        #fields = ('pk','url', 'nom', 'ingredients', 'prix', 'vegetarienne')

        fields = ('nom', 'ingredients', 'prix', 'vegetarienne')
