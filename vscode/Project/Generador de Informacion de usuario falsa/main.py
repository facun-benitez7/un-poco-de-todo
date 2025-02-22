from faker import Faker  # pip install faker

fake = Faker()

for _ in range(0, 10):
    name = fake.name()
    addr = fake.address()
    print(f'{name} => {addr}')
