from .forms import ContactForm
from django.views.generic.edit import FormView
from django.http import HttpResponse

from .models import Student


class ContactFormView(FormView):
    template_name = "author/contact.html"
    form_class = ContactForm
    models = Student
    # success_url = "/thanks/"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
        
    return HttpResponse('hello world')
    