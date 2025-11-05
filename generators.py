from faker import Faker

faker = Faker()

def email_generator():
    email = faker.free_email()
    return email

def password_generator():
    password = faker.password(length=10, digits=True, upper_case=True, lower_case=True, special_chars=False)
    return password

def name_generator():
    name = faker.first_name()
    return name