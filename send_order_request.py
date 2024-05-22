from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json

driver = webdriver.Chrome()

driver.get("http://54.251.65.26/wp-admin")

username = driver.find_element_by_id("user_login")
password = driver.find_element_by_id("user_pass")
username.send_keys("vmhoang1703")
password.send_keys("Vmhoang@1703")
password.send_keys(Keys.RETURN)

driver.get("http://54.251.65.26/wp-admin/edit.php?post_type=shop_order")

order_row = driver.find_element_by_css_selector("table.wp-list-table tr.iedit")
order_id = order_row.find_element_by_css_selector("a.row-title").text
customer_email = order_row.find_element_by_css_selector("td.email").text

order_data = {"order_id": order_id, "customer_email": customer_email}
power_automate_webhook = "https://prod-48.southeastasia.logic.azure.com:443/workflows/fa3c914652ed48eeb41f3f50fd9cf43b/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=L3_bjFJQqazRw8LgK5YHi_FJPBh4zP4vzZ5ud501n54"
requests.post(power_automate_webhook, data=json.dumps(order_data))

driver.quit()