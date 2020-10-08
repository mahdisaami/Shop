from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, ListView, DetailView
from django.views import View

from category.models import Category, CatAttribute
from product.forms import CreateProductForm, ImageForm, CreatePrAttribute
from product.models import Media, Product, PrAttribute, Star


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
def create_product(request):
    ImageFormSet = modelformset_factory(Media, form=ImageForm, extra=3)
    AttributeFormSet = modelformset_factory(PrAttribute, form=CreatePrAttribute, extra=3)
    CatAttr = CatAttribute.objects.all()


    if request.method == 'POST':

        ProductForm = CreateProductForm(request.POST)
        AttributeForm = AttributeFormSet(request.POST, request.FILES, queryset=PrAttribute.objects.none())
        formset = ImageFormSet(request.POST, request.FILES, queryset=Media.objects.none())


        if ProductForm.is_valid() and formset.is_valid() and AttributeForm.is_valid():
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
            for form in AttributeForm.cleaned_data:
                if form:
                    value = form['value']
                    attr = PrAttribute(product=product_form, value=value, name=14)
                    attr.save()
            return HttpResponseRedirect("/")
        else:
            print(ProductForm.errors, formset.errors, AttributeForm.errors)
    else:
        ProductForm = CreateProductForm()
        formset = ImageFormSet(queryset=Media.objects.none())
        AttributeForm = AttributeFormSet(queryset=PrAttribute.objects.none())
    return render(request, 'product/create_product.html',
                  {'ProductForm': ProductForm, 'formset': formset, 'Attribute': AttributeForm, 'CatAttr': CatAttr})


class ProductListView(ListView):
    model = Product
    fields = ('name', 'description', 'price', 'category', 'medias', )
    template_name = 'product/products.html'
    queryset = Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'


class StarView(View):

    def get_object(self):
        try:
            product = Product.objects.filter(pk=self.kwargs.get('pk')).first()
        except product is None:
            raise Http404
        return product

    def get(self, request, *args, **kwargs):
        product = self.get_object()
        user = request.user
        star = Star.objects.filter(product=product, user=user).first()
        if star is None:
            star = Star.objects.create(product=product, user=user)
            return redirect('/product/{}'.format(self.kwargs.get('pk')))
        messages.error(self.request, 'Sorry you have already liked this product')
        return redirect('/product/{}'.format(self.kwargs.get('pk')))
