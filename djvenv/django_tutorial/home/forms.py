from django import forms
from . models import Booking

class Dateinput(forms.DateInput):
    input_type = "date"

class Bookingform(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        
        widgets = {
            "booking_date" : Dateinput
        }
        labels = {
            'p_name' :"Patient Name : ", 
            'p_phone' : "Phone Number :",
            'p_email' : "Email : ",
            'doc_name' : "Doctor Name : " ,
            'booking_date' : "Booking Date : " 
        }