import sys
import datetime
import moodle_locators as locators
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

###
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

def logger():
    old_instance = sys.stdout
    log_file = open('message.log', 'a')
    sys.stdout = log_file
    print(f'Email: {locators.email} \nUsername: {locators.new_username} \nPassword: {locators.new_password}')
    print('--------------')
    sys.stdout = old_instance
    log_file.close()


# Fixture method
# Open web browser and navigate to url
def setUp():
    # Make a full screen
    driver.maximize_window()

    # Let's wait for the browser response in general
    driver.implicitly_wait(30)

    # Navigating to the Moodle app website
    driver.get(locators.moodle_url)

    # Checking that we're on the correct URL address and we're seeing correct title
    if driver.current_url == locators.moodle_url and driver.title == 'Software Quality Assurance Testing':
        print(f'We\'re at Moodle homepage -- {driver.current_url}')
        print(f'We\'re seeing title message -- "Software Quality Assurance Testing"')
        # sleep(5)
        # driver.close()
    else:
        print(f'We\'re not at the Moodle homepage. Check your code!')
        driver.close()
        driver.quit()

# shut down driver
def tearDown():
    if driver is not None:
        print(f'---------------')
        print(f'Test completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

# Log in
def log_in(username, password):
    if driver.current_url == locators.moodle_url:
        driver.find_element(By.LINK_TEXT, 'Log in').click()
        if driver.current_url == locators.moodle_login_url:
            driver.find_element(By.ID, 'username').send_keys(username)
            sleep(0.25)
            driver.find_element(By.ID,'password').send_keys(password)
            sleep(0.25)
            driver.find_element(By.ID, 'loginbtn').click()
            if driver.title == 'Dashboard' and driver.current_url == locators.moodle_dashboard_url:
                print(f'Log in successful. Dashboard present. \n'
                      f'We logged in with Username: {username} and Password: {password}')
            else:
                print(f'Log in not successful. We are not at the dashboard.')

# Create a new user
def create_test_user():
    driver.find_element(By.XPATH, '//span[contains(., "Site administration")]').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users').is_displayed()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(0.25)
    # Enter fake data into username open field
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
    print(locators.new_username)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.surname)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    print(locators.email)
    # Select 'Allow everyone to see my email address'
    Select(driver.find_element(By.ID, 'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    sleep(0.25)
    driver.find_element(By.ID, 'id_moodlenetprofile').send_keys(locators.moodle_net_profile)
    driver.find_element(By.ID, 'id_city').send_keys(locators.city)

    Select(driver.find_element(By.ID, 'id_country')).select_by_visible_text(
        'Canada')
    # or
    # Select(driver.find_element(By.ID, 'id_country')).select_by_value(
    #         'CA')

    Select(driver.find_element(By.ID, 'id_timezone')).select_by_value(
        '99')

    driver.find_element(By.ID, 'id_description_editoreditable').clear()
    driver.find_element(By.ID, 'id_description_editoreditable').send_keys(locators.description)

    # Upload picture to user picture section
    # Click by ' You can drag and drop files here to add them.' section
    driver.find_element(By.CLASS_NAME, 'dndupload-arrow').click()
    sleep(0.25)

    driver.find_element(By.LINK_TEXT, 'Server files').click()
    sleep(0.25)
    # or
    # driver.find_element(By.XPATH, '//span[contains(., "Server files")]').click()
    # or
    # driver.find_element(By.PARTIAL_LINK_TEXT, 'Server files').click()

    driver.find_element(By.PARTIAL_LINK_TEXT, 'Cosmetics').click()
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Biotherm 2021 fall school').click()
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT, 'Course image').click()
    sleep(0.25)
    driver.find_element(By.PARTIAL_LINK_TEXT, 'BT2021fall.png').click()
    sleep(0.50)

    driver.find_element(By.XPATH, '//button[contains(., "Select this file")]').click()
    sleep(0.25)

    driver.find_element(By.ID, 'id_imagealt').send_keys(locators.picture_description)

    driver.find_element(By.PARTIAL_LINK_TEXT, 'Additional names').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstnamephonetic').send_keys(locators.phonetic_name)
    driver.find_element(By.ID, 'id_lastnamephonetic').send_keys(locators.phonetic_name)
    driver.find_element(By.ID, 'id_middlename').send_keys(locators.phonetic_name)
    driver.find_element(By.ID, 'id_alternatename').send_keys(locators.phonetic_name)
    sleep(0.25)
    driver.find_element(By.XPATH, '//a[contains(., "Interests")]').click()
    sleep(0.25)

    # Using for loop, take all items from the list and populate data
    for tag in locators.list_of_interests:
        driver.find_element(By.XPATH, '//div[3]/input').click
        sleep(0.25)
        driver.find_element(By.XPATH, '//div[3]/input').send_keys(tag)
        sleep(0.25)
        driver.find_element(By.XPATH, '//div[3]/input').send_keys(Keys.ENTER)
    sleep(0.25)

    # optional section
    driver.find_element(By.XPATH, '//a[text() = "Optional"]').click()
    driver.find_element(By.CSS_SELECTOR, "input#id_url").send_keys(locators.web_page_url)
    sleep(0.25)
    driver.find_element(By.CSS_SELECTOR, "input#id_icq").send_keys(locators.icq_number)
    driver.find_element(By.CSS_SELECTOR, "input#id_skype").send_keys(locators.new_username)
    driver.find_element(By.CSS_SELECTOR, "input#id_aim").send_keys(locators.new_username)
    driver.find_element(By.CSS_SELECTOR, "input#id_yahoo").send_keys(locators.new_username)
    driver.find_element(By.CSS_SELECTOR, "input#id_msn").send_keys(locators.new_username)
    driver.find_element(By.CSS_SELECTOR, "input#id_idnumber").send_keys(locators.icq_number)
    driver.find_element(By.ID, 'id_institution').send_keys(locators.institution)
    driver.find_element(By.ID, 'id_department').send_keys(locators.department)
    driver.find_element(By.CSS_SELECTOR, 'input#id_phone1').send_keys(locators.phone)
    driver.find_element(By.CSS_SELECTOR, "input#id_phone2").send_keys(locators.mobile_phone)
    driver.find_element(By.CSS_SELECTOR, "input#id_address").send_keys(locators.address)
    sleep(0.25)
    # click "Create user" button
    driver.find_element(By.ID, 'id_submitbutton').click()
    print(f'Test Scenario: Create a new user "{locators.new_username}" --- passed')
    logger()

# Confirm "new user" was created
def confirm_user_created():
    if driver.current_url == locators.moodle_users_main_page and driver.title == 'SQA: Administration: Users: Accounts: Browse list of users':
        assert driver.find_element(By.XPATH, '//h1[text() = "Software Quality Assurance Testing"]').is_displayed()
        if driver.find_element(By.ID, 'fgroup_id_email_grp_label') and driver.find_element(By.NAME, 'email'):
            driver.find_element(By.CSS_SELECTOR, 'input#id_email').send_keys(locators.email)
            driver.find_element(By.CSS_SELECTOR, 'input#id_addfilter').click()
            if driver.find_element(By.XPATH, f'//td[contains(., "{locators.email}")]'):
                print('Test scenario : confirm user created --- passed')

# Confirm that we logged in with new user credentials
def check_we_logged_in_with_new_cred():
    if driver.current_url == locators.moodle_dashboard_url:
        if driver.find_element(By.XPATH, f'//span[contains(., "{locators.full_name}")]').is_displayed():
            print(f'--- User with the name {locators.full_name} is displayed. Test Passed ---')


def delete_test_user():
    assert driver.title == 'Dashboard' and driver.current_url == locators.moodle_dashboard_url
    driver.find_element(By.XPATH, '//span[contains(., "Site administration")]').click()
    driver.find_element(By.LINK_TEXT, 'Users').click()
    driver.find_element(By.LINK_TEXT, 'Browse list of users').click()
    sleep(0.3)
    if driver.find_element(By.ID, 'fgroup_id_email_grp_label').is_displayed() and driver.find_element(By.ID, 'id_email').is_displayed():
        driver.find_element(By.ID, 'id_email').send_keys(locators.email)
        sleep(0.25)
        driver.find_element(By.ID, 'id_addfilter').click()
        sleep(0.25)
        if driver.find_element(By.XPATH, f'//td[contains(., "{locators.email}")]').is_displayed() and driver.find_element(By.XPATH, '//i[@title = "Delete"]').is_displayed():
            driver.find_element(By.XPATH, '//i[@title = "Delete"]').click()
            driver.find_element(By.XPATH, '//button[contains(., "Delete")]').click()
            print(f'User with email address: {locators.email} was deleted')
        else:
            print(f'User was not deleted')


# Log out
def log_out():
    driver.find_element(By.CLASS_NAME, 'userpicture').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//span[contains(., "Log out")]').click()
    sleep(0.25)
    if driver.current_url == locators.moodle_url:
        print(f'Logged out successfully at: {datetime.datetime.now()}')



# #-------------------------------
# ### Create a new user test case
# setUp()
# log_in(locators.moodle_username, locators.moodle_password)
# create_new_user()
# confirm_user_created()
# log_out()
# # tearDown()
# sleep(2)
# #--------------------------------
# ### Log in with new user credentials test case
#
# # setUp()
#
# # Log in with new user credentials
# # log_in(locators.new_username, locators.new_password)
#
# # Confirm that we logged in with the new credentials
# # check_we_logged_in_with_new_cred()
# # log_out()
# # tearDown()
