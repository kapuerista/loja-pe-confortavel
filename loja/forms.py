from django import forms
from .models import Cliente, Produto


class ClienteForm(forms.ModelForm):

    senha = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Cliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

    def clean_nome(self):

        nome = self.cleaned_data["nome"]

        if len(nome) < 25:
            raise forms.ValidationError(
                "O nome deve conter entre 25 e 70 caracteres."
            )

        return nome

    def clean_cpf(self):

        cpf = self.cleaned_data["cpf"]

        if not cpf.isdigit():
            raise forms.ValidationError(
                "O CPF deve conter apenas números."
            )

        if len(cpf) != 11:
            raise forms.ValidationError(
                "O CPF deve conter exatamente 11 números."
            )

        return cpf

    def clean_telefone(self):

        telefone = self.cleaned_data["telefone"]

        if not telefone.isdigit():
            raise forms.ValidationError(
                "O telefone deve conter apenas números."
            )

        if len(telefone) != 11:
            raise forms.ValidationError(
                "O telefone deve conter exatamente 11 números."
            )

        return telefone

    def clean_senha(self):

        senha = self.cleaned_data["senha"]

        if len(senha) != 8:
            raise forms.ValidationError(
                "A senha deve conter exatamente 8 caracteres."
            )

        return senha

    def clean(self):

        dados = super().clean()

        email = dados.get("email")
        usuario = dados.get("usuario")

        if email and usuario and usuario != email:
            self.add_error(
                "usuario",
                "O nome de usuário deve ser igual ao e-mail."
            )

        return dados


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'

    # mantenha abaixo os métodos de validação já existentes