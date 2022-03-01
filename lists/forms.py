from django import forms
from lists.models import Tasks

PURPOSE = (
     ('Personal','Personal'),
     ('Fitness','Fitness'),
     ('School', 'School'),
     ('Business','Business'),        
     ('Office','Office'),        
)

class TodoForm(forms.ModelForm):
    purpose = forms.CharField(widget=forms.Select(choices=PURPOSE), label='Purpose')
    note = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    
    class Meta:
        model = Tasks
        exclude = ('slug',)
        fields = '__all__'
        