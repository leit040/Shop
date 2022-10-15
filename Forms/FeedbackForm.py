from django import forms

from feedbacks.models import Feedback


class FeedbackForm(forms.ModelForm):

    #def __init__(self, user, *args, **kwargs):
        # super().__init__(self, *args, **kwargs)
        # self.fields['user'].widget = forms.HiddenInput()
        # self.fields['user'].initial = user

    #не очень я понял для зачем это было, кстати оно так и не заработало нормально
    #я просто сделал сохранение во вьюшке и все. ну некошерно, но мои знания пока не позволяют быстро в ошибках разбиратся

    class Meta:
        model = Feedback
        fields = ('text', 'rate')
