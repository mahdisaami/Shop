from django.contrib import messages
from django.forms import modelformset_factory
from django.views.generic import FormView
from product.forms import CreateProductForm


class CreateProductView(FormView):
    form_class = CreateProductForm
    template_name = 'product/create_product.html'
    success_url = '/'

    def form_valid(self, form):
        form.cleaned_data['user'] = self.request.user
        form.save()
        messages.success(self.request, 'Product created')
        return super().form_valid(form)
