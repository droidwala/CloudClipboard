import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cloudclipboard.settings')

import django
django.setup()

from login.models import Category,Page

def populate():
    python_cat=add_cat(name='Python',views=128,likes=64)

    add_page(cat=python_cat,title='Official Python Tut',url="http://docs.python.org/2/tutorial")

    django_cat=add_cat('Django',views=23,likes=32)

    add_page(cat=django_cat,title='Official Django Tut',url="http://django.python.org")

    
def add_cat(name,views,likes):
    c = Category.objects.get_or_create(name=name,views=views,likes=likes)[0]
    return c

def add_page(cat,title,url,views=0):
    p = Page.objects.get_or_create(category=cat,title=title,url=url,views=views)[0]
    return p
    
if __name__=="__main__":
    print "Populating Database..."
    populate()

    
    
