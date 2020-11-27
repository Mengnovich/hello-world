# Define user credentials - only change this part!
vorname = ''
Nachname = ''
email = ''
password = ''

# Initial Chrome driver
from selenium import webdriver
driver = webdriver.Chrome()

# Set implicitly waiting time
driver.implicitly_wait(10)

# Open webpage
driver.get('https://seatable.io/registrierung/')

# Accept cookies by saving current selections
driver.find_element_by_css_selector('a#CookieBoxSaveButton._brlbs-btn._brlbs-cursor').click()

# Enter first name, last name, email and password
driver.find_element_by_css_selector('input#input_3_1.medium').send_keys(vorname);
driver.find_element_by_css_selector('input#input_3_2.medium').send_keys(Nachname);
driver.find_element_by_css_selector('input#input_3_5.medium').send_keys(email);
driver.find_element_by_css_selector('input#input_3_4.medium').send_keys(password);

# Accept the Terms of Use
driver.find_element_by_css_selector('input#input_3_8_1').click();

# Click on the Register now button
driver.find_element_by_css_selector('input#gform_submit_button_3.gform_button.button').click()

