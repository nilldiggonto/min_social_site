from django.shortcuts import get_object_or_404,render
from django.http import Http404,HttpResponseRedirect
from .models import ImiStatus
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import ImiModelForm
from imi_social.mixins import FormUserNeededMixin,UserOwnerMixin
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.



class Imi_list_view(ListView):
    model = ImiStatus
    template_name = 'imi_status/imi_list.html'

    def get_queryset(self,*args,**kwargs):
        qs = ImiStatus.objects.all()
        query = self.request.GET.get('q',None)
        if query is not None:
            qs = qs.filter(
                            Q(content__icontains = query) |
                            Q(user__username__icontains= query) 
                        )
        return qs

    def get_context_data(self, **kwargs):
        context = super(Imi_list_view,self).get_context_data(**kwargs)
        context["create_form"] = ImiModelForm()
        context['create_url'] = reverse_lazy('post:create') 
        return context
    

class Imi_detail_view(DetailView):
    model = ImiStatus
    template_name = 'imi_status/imi_detail.html'

class Imi_create_view(FormUserNeededMixin,SuccessMessageMixin, CreateView):
   
    form_class = ImiModelForm
   
    template_name = 'imi_status/create.html'
    success_message = "Your bs has been created"
    # success_url = reverse_lazy('post:detail')
    # login_url = '/admin/'


class Imi_update_view(LoginRequiredMixin,UserOwnerMixin, SuccessMessageMixin, UpdateView):
    model = ImiStatus
    form_class = ImiModelForm
    template_name = 'imi_status/update.html'
    
    login_url = '/admin/'
    success_message = "Your bs has been Updated"

class Imi_delete_view(LoginRequiredMixin,UserOwnerMixin, DeleteView):
    model = ImiStatus
    success_url = reverse_lazy('post:list')
    template_name = 'imi_status/delete.html'
    login_url = '/admin/'

    def delete(self, request, *args, **kwargs):
       self.object = self.get_object()
       if self.object.user == request.user:
          self.object.delete()
          return HttpResponseRedirect(self.get_success_url())
       else:
          raise Http404 #or return HttpResponse('404_url')

    

    
