from faker import Faker

fake = Faker(locale='en_CA')
moodle_url = 'http://52.39.5.126/'
moodle_users_main_page = 'http://52.39.5.126/admin/user.php'
moodle_login_url = 'http://52.39.5.126/login/index.php'
moodle_username = 'maxotis'
moodle_password = 'CCTBmax11!'
moodle_dashboard_url = 'http://52.39.5.126/my/'
new_username = fake.user_name()
new_password = fake.password()
first_name = fake.first_name()
surname = fake.last_name()
full_name = f'{first_name} {surname}'
email = fake.email()
moodle_net_profile = f'https://moodle.net/{new_username}'
city = fake.city()
description = fake.sentence(nb_words=100)
picture_description = fake.sentence(nb_words=6)
phonetic_name = fake.user_name()
list_of_interests = [new_username, full_name, city, fake.sentence(nb_words=1)]
web_page_url = fake.url()
icq_number = fake.pyint(111111, 999999)
institution = fake.lexify(text = '?????')
department = fake.lexify(text = '?????????')
phone = fake.phone_number()
mobile_phone = fake.phone_number()

# note: The "address" command from fake library, has an embedded command to execute the code. That's why it automatically presses enter.
# To disable this feature, we can replace \n with space, as follows:
# address = fake.address()
address = fake.address().replace('\n', ' ')
