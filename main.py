from service.client import Service


def main():
    # Инициализируем сервис, в итоге получим свежую информацию с сайта
    service = Service()
    # Запишем всю информацию в файл JSON
    service.write_to_file()
    # Ищем вакансии по профессии
    user_input = input("Какую IT профессию вы хотите найти? ")
    service.find_by_name(user_input)
    # Ищем вакансии по зарплате
    user_input = int(input("Какая зарплата вас бы устроила? "))
    service.find_by_salary(user_input)


if __name__ == "__main__":
    main()
