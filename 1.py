import re
import socket
from typing import Any
import dns.resolver
import smtplib
from validate_email_address import validate_email
import openpyxl

# pattern = "^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
# pattern_2 = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
# pattern_3 = "^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$"


def checking_mail_syntax(list_email: list) -> tuple[list[Any], list[Any]]:
    """
    Функция проверки списка email адресов на валидность с использованием регулярных выражений
    :param list_email: список email адресов
    :return: кортеж из двух списков: валидных и невалидных email адресов
    """
    valid_syntax_email = []
    invalid_syntax_email = []
    pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    for mail in list_email:
        if re.match(pattern, mail) is not None:
            valid_syntax_email.append(mail)
        else:
            invalid_syntax_email.append(mail)
    print(f"хорошие{len(valid_syntax_email)} \n\n\n\n\n плохие{len(invalid_syntax_email)}")
    print(f"\nхорошие \n{valid_syntax_email}, \n\n\n\n\nплохие \n{invalid_syntax_email}")
    return valid_syntax_email, invalid_syntax_email

def alternative_email_verification(list_email: list) -> tuple[list[Any], list[Any]]:
    """
    Функция проверки списка email адресов на валидность с использованием validate_email_address
    :param list_email: список email адресов
    :return: кортеж из двух списков: валидных и невалидных email адресов
    """
    valid_email = []
    invalid_email = []

    for mail in list_email:
        if validate_email(mail, verify=True):
            valid_email.append(mail)
        else:
            invalid_email.append(mail)
    print(f"хорошие {valid_email}, плохие {invalid_email}")
    return valid_email, invalid_email

def alternative_email_verification2(list_email: list) -> tuple[list[Any], list[Any]]:
    """
    Function to verify a list of email addresses by checking MX records and mail server availability
    :param list_email: list of email addresses
    :return: tuple of two lists: valid and invalid email addresses
    """
    valid_email = []
    invalid_email = []

    for mail in list_email:
        try:
            domain = mail.split('@')[1]
            # Check for MX records
            mx_records = dns.resolver.resolve(domain, 'MX')
            mx_record = str(mx_records[0].exchange)

            # Check mail server availability
            with socket.create_connection((mx_record, 25), timeout=10):
                valid_email.append(mail)
        except Exception:
            invalid_email.append(mail)

    print(f"valid: {valid_email}, invalid: {invalid_email}")
    return valid_email, invalid_email



def domain_and_MX_record_verification(valid_syntax_email: set, invalid_syntax_email: list):
    """
    Функция проверки списка email адресов на валидность домена и наличие MX записи
    :param list_email: список email адресов
    :return: кортеж из двух списков: email адресов с валидным доменом и email адресов с невалидным доменом
    """
    valid_domain_email = []
    invalid_domain_email = []

    # server = smtplib.SMTP()
    # server.set_debuglevel(0)
    count = 0
    for mail in valid_syntax_email:

        print(count)
        try:
            domain = mail.split('@')[1]
            rec = dns.resolver.resolve(domain, 'MX')
            mx_record = rec[0].exchange
            mx_record = str(mx_record)

            # server.connect(mx_record)
            # code, message = server.helo(mail)
            #
            # server.mail(mail)
            # code, message = server.rcpt(str(mail))


            valid_domain_email.append(mail)
            count+=1
        except Exception:
            pass
            invalid_domain_email.append(mail)
    print(f"хорошие {valid_domain_email}")
    return valid_domain_email, invalid_domain_email, invalid_syntax_email




def checking_mail_syntax_in_xlsx(file_name: str, column_name: str):
    """
    Функция проверки email адресов в файле xlsx на валидность
    :param file_name: имя файла
    :param column_name: имя столбца
    """
    valid_email = set()
    invalid_email = []

    workbook = openpyxl.load_workbook(file_name)
    sheet = workbook.active
    cell = sheet[column_name]

    for row in cell:
        if row.value is not None and row.value != "" and row.value != "#" and row.value != "your@email":
            value = row.value.strip().replace('%20', '')
            value = value.split('?')[0]
            value = value.split(';')[0]

            if re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", value) is not None:
                valid_email.add(value)
            else:
                invalid_email.append(value)

    return valid_email, invalid_email

# TODO написать функцию которая принимает эти три списка и записывает их в три разных файла



list_email2 = [
    "55reigen55@mail.ru",
    "55reigen55@gmail.com",
    "55reigen55@dmail.zzz",
    "хуй на руль"
]


print("начало")

list_email = checking_mail_syntax_in_xlsx("Книга1.xlsx", "A")
print("list_email")

domain_and_MX_record_verification(list_email)