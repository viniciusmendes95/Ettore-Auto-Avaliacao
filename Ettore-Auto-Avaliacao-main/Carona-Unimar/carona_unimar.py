# Carona Unimar
import os
import getpass

class carona_unimar:
    def cadastrar(self, qtnd) -> None:
        with open('usuarios.txt', 'a') as file:
            for i in range(qtnd):
                user = input(f'Nome do usuário {i+1}: ')
                passwd = getpass.getpass(f'Senha do usuário {i+1}: ')
                file.write(f'{user}:{passwd}\n')

    def login(self, user, passwd) -> bool:
        with open('usuarios.txt', 'r') as file:
            for row in file:
                if user in row:
                    senha_user = str(row[row.index(':')+1:]).strip()
                    if passwd == senha_user:
                        return True
            return False
        
    def listar(self) -> None:
        with open('usuarios.txt', 'a') as file:
            file.write('carona unimar\n')
        
        with open('usuarios.txt', 'r') as file:
            print('--lista de usuarios--')
            print(file.read())
        
        input('aperte enter para continuar')

    def exibir_menu(self):
        menu = """--Bem vindo--
        [1] Cadastrar
        [2] Login
        [3] Listar
        [4] Sair
        Opção: """
        opcao = input(menu)
        return opcao

    def carona_unimar(self):
        print("Carona Unimar")
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            opcao = self.exibir_menu()
            os.system('cls' if os.name == 'nt' else 'clear')

            if opcao == '1':
                qtnd = int(input('Quantidade de usuários: '))
                self.cadastrar(qtnd)
            elif opcao == '2':
                user = input('Usuário: ')
                passwd = getpass.getpass('Senha: ')
                if self.login(user, passwd):
                    print(f'Entrou com sucesso na conta {user}')
                else:
                    print('Senha ou Usuário incorreto(s)')
                    input('Pressione enter para continuar')
            elif opcao == '3':
                self.listar()
            elif opcao == '4':
                break

if __name__ == '__main__':
    carona = carona_unimar()
    carona.carona_unimar()

