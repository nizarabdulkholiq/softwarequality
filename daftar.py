from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

#mengambil halaman web yang aman di tes
driver.get("https://nizarabdulkholiq.github.io/ProjectDadakan/daftar")  # Ganti dengan jalur absolut ke file HTML Anda


time.sleep(2)

#get by id untuk filed yang akan di isi
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("zayni")

email_field = driver.find_element(By.ID, "email")
email_field.send_keys("zay@gmail.com")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("123456")

phone_field = driver.find_element(By.ID, "nomorTelepon")
phone_field.send_keys("081292763456")

address_field = driver.find_element(By.ID, "alamat")
address_field.send_keys("123 Street, City")

3get submit button
submit_button = driver.find_element(By.CLASS_NAME, "signup-button")
submit_button.click()


time.sleep(5)


