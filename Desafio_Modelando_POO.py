from abc import ABC, abstractclassmethod, abstractproperty
 

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self,  nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self. data_nascimento = data_nascimento


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def client(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Não é possivel realizar o saque, Você não tem saldo suficiente.")
        
        elif valor > 0:
            saldo -= valor 
            extrato += f"\tSaque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("‖‖ Saque realizado com sucesso! ‖‖")

        else:
            print("Operação invalida, verifique o valor informado")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor 
            print("\n‖‖ Depósito realizado com sucesso ‖‖")

        else:
            print("Operação invalida, verifique o valor informado.")
            return False
        
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super._init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if ["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite: 
            print("Não é possivel realizar o saque, O valor do saque excede o limite")

        elif excedeu_saques:
            print("Não é possivel realizar o saque, Número de saques diários excedido")

        else:
            return super().sacar(valor)

        return False


class Historico(ABC):
    def __init__(self):
        self._transacoes = []

    @property
    def trasacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.appe(
            {
                "tipo": transacao.__clas__.__name__,
                "valor": transacao.valor,
            }
        )


class Transacao(ABC):
    @property
    @abstractclassmethod
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.hitorico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.hitorico.adicionar_transacao(self)