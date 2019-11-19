from django import forms

from .models import Poll,Choice

class PollForm(forms.ModelForm):

    choice1 = forms.CharField(
                            label ='Primeira Opção', 
                            max_length= 100,
                            min_length=2,
                            widget = forms.TextInput(attrs={'class':'form-control'}),)
    choice2 = forms.CharField(
                            label ='Segunda Opção', 
                            max_length= 100,
                            min_length=2,
                            widget = forms.TextInput(attrs={'class':'form-control'}),)

    class Meta:
        model = Poll
        fields = ['texto','choice1', 'choice2']
        widgets = {
            'texto': forms.Textarea(attrs = {"class":"form-control", "rows":5, "cols":20})
        }

class EditPollForm(forms.ModelForm):
   class Meta:
        model = Poll
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={"class":"form-control", "rows": 5, "cols": 20})
        }

class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ['opcao_escolha']