# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def print_user_param_in_one_string(first_name, last_name, birth_year, city, email, phone_number):
    print(f'{first_name} {last_name},  {birth_year}, {city}, email: {email}, phone number:{phone_number}')


user_first_name = input('Enter your first name: ')
user_last_name = input('Enter your last name: ')
user_birth_year = input('Enter your year of birth: ')
user_city = input('Enter your city: ')
user_email = input('Enter your email address: ')
user_phone_number = input('Enter your phone number: ')


print_user_param_in_one_string(
    first_name=user_first_name,
    last_name=user_last_name,
    birth_year=user_birth_year,
    city=user_city,
    email=user_email,
    phone_number=user_phone_number
)
