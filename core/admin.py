from django.contrib import admin

# Register your models here.
from .models import Produto, Pagamento, Cores, Cliente, Fornecedor, Tributacao, Vender, Nfe, Nfce

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('pnome', 'snome', 'email', 'sexo')
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

    def __str__(self):
        return self.name

class CoresAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome')

class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('cartao', 'numero', 'bandeira')

class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo', 'email', 'endereco', 'numero', 'tel')

class TributacaoAdmin(admin.ModelAdmin):
    list_display = ('cfop', 'ncm', 'cst')

    def __int__(self):
        return self.cfop

'''''''''
class VenderAdmin(admin.ModelAdmin):
    list_display = ('codvenda', 'codprod', 'sku', 'tamanho', 'cor', 'quantidade', 'valor', 'troco', 'desconto', 'acrescimo', 'pagamento', 'cliente', 'formapag', 'parcelas', 'vendedor', 'codvendedor', 'caixa')
'''
class NfeAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'produto', 'vendas', 'fornecedor', 'pagamento', 'cores', 'tributacao', 'date_add', 'invite_reason')
    def __int__(self):
        return self.cfop
class VenderAdmin(admin.ModelAdmin):
    list_display = ('codvenda', 'codprod', 'sku', 'tamanho', 'cor', 'quantidade', 'valor', 'troco', 'desconto', 'acrescimo', 'pagamento', 'cliente', 'formapag', 'parcelas', 'vendedor', 'codvendedor', 'caixa')

class NfceAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'produto', 'vendas', 'fornecedor', 'pagamento', 'cores', 'tributacao', 'date_add')

    def __str__(self):
        return self.produto.nome


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Pagamento, PagamentoAdmin)
admin.site.register(Cores, CoresAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Tributacao, TributacaoAdmin)
#admin.site.register(Vendas, VendasAdmin)
admin.site.register(Nfe, NfeAdmin)
admin.site.register(Vender, VenderAdmin)
admin.site.register(Nfce, NfceAdmin)
