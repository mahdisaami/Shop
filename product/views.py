
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView, CreateView, ListView

from category.models import Category
from product.forms import CreateProductForm, ImageForm
from product.models import Media, Product


class CreateProductView(CreateView):
    form_class = CreateProductForm
    template_name = 'product/create_product.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        messages.success(self.request, 'Product created')
        return super().form_valid(form)


@login_required
def add_product(request):
    ImageFormSet = modelformset_factory(Media,
                                        form=ImageForm, extra=3)

    # 'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':

        ProductForm = CreateProductForm(request.POST)
        # ProductForm.fields['category'].queryset = Category.objects.filter(name='Clothes')
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Media.objects.none())

        if ProductForm.is_valid() and formset.is_valid():
            product_form = ProductForm.save(commit=False)
            product_form.user = request.user

            product_form.save()

            for form in formset.cleaned_data:
                # this helps to not crash if the user
                # do not upload all the photos
                if form:
                    image = form['media_file']
                    photo = Media(product=product_form, media_file=image)
                    photo.save()
            # use django messages framework
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print(ProductForm.errors, formset.errors)
    else:
        ProductForm = CreateProductForm()
        formset = ImageFormSet(queryset=Media.objects.none())
    return render(request, 'product/create_product.html',
                  {'ProductForm': ProductForm, 'formset': formset})


class ProductListView(ListView):
    model = Product
    fields = ('name', 'description', 'price', 'category', 'medias', )
    template_name = 'product/products.html'
    queryset = Product.objects.all()



