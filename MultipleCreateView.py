class MultipleCreateView(CreateView): 
    """ Talvez alterar o father para BaseCreateView e um template response mixin"""

    def get_context_data(self, **kwargs): 
        for key, value in self.form_class.items(): 
            if key not in kwargs: 
                kwargs[key] = value
        return super().get_context_data(**kwargs)  
    
    def post(self,  request, *args, **kwargs):
        self.object = None 
        forms = {}
        for key, value in self.form_class.items(): 
            forms[key] = value(**self.get_form_kwargs()) 

        for form in forms.values(): 
            if not form.is_valid():
                return self.form_invalid(**forms) 
        return self.form_valid(**forms) 

    def form_valid(self, **forms):
        """ Implementar o save e não esquecer de colocar um self.object = form """ 
        
        for i, validForm in enumerate(forms.values()) : 
            if i == 0:
                self.object = validForm.save()
            validForm.save()  
        """
        form = forms['form'] 
        form.save()
        form2 = forms['form2'] 
        self.object = form2.save() 
        """

        """
        Fazer o messages.succes funcionar com **forms

        Tentar o -> if success_message
        super().form_valid(**forms) #Por que quando eu uso isso funciona, mas se eu  não usar super nenhum ele da erro? 
            Pq tem q falar para a view quem é o object.

        """ 
        print(self.object)
        messages.success(self.request, "This is my success message")
        print(self.get_success_url())
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self,**forms):
        return self.render_to_response(self.get_context_data(**forms))


