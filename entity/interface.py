from abc import ABC, abstractmethod
from datetime import date

class Person(ABC):
    '''
    Classe abstrada, que define os padrões/contrato para todos os usuários do sistema
    '''
    def __init__(self, name: str, cpf: str, date_of_birth: date, email: str):
        self._name = name
        self._cpf = cpf
        self._date_of_birth = date_of_birth
        self.email = email

    @property
    def name(self):
        ''' usado para retornar o nome dos usuários'''
        return self._name 

    @property
    def cpf(self):
        '''usado para retornar o cpf dos usuários'''
        return self._cpf
    
    @property
    def show_cpf(self):
        """
        Retorna uma versão dividida do CPF para mostrar os dados no sistema usando o método de 'split'.
        """
        partes = self._cpf.replace('-', '.').split('.')
        if len(partes) == 4:
            cpf_mascarado = f"***.{partes[1]}.{partes[2]}-**"
            return cpf_mascarado     
        return "CPF Inválido"

    @property
    def date_of_birth(self):
        '''usasdo apra retornar a data de aniversário dos usuários'''
        return self._date_of_birth

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email: str):
        if isinstance(new_email, str) and "@" in new_email and "." in new_email:
            self._email = new_email
        else:
            raise ValueError(f"ERRO: Email inválido: '{new_email}'.")
    
