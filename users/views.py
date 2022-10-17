from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic import TemplateView

from Forms.RegistrationForm import RegistrationForm


class Registration(TemplateView):
    template_name = 'users/registrationForm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(({'form': RegistrationForm}))
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = context['form']
        form = form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email'].split('@')[0]
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email,
                                            is_active=True,
                                            is_staff=False,
                                            is_superuser=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect("/feedbacks/")
