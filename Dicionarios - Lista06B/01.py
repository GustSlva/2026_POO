from datetime import datetime
import json
from typing import List, Optional

# ==========================================
# MODELOS
# ==========================================

class Cliente:
    def __init__(self, id_cliente: int, nome: str, email: str, fone: str):
        self.id = id_cliente
        self.nome = nome
        self.email = email
        self.fone = fone

    def __str__(self):
        return f'Cliente N° {self.id} | Nome: {self.nome} | E-mail: {self.email} | Telefone: {self.fone}'

    @property
    def id(self): return self.__id
    
    @id.setter
    def id(self, valor: int):
        if valor <= 0: raise ValueError("ID inválido!")
        self.__id = valor

    @property
    def nome(self): return self.__nome

    @nome.setter
    def nome(self, valor: str):
        if not valor: raise ValueError("Nome não pode ser vazio!")
        self.__nome = valor

    @property
    def email(self): return self.__email

    @email.setter
    def email(self, valor: str):
        if not valor: raise ValueError("E-mail não pode ser vazio!")
        self.__email = valor

    @property
    def fone(self): return self.__fone

    @fone.setter
    def fone(self, valor: str):
        if not valor: raise ValueError("Telefone não pode ser vazio!")
        self.__fone = valor


class Categoria:
    def __init__(self, id_categoria: int, descricao: str):
        self.id = id_categoria
        self.descricao = descricao

    def __str__(self):
        return f'Categoria N° {self.id} | Descrição: {self.descricao}'
    
    @property
    def id(self): return self.__id

    @id.setter
    def id(self, valor: int):
        if valor <= 0: raise ValueError("ID inválido!")
        self.__id = valor

    @property
    def descricao(self): return self.__descricao

    @descricao.setter
    def descricao(self, valor: str):
        if not valor: raise ValueError("Descrição inválida!")
        self.__descricao = valor


class Produto:
    def __init__(self, id_produto: int, descricao: str, preco: float, estoque: int, id_categoria: int):
        self.id = id_produto
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.id_categoria = id_categoria

    def __str__(self):
        return f'Produto N° {self.id} | Desc: {self.descricao} | Preço: R${self.preco:.2f} | Estoque: {self.estoque} | Categoria ID: {self.id_categoria}'
    
    @property
    def id(self): return self.__id
    @id.setter
    def id(self, valor: int):
        if valor <= 0: raise ValueError("ID inválido!")
        self.__id = valor

    @property
    def descricao(self): return self.__descricao
    @descricao.setter
    def descricao(self, valor: str):
        if not valor: raise ValueError("Descrição inválida!")
        self.__descricao = valor

    @property
    def preco(self): return self.__preco
    @preco.setter
    def preco(self, valor: float):
        if valor < 0: raise ValueError("Preço inválido!")
        self.__preco = valor

    @property
    def estoque(self): return self.__estoque
    @estoque.setter
    def estoque(self, valor: int):
        if valor < 0: raise ValueError("Estoque inválido!")
        self.__estoque = valor

    @property
    def id_categoria(self): return self.__id_categoria
    @id_categoria.setter
    def id_categoria(self, valor: int):
        if valor <= 0: raise ValueError("ID de Categoria inválido!")
        self.__id_categoria = valor


class Venda:
    def __init__(self, id_venda: int):
        self.id = id_venda 
        self.data: Optional[datetime] = None
        self.carrinho: bool = False
        self.total: float = 0.0
        self.id_cliente: int = 0
    
    def __str__(self):
        data_str = self.data.strftime('%d/%m/%Y %H:%M') if self.data else 'Pendente'
        return f'Venda N° {self.id} | Data: {data_str} | Carrinho Aberto: {self.carrinho} | Total: R${self.total:.2f} | Cliente ID: {self.id_cliente}'
    
    @property
    def id(self): return self.__id
    @id.setter
    def id(self, valor: int):
        if valor <= 0: raise ValueError("ID inválido!")
        self.__id = valor
    
    @property
    def data(self): return self.__data
    @data.setter
    def data(self, valor):
        if valor is not None and not isinstance(valor, datetime): raise ValueError("Data inválida!")
        self.__data = valor

    @property
    def carrinho(self): return self.__carrinho
    @carrinho.setter
    def carrinho(self, valor: bool):
        if not isinstance(valor, bool): raise ValueError("Status do carrinho inválido!")
        self.__carrinho = valor

    @property
    def total(self): return self.__total
    @total.setter
    def total(self, valor: float):
        if valor < 0: raise ValueError("O total não pode ser negativo!")
        self.__total = valor

    @property
    def id_cliente(self): return self.__id_cliente
    @id_cliente.setter
    def id_cliente(self, valor: int):
        if valor < 0: raise ValueError("ID do Cliente inválido!")
        self.__id_cliente = valor


class VendaItem:
    def __init__(self, id_item: int, qtd: int, preco: float):
        self.id = id_item
        self.qtd = qtd
        self.preco = preco
        self.id_venda: int = 0
        self.id_produto: int = 0

    def __str__(self):
        return f'Item N° {self.id} | Qtd: {self.qtd} | Preço: R${self.preco:.2f} | Venda ID: {self.id_venda} | Produto ID: {self.id_produto}'

    @property
    def id(self): return self.__id
    @id.setter
    def id(self, valor: int):
        if valor <= 0: raise ValueError("ID inválido!")
        self.__id = valor

    @property
    def qtd(self): return self.__qtd
    @qtd.setter
    def qtd(self, valor: int):
        if valor <= 0: raise ValueError("Quantidade inválida!")
        self.__qtd = valor

    @property
    def preco(self): return self.__preco
    @preco.setter
    def preco(self, valor: float):
        if valor < 0: raise ValueError("Preço inválido!")
        self.__preco = valor

    @property
    def id_venda(self): return self.__id_venda
    @id_venda.setter
    def id_venda(self, valor: int):
        if valor < 0: raise ValueError("ID da Venda inválido!")
        self.__id_venda = valor

    @property
    def id_produto(self): return self.__id_produto
    @id_produto.setter
    def id_produto(self, valor: int):
        if valor < 0: raise ValueError("ID do Produto inválido!")
        self.__id_produto = valor


# ==========================================
# DAOs (Data Access Objects)
# ==========================================

class ClienteDAO:
    objetos: List[Cliente] = []

    @classmethod
    def inserir(cls, obj: Cliente):
        cls.objetos.append(obj)

    @classmethod
    def listar(cls) -> List[Cliente]:
        return cls.objetos

    @classmethod
    def listar_id(cls, id_cliente: int) -> Optional[Cliente]:
        for obj in cls.objetos:
            if obj.id == id_cliente: return obj
        return None

    @classmethod
    def atualizar(cls, obj: Cliente):
        cliente = cls.listar_id(obj.id)
        if cliente:
            cliente.nome = obj.nome
            cliente.email = obj.email
            cliente.fone = obj.fone

    @classmethod
    def excluir(cls, id_cliente: int):
        cliente = cls.listar_id(id_cliente)
        if cliente: cls.objetos.remove(cliente)

    @classmethod
    def salvar(cls):
        with open('clientes.json', 'w') as f:
            lista = [{'id': o.id, 'nome': o.nome, 'email': o.email, 'fone': o.fone} for o in cls.objetos]
            json.dump(lista, f, indent=4)

    @classmethod
    def abrir(cls):
        cls.objetos.clear()
        try:
            with open('clientes.json', 'r') as f:
                for d in json.load(f):
                    cls.objetos.append(Cliente(d['id'], d['nome'], d['email'], d['fone']))
        except FileNotFoundError: pass


class CategoriaDAO:
    objetos: List[Categoria] = []

    @classmethod
    def inserir(cls, obj: Categoria): cls.objetos.append(obj)

    @classmethod
    def listar(cls) -> List[Categoria]: return cls.objetos

    @classmethod
    def listar_id(cls, id_categoria: int) -> Optional[Categoria]:
        for obj in cls.objetos:
            if obj.id == id_categoria: return obj
        return None

    @classmethod
    def atualizar(cls, obj: Categoria):
        categoria = cls.listar_id(obj.id)
        if categoria: categoria.descricao = obj.descricao

    @classmethod
    def excluir(cls, id_categoria: int):
        categoria = cls.listar_id(id_categoria)
        if categoria: cls.objetos.remove(categoria)

    @classmethod
    def salvar(cls):
        with open('categorias.json', 'w') as f:
            lista = [{'id': o.id, 'descricao': o.descricao} for o in cls.objetos]
            json.dump(lista, f, indent=4)

    @classmethod
    def abrir(cls):
        cls.objetos.clear()
        try:
            with open('categorias.json', 'r') as f:
                for d in json.load(f):
                    cls.objetos.append(Categoria(d['id'], d['descricao']))
        except FileNotFoundError: pass


class ProdutoDAO:
    objetos: List[Produto] = []

    @classmethod
    def inserir(cls, obj: Produto): cls.objetos.append(obj)

    @classmethod
    def listar(cls) -> List[Produto]: return cls.objetos

    @classmethod
    def listar_id(cls, id_produto: int) -> Optional[Produto]:
        for obj in cls.objetos:
            if obj.id == id_produto: return obj
        return None

    @classmethod
    def atualizar(cls, obj: Produto):
        produto = cls.listar_id(obj.id)
        if produto:
            produto.descricao = obj.descricao
            produto.preco = obj.preco
            produto.estoque = obj.estoque
            produto.id_categoria = obj.id_categoria

    @classmethod
    def excluir(cls, id_produto: int):
        produto = cls.listar_id(id_produto)
        if produto: cls.objetos.remove(produto)

    @classmethod
    def salvar(cls):
        with open('produtos.json', 'w') as f:
            lista = [{'id': o.id, 'descricao': o.descricao, 'preco': o.preco, 'estoque': o.estoque, 'id_categoria': o.id_categoria} for o in cls.objetos]
            json.dump(lista, f, indent=4)

    @classmethod
    def abrir(cls):
        cls.objetos.clear()
        try:
            with open('produtos.json', 'r') as f:
                for d in json.load(f):
                    cls.objetos.append(Produto(d['id'], d['descricao'], d['preco'], d['estoque'], d['id_categoria']))
        except FileNotFoundError: pass


class VendaDAO:
    objetos: List[Venda] = []

    @classmethod
    def inserir(cls, obj: Venda): cls.objetos.append(obj)

    @classmethod
    def listar(cls) -> List[Venda]: return cls.objetos

    @classmethod
    def listar_id(cls, id_venda: int) -> Optional[Venda]:
        for obj in cls.objetos:
            if obj.id == id_venda: return obj
        return None

    @classmethod
    def atualizar(cls, obj: Venda):
        venda = cls.listar_id(obj.id)
        if venda:
            venda.data = obj.data
            venda.carrinho = obj.carrinho
            venda.total = obj.total
            venda.id_cliente = obj.id_cliente

    @classmethod
    def excluir(cls, id_venda: int):
        venda = cls.listar_id(id_venda)
        if venda: cls.objetos.remove(venda)

    @classmethod
    def salvar(cls):
        with open('vendas.json', 'w') as f:
            lista = []
            for o in cls.objetos:
                data_texto = o.data.strftime('%Y-%m-%d %H:%M:%S') if o.data else None
                lista.append({'id': o.id, 'data': data_texto, 'carrinho': o.carrinho, 'total': o.total, 'id_cliente': o.id_cliente})
            json.dump(lista, f, indent=4)

    @classmethod
    def abrir(cls):
        cls.objetos.clear()
        try:
            with open('vendas.json', 'r') as f:
                for d in json.load(f):
                    venda = Venda(d['id'])
                    if d['data']: venda.data = datetime.strptime(d['data'], '%Y-%m-%d %H:%M:%S')
                    venda.carrinho = d['carrinho']
                    venda.total = d['total']
                    venda.id_cliente = d['id_cliente']
                    cls.objetos.append(venda)
        except FileNotFoundError: pass


class VendaItemDAO:
    objetos: List[VendaItem] = []

    @classmethod
    def inserir(cls, obj: VendaItem): cls.objetos.append(obj)
    
    @classmethod
    def listar(cls) -> List[VendaItem]: return cls.objetos

    @classmethod
    def listar_id(cls, id_item: int) -> Optional[VendaItem]:
        for obj in cls.objetos:
            if obj.id == id_item: return obj
        return None

    @classmethod
    def atualizar(cls, obj: VendaItem):
        item = cls.listar_id(obj.id)
        if item:
            item.qtd = obj.qtd
            item.preco = obj.preco
            item.id_venda = obj.id_venda
            item.id_produto = obj.id_produto

    @classmethod
    def excluir(cls, id_item: int):
        item = cls.listar_id(id_item)
        if item: cls.objetos.remove(item)

    @classmethod
    def salvar(cls):
        with open('venda_itens.json', 'w') as f:
            lista = [{'id': o.id, 'qtd': o.qtd, 'preco': o.preco, 'id_venda': o.id_venda, 'id_produto': o.id_produto} for o in cls.objetos]
            json.dump(lista, f, indent=4)

    @classmethod
    def abrir(cls):
        cls.objetos.clear()
        try:
            with open('venda_itens.json', 'r') as f:
                for d in json.load(f):
                    item = VendaItem(d['id'], d['qtd'], d['preco'])
                    item.id_venda = d['id_venda']
                    item.id_produto = d['id_produto']
                    cls.objetos.append(item)
        except FileNotFoundError: pass


# ==========================================
# INTERFACE DE USUÁRIO (UI)
# ==========================================

class UI:
    @classmethod
    def main(cls):
        ClienteDAO.abrir()
        CategoriaDAO.abrir()
        ProdutoDAO.abrir()
        
        op = -1
        while op != 0:
            op = cls.menu()
            if op == 1: cls.cliente_inserir()
            elif op == 2: cls.cliente_listar()
            elif op == 3: cls.cliente_atualizar()
            elif op == 4: cls.cliente_excluir()
            elif op == 5: cls.categoria_inserir()
            elif op == 6: cls.categoria_listar()
            elif op == 7: cls.categoria_atualizar()
            elif op == 8: cls.categoria_excluir()
            elif op == 9: cls.produto_inserir()
            elif op == 10: cls.produto_listar()
            elif op == 11: cls.produto_atualizar()
            elif op == 12: cls.produto_excluir()
            
        ClienteDAO.salvar()
        CategoriaDAO.salvar()
        ProdutoDAO.salvar()

    @classmethod
    def menu(cls) -> int:
        print("\n=== SISTEMA DE GESTÃO ===")
        print("1 - Inserir Cliente")
        print("2 - Listar Clientes")
        print("3 - Atualizar Cliente")
        print("4 - Excluir Cliente")
        print("-" * 25)
        print("5 - Inserir Categoria")
        print("6 - Listar Categorias")
        print("7 - Atualizar Categoria")
        print("8 - Excluir Categoria")
        print("-" * 25)
        print("9 - Inserir Produto")
        print("10 - Listar Produtos")
        print("11 - Atualizar Produto")
        print("12 - Excluir Produto")
        print("0 - Sair e Salvar")
        try:
            return int(input("Escolha uma opção: "))
        except ValueError:
            return -1

    # --- CLI Cliente ---
    @classmethod
    def cliente_inserir(cls):
        id_cli = int(input("ID: "))
        nome = input("Nome: ")
        email = input("Email: ")
        fone = input("Fone: ")
        ClienteDAO.inserir(Cliente(id_cli, nome, email, fone))

    @classmethod
    def cliente_listar(cls):
        for obj in ClienteDAO.listar(): print(obj) # Repare que aqui chama automaticamente o __str__

    @classmethod
    def cliente_atualizar(cls):
        id_cli = int(input("ID a atualizar: "))
        nome = input("Novo Nome: ")
        email = input("Novo Email: ")
        fone = input("Novo Fone: ")
        ClienteDAO.atualizar(Cliente(id_cli, nome, email, fone))

    @classmethod
    def cliente_excluir(cls):
        id_cli = int(input("ID a excluir: "))
        ClienteDAO.excluir(id_cli)

    # --- CLI Categoria ---
    @classmethod
    def categoria_inserir(cls):
        id_cat = int(input("ID: "))
        descricao = input("Descrição: ")
        CategoriaDAO.inserir(Categoria(id_cat, descricao))

    @classmethod
    def categoria_listar(cls):
        for obj in CategoriaDAO.listar(): print(obj)

    @classmethod
    def categoria_atualizar(cls):
        id_cat = int(input("ID a atualizar: "))
        descricao = input("Nova Descrição: ")
        CategoriaDAO.atualizar(Categoria(id_cat, descricao))

    @classmethod
    def categoria_excluir(cls):
        id_cat = int(input("ID a excluir: "))
        CategoriaDAO.excluir(id_cat)

    # --- CLI Produto ---
    @classmethod
    def produto_inserir(cls):
        id_prod = int(input("ID: "))
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))
        id_cat = int(input("ID Categoria: "))
        ProdutoDAO.inserir(Produto(id_prod, descricao, preco, estoque, id_cat))

    @classmethod
    def produto_listar(cls):
        for obj in ProdutoDAO.listar(): print(obj)

    @classmethod
    def produto_atualizar(cls):
        id_prod = int(input("ID a atualizar: "))
        descricao = input("Nova Descrição: ")
        preco = float(input("Novo Preço: "))
        estoque = int(input("Novo Estoque: "))
        id_cat = int(input("Novo ID Categoria: "))
        ProdutoDAO.atualizar(Produto(id_prod, descricao, preco, estoque, id_cat))

    @classmethod
    def produto_excluir(cls):
        id_prod = int(input("ID a excluir: "))
        ProdutoDAO.excluir(id_prod)


if __name__ == "__main__":
    UI.main()