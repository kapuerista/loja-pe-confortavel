from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm, ProdutoForm
from .models import Cliente, Produto
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def cadastrar_cliente(request):

    if request.method == 'POST':
        form = ClienteForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso.')
            return redirect('lista_clientes')

    else:
        form = ClienteForm()

    return render(
        request,
        'clientes/cadastrar_clientes.html',
        {'form': form}
    )


def lista_clientes(request):

    clientes = Cliente.objects.all()

    return render(
        request,
        'clientes/lista_clientes.html',
        {'clientes': clientes}
    )


def fabricante_construcao(request):
    return render(request, 'fabricantes/construcao.html')

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Produto cadastrado com sucesso.')
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()

    return render(
        request,
        'produtos/cadastrar_produto.html',
        {'form': form}
    )

def lista_produtos(request):

    produtos = Produto.objects.all()

    return render(
        request,
        'produtos/lista_produtos.html',
        {'produtos': produtos}
    )

def editar_cliente(request, id):

    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso.')
            return redirect('lista_clientes')

    else:
        form = ClienteForm(instance=cliente)

    return render(
        request,
        'clientes/editar_clientes.html',
        {
            'form': form,
            'cliente': cliente
        }
    )

def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)

    if request.method == 'POST':
        form = ProdutoForm(
            request.POST,
            request.FILES,
            instance=produto
        )

        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso.')
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)

    return render(
        request,
        'produtos/editar_produto.html',
        {
            'form': form,
            'produto': produto
        }
    )

def excluir_produto(request, id):

    produto = get_object_or_404(Produto, id=id)

    if request.method == "POST":
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso.')
        return redirect("lista_produtos")

    return render(
        request,
        "produtos/excluir_produto.html",
        {
            "produto": produto
        }
    )
    
def excluir_cliente(request, id):

    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')

    return render(
        request,
        'clientes/excluir_cliente.html',
        {
            'cliente': cliente
        }
    )