import unittest
from unittest.mock import patch
from carona_unimar import carona_unimar

class CaronaUnimarTest(unittest.TestCase):

    def setUp(self):
        self.carona = carona_unimar()

    def tearDown(self):
        # Limpar o arquivo 'usuarios.txt' após cada teste
        with open('usuarios.txt', 'w') as file:
            file.write('')

    @patch('builtins.input', side_effect=['2', '4'])
    @patch('getpass.getpass', side_effect=['senha2', 'senha4'])
    def test_cadastrar(self, mock_input, mock_getpass):
        self.carona.cadastrar(2)
        
        # Verificar se os usuários foram corretamente cadastrados no arquivo
        with open('usuarios.txt', 'r') as file:
            lines = file.readlines()

        self.assertEqual(len(lines), 2)
        self.assertEqual(lines[0], '2:senha2\n')
        self.assertEqual(lines[1], '4:senha4\n')

if __name__ == '__main__':
    unittest.main()
