from django import forms

class SchoolRegistrationForm(forms.Form):
    student_name = forms.CharField(max_length=100, label="Student Name", widget=forms.TextInput(attrs={'class': 'form-control'}))
    dob = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], label="Gender", widget=forms.Select(attrs={'class': 'form-select'}))
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(max_length=15, label="Phone Number", widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), label="Address")
    grade = forms.CharField(max_length=10, label="Grade Applying For", widget=forms.TextInput(attrs={'class': 'form-control'}))
