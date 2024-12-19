import unittest
from unittest.mock import patch
class BankAccount:

    def __init__(self, account_number: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount: float):
        """Метод для пополнения счёта, сумма должна быть больше 0"""
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше 0")
        self.balance += amount  # увеличиваем баланс на указанную сумму

    def withdraw(self, amount: float): # метод для снятия денег со счёта
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше 0")
        if amount > self.balance:
            raise ValueError("Insufficient funds")  # ошибка при недостатке средств
        self.balance -= amount

    def get_balance(self) -> float:
        return self.balance


class TestBankAccount(unittest.TestCase):

    def test_create_account(self): # тест создания счёта с разными начальными балансами
        with self.assertRaises(ValueError):  # проверка, что при отрицательном балансе возникает ошибка
            BankAccount("12345", -50.0)

        account1 = BankAccount("12345", 100.0)
        self.assertEqual(account1.get_balance(), 100.0)  # проверяем, что баланс установлен правильно

        account2 = BankAccount("12345")
        self.assertEqual(account2.get_balance(), 0.0)

    def test_deposit(self): # тесты для метода пополнения счёта
        account = BankAccount("12345", 50.0)

        with self.assertRaises(ValueError):  # проверка ошибки при пополнении на 0
            account.deposit(0)

        with self.assertRaises(ValueError):  # проверка ошибки при пополнении отрицательной суммой
            account.deposit(-10.0)

        account.deposit(50.0)
        self.assertEqual(account.get_balance(), 100.0)  # проверяем, что баланс увеличился

    def test_withdraw(self): # тесты для метода снятия средств
        account = BankAccount("12345", 100.0)

        with self.assertRaises(ValueError):  # ошибка при попытке снять 0
            account.withdraw(0.0)

        with self.assertRaises(ValueError):
            account.withdraw(-10.0)

        with self.assertRaises(ValueError) as context:  # ошибка при попытке снять сумму больше баланса
            account.withdraw(200.0)
        self.assertEqual(str(context.exception), "Insufficient funds")  # проверяем сообщение ошибки

        account.withdraw(50.0)  # снимаем 50
        self.assertEqual(account.get_balance(), 50.0)  # проверяем, что баланс уменьшился

    def test_get_balance_after_operations(self):
        account = BankAccount("12345", 100.0)
        account.deposit(50.0)  # Пополняем на 50
        account.withdraw(30.0)  # Снимаем 30
        self.assertEqual(account.get_balance(), 120.0)  # проверяем, что баланс правильный

    @patch.object(BankAccount, 'get_balance', return_value=100.0)
    def test_mocked_get_balance(self, mock_get_balance): # тест с использованием мокирования метода get_balance
        account = BankAccount("12345", 50.0)
        self.assertEqual(account.get_balance(), 100.0)  # проверяем, что метод возвращает замокированное значение
        mock_get_balance.assert_called_once()


if __name__ == '__main__':
    unittest.main(verbosity=2)