from faker import Faker

faker = Faker()


def generate_username():
    return faker.name()


def generate_email():
    return faker.email()


def generate_password():
    return faker.password(length=8, digits=True)


def generate_user_data():
    email = generate_email()
    password = generate_password()
    name = generate_username()
    return email, password, name