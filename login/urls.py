from django.conf.urls import patterns,url
from login import views

urlpatterns = patterns('',url(r'^$',views.index,name='index')
                         ,url(r'^about/',views.about,name='about')
                         ,url(r'^add_category/',views.add_category,name='add_category')
                         ,url(r'^register/',views.register,name='register')
                         ,url(r'^login/',views.user_login,name='login')
                         ,url(r'^remove_cat/',views.remove_category,name='remove_cat')
                         ,url(r'^logout/',views.user_logout,name='logout')
                         ,url(r'^confirm/(?P<activation_key>\w+)/',views.register_confirm,name='register_confirm'),

                         )

                       
