from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from Forms.FeedbackForm import FeedbackForm
from Usecases.textClear import text_clear
from djStore import settings


@login_required
def index(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    if request.method == 'POST':
        form = FeedbackForm(data=request.POST)

        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.text = text_clear(form.cleaned_data['text'])
            feedback.user = request.user
            feedback.save()

    else:
        form = FeedbackForm()
    context = {
        'form': form,
    }
    return render(request, 'feedbacks/addFeedbackForm.html', context=context)
