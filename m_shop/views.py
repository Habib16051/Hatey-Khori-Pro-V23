from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Product, ProductCategory
from .forms import ProductForm
from django.urls import reverse_lazy  # Required for DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'home.html'
    
@method_decorator(login_required, name='dispatch')
class ProductListView(ListView):
    model = Product
    template_name = 'm_shop/shop.html'
    context_object_name = 'products'
    

class ProductDetailView(DetailView):
    model = Product
    template_name = 'm_shop/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'm_shop/add_product.html'

    def form_valid(self, form):
        product = form.save()
        return redirect('product_detail', pk=product.pk)

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'm_shop/update_product.html'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse_lazy('product_detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'm_shop/delete_product.html'
    context_object_name = 'product'
    success_url = reverse_lazy('shop')

class ManageCategoriesView(ListView):
    model = ProductCategory
    template_name = 'm_shop/manage_categories.html'
    context_object_name = 'categories'


# About Us View

class About(TemplateView):
    template_name = 'about.html'
    
    

# Contact View

from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

class ContactView(FormView):
    template_name = 'contacts/contact_form.html'
    form_class = ContactForm
    success_url = 'success/'

    def form_valid(self, form):
        # Get form data
        email = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']

        # Send email
        try:
            send_mail(
                subject,
                message,
                email,
                ['habibmhr143@gmail.com'],  # Replace with your email address
                fail_silently=False,
            )
            messages.success(self.request, 'Your message was sent successfully!')
        except Exception as e:
            messages.error(self.request, 'There was an error sending your message.')

        return super().form_valid(form)


# Success message

class SuccessView(TemplateView):
    template_name = 'contacts/success.html'


# Registration Page

# from django.shortcuts import render, redirect
# from .forms import RegisterForm
# from django.contrib import messages

# # Create your views here.
# def RegisterView(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f"Account created for {username}!")
#             return redirect('login')
#     else:
#         form = RegisterForm()

#     context = {'form': form}
#     return render(request, 'registration/register.html', context)