from django.db import models


class Produto(models.Model):
    nome = models.CharField('Nome ', max_length=100)
    preco = models.DecimalField('Preco ', decimal_places=1, max_digits=8)
    estoque = models.IntegerField('Qnt Produto')

    def __str__(self):
        return self.nome

class Tributacao(models.Model):
    cfop = models.DecimalField('Cfop ', decimal_places=0, max_digits=4)
    ncm = models.DecimalField('Ncm ', decimal_places=0, max_digits=8)
    cst = models.DecimalField('Cst ', decimal_places=0, max_digits=3)

    def __int__(self):
        return self.ncm


class Cliente(models.Model):
    pnome = models.CharField('Primeiro Nome : ', max_length=100)
    snome = models.CharField('Segundo Nome : ', max_length=80)
    email = models.EmailField('Email : ' , max_length=100)
    sexo = models.CharField('Sexo : ', max_length=1)

    def __str__(self):
        return self.pnome

class Pagamento(models.Model):
    cartao = models.CharField('Cartão :', max_length=100)
    numero = models.DecimalField('Numero : ', decimal_places=0 , max_digits=9)
    bandeira = models.CharField('Bandeira : ', max_length=50)

    def __str__(self):
        return self.bandeira

class Cores(models.Model):
    nome = models.CharField('Nome ', max_length=50)
    codigo = models.DecimalField('Código ', decimal_places=0, max_digits=8)

    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    codigo = models.DecimalField('Código ', decimal_places=0, max_digits=10)
    nome = models.CharField('Nome ', max_length=100)
    email = models.EmailField('Email ', max_length=80)
    endereco = models.CharField('Endereço ', max_length=100)
    numero = models.DecimalField('Numero ', decimal_places=0, max_digits=15)
    tel = models.DecimalField('Telefone ',decimal_places=0, max_digits=15)

    def __str__(self):
        return self.nome

'''''''''
class Vendas(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    codvenda = models.DecimalField('Código Venda ',decimal_places=1, max_digits=10)
    codprod = models.DecimalField('Código Produto', decimal_places=0, max_digits=10)
    sku = models.DecimalField('Sku ', decimal_places=0, max_digits=15)
    tamanho = models.CharField('Tamanho ', max_length=10)
    cor  = models.DecimalField('Cor ',decimal_places=0, max_digits=10)
    quantidade = models.DecimalField('Quantidade ', decimal_places=0, max_digits=10)
    valor = models.DecimalField('Valor ',decimal_places=1, max_digits=10)
    troco = models.DecimalField('Troco ',decimal_places=1, max_digits=10)
    desconto = models.DecimalField('Desconto ', decimal_places=1, max_digits=10)
    acrescimo = models.DecimalField('Acrescimos ', decimal_places=1, max_digits=10)
    pagamento = models.DecimalField('Pagamento ', decimal_places=1, max_digits=10)
    cliente = models.CharField('Cliente ', max_length=50 )
    formapag = models.CharField('Forma de Pagamento ', max_length=40)
    parcelas = models.DecimalField('Parcelas ', decimal_places=1, max_digits=5)
    vendedor =  models.CharField('Vendedor ', max_length=50)
    codvendedor = models.DecimalField('Código Vendedor ', decimal_places=1, max_digits=10)
    caixa =  models.DecimalField('Caixa ', decimal_places=1, max_digits=10)
'''''''''
class Vender(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    codvenda = models.DecimalField('Código Venda ',decimal_places=1, max_digits=10)
    codprod = models.DecimalField('Código Produto', decimal_places=0, max_digits=10)
    sku = models.DecimalField('Sku ', decimal_places=0, max_digits=15)
    tamanho = models.CharField('Tamanho ', max_length=10)
    cor  = models.DecimalField('Cor ',decimal_places=0, max_digits=10)
    quantidade = models.DecimalField('Quantidade ', decimal_places=0, max_digits=10)
    valor = models.DecimalField('Valor ',decimal_places=1, max_digits=10)
    troco = models.DecimalField('Troco ',decimal_places=1, max_digits=10)
    desconto = models.DecimalField('Desconto ', decimal_places=1, max_digits=10)
    acrescimo = models.DecimalField('Acrescimos ', decimal_places=1, max_digits=10)
    pagamento = models.DecimalField('Pagamento ', decimal_places=1, max_digits=10)
    cliente = models.CharField('Cliente ', max_length=50 )
    formapag = models.CharField('Forma de Pagamento ', max_length=40)
    parcelas = models.DecimalField('Parcelas ', decimal_places=1, max_digits=5)
    vendedor =  models.CharField('Vendedor ', max_length=50)
    codvendedor = models.DecimalField('Código Vendedor ', decimal_places=1, max_digits=10)
    caixa =  models.DecimalField('Caixa ', decimal_places=1, max_digits=10)

    def __str__(self):
        return self.produto.nome

#= models.ManyToManyField(Tributacao, through="Membership")
class Nfe(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    vendas = models.ForeignKey(Vender, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    cores = models.ForeignKey(Cores, on_delete=models.CASCADE)
    tributacao = models.ForeignKey(Tributacao, on_delete=models.CASCADE)
    date_add = models.DateField()
    invite_reason = models.CharField(max_length=64)

class Nfce(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    vendas = models.ForeignKey(Vender, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    cores = models.ForeignKey(Cores, on_delete=models.CASCADE)
    tributacao = models.ForeignKey(Tributacao, on_delete=models.CASCADE)
    date_add = models.DateField()

'''''
class Tributo(models.Model):
    cfop = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cst = models.ForeignKey(Tributacao, on_delete=models.CASCADE)
    vendas = models.ForeignKey(Vendas, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    ncm  = models.ForeignKey(Produto, on_delete=models.CASCADE)
    ipi = models.ForeignKey(Tributacao, on_delete=models.CASCADE)
    csosn = models.ForeignKey(Tributacao, on_delete=models.CASCADE)
    cest = models.ForeignKey(Tributacao, on_delete=models.CASCADE)
'''''

"""
class Fiscal(models.Model):
    cfop = models.Charfield(Fiscal, max_length=150)
"""










