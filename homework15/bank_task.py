"""
Задание:
Возьмите любые 1-3 задачи из прошлых домашних заданий.
Добавьте к ним логирование ошибок и полезной информации.
Также реализуйте возможность запуска из командной строки с передачей параметров.

Логирование реализовано на базе задачи про банкомат,
а возможность запуска из командной строки с передачей параметров
релизована в 6 задаче из семинара (которую не успели сделать)
"""

import decimal
import logging

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

FORMAT = '{levelname:<8} - {asctime}. Функция: {funcName} Результат: {message}'

logging.basicConfig(filename='log/bank_operations.log', encoding='utf-8', format=FORMAT, style='{', level='INFO')
logger = logging.getLogger(__name__)


bank_account = decimal.Decimal(0)
count = 0


def deposit(amount):
    global bank_account, count
    # if check_multiplicity(amount):
    bank_account += amount
    msg = f"Пополнение карты на {amount} у.е. Итого {bank_account} у.е."
    print(msg)
    logging.info(msg)


def withdraw(amount):
    global bank_account, count
    com = (amount * PERCENT_REMOVAL)
    com = min(max(com, MIN_REMOVAL), MAX_REMOVAL)
    com = com.quantize(decimal.Decimal('0'))
    score = amount + com
    if score > bank_account:
        msg = f"Недостаточно средств. Сумма с комиссией {score} у.е. На карте {bank_account} у.е."
        print(msg)
        logging.error(msg)
    else:
        bank_account -= score
        msg = f"Снятие с карты {amount} у.е. Процент за снятие {com} у.е.. Итого {bank_account} у.е."
        print(msg)
        logging.info(msg)



def exit():
    global bank_account, count
    if bank_account > RICHNESS_SUM:
        tax = bank_account * RICHNESS_PERCENT.quantize(decimal.Decimal('.0001'))
        bank_account -= tax
        msg = f"Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {tax} у.е. Итого {bank_account} у.е."
        print(msg)
        logging.info(msg)
    msg = f"Возьмите карту на которой {bank_account} у.е."
    print(msg)
    logging.info(msg)


def input_amount(text: str) -> decimal.Decimal:
    while True:
        try:
            amount = decimal.Decimal(input(text))
            if amount <= 0:
                msg = "Сумма должна быть положительной."
                print(msg)
                logging.error(msg)
                continue
            if amount % MULTIPLICITY != 0:
                msg = f"Сумма должна быть кратной {MULTIPLICITY} у.е."
                print(msg)
                logging.error(msg)
                continue
            return amount
        except decimal.InvalidOperation:
            print("Введено не число. Попробуйте еще раз.")
            logging.error("Введено не число")


if __name__ == '__main__':

    while True:
        print("Выберите действие:")
        print("1. Пополнить карту")
        print("2. Снять с карты")
        print("3. Завершить работу")

        choice = input("Введите номер действия: ")

        if choice == "1":
            amount = input_amount("Введите сумму для пополнения: ")
            deposit(amount)
        elif choice == "2":
            amount = input_amount("Введите сумму для снятия: ")
            withdraw(amount)
        elif choice == "3":
            exit()
            break
        else:
            print("Некорректный выбор. Попробуйте еще раз.")
            logger.error("Некорректный выбор.")
