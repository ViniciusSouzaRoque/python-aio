from abc import ABC, abstractmethod


class Pessoa(ABC):
    @abstractmethod
    def tipo_de_pessoa(self) -> None: pass

    @abstractmethod
    def documento(self) -> None: pass


class PessoaFisica(Pessoa):
    def tipo_de_pessoa(self) -> None:
        print("Pessoa Fisica")

    def documento(self) -> None:
        print("CPF")


class PessoaJuridica(Pessoa):
    def tipo_de_pessoa(self) -> None:
        print("Pessoa Juridica")

    def documento(self) -> None:
        print("CNPJ")


class PessoaFactory:
    @staticmethod
    def get_pessoa(tipo: str) -> Pessoa:
        if tipo == 'fisica':
            return PessoaFisica()
        if tipo == 'juridica':
            return PessoaJuridica()
        assert 0, 'Tipo inválido de pessoa.'


if __name__ == "__main__":
    fisica = PessoaFactory.get_pessoa('fisica')
    juridica = PessoaFactory.get_pessoa('juridica')

    print('--- Pessoa Fisica ---')
    fisica.tipo_de_pessoa()
    fisica.documento()

    print('--- Pessoa Juridica ---')
    juridica.tipo_de_pessoa()
    juridica.documento()
