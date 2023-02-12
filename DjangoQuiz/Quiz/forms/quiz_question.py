from django import forms


class QuizQuestionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('choices')
        super().__init__(*args, **kwargs)
        self.fields['choice'] = forms.ChoiceField(choices=choices, widget=forms.RadioSelect())

    choice = forms.ChoiceField(widget=forms.RadioSelect())
