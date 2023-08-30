from django.urls import path

from .views import index, contato, produto, fornecedores, estoque, pagamento, vendas

urlpatterns =[
    path('',index ),
    path('contato' ,contato),
    path('produto',produto),
    path('fornecedores', fornecedores),
    path('estoque', estoque),
    path('pagamento', pagamento),
    path('vendas', vendas),

]