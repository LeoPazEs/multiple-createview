
MultipleCreateView
================== 
View to use multiple unrelated or related forms of different objects. 
Some mixins don't work with this view. 

Usage:  
```
class ContactFormView(MultipleCreateView): 
    template_name = 'contact.html' 
    form_class = {'form_contact' : ContactForm, 'form_client': ClientForm } 
    success_url = '/thanks/' 
```
