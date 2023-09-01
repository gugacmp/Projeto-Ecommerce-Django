from django.shortcuts import render
# Create your views here.

def index(request):
    print(dir(request.user))
    print(f"User: {request.user}")

    if str(request.user) == 'AnonymousUser':
        teste = (f"Usuário : {request.user}")
    else:
        teste = (f"Usuário : {request.user}")
    context = {
        'logado' : teste,
        'ultimo' : (f"Email : {request.user.email}"),

    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')

def produto(request):
    return render(request, 'produto.html')
    
def fornecedores(request):
    return render(request,'fornecedores.html')

def estoque(request):
    return render(request, 'estoque.html')

def pagamento(request):
    return render(request, 'pagamento.html')

def vendas(request):
    return render(request, 'vendas.html')

def fiscal(request):
    return render(request, 'fiscal.html')
