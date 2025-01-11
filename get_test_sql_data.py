from faker import Faker

faker = Faker(locale='zh_CN')

fake_data = {
    "name": faker.name(),
    "email": faker.email(),
    "password": faker.password(),
    'avatar': faker.image_url(),
    'gender': faker.random_element(elements=('男', '女')),
    'age': faker.random_int(min=18, max=60),
    'address': faker.address(),
    'phone': faker.phone_number(),
    'created_at': faker.date_time_this_year(),
    'updated_at': faker.date_time_this_year()
}

print(fake_data)