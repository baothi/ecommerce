'''
# shell session 1
# python manage.py shell
'''
from tags.models import Tag 
qs = Tag.objects.all()
print(qs)
black = Tag.objects.last()
black.title
black.slug
black.products

'''
return
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelateMany
'''
black.products.all()

'''
this is an actual queryset of PRODUCTS
Much like Products.objects.all(), but in this case it's All of the products that are
'''

black.products.all().frist()

''' 
returns the first instance, if any
'''
exit()

from products.models import Product

qs = Product.objects.all()
print(qs)
tshirt = qs.first()
tshirt.title
tshirt.description

tshirt.tag
'''
Raises an error because the Product model doens't have a field "tag"
'''

tshirt.tags
'''
Raises an error because the Product model doens't have a field "tags"
'''

tshirt.tag_set

tshirt.tag_set.all()