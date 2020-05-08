import README
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox() if README.browser else webdriver.Chrome()

# Get new note from Whatsapp
driver.get('https://web.whatsapp.com')
time.sleep(5)
xpath = "//*[@title='{}']".format(README.group_name)
elem = driver.find_element_by_xpath(xpath)
elem.click()
notes_ob = driver.find_elements_by_class_name("_3zb-j")
time.sleep(1)
notes = list(map(lambda note_ob: note_ob.text,notes_ob))

# Clear saved notes.
emptychat = driver.find_element_by_class_name("wml2-")
actionChains = ActionChains(driver)
actionChains.context_click(emptychat).perform()
time.sleep(1)
clear = driver.find_element_by_xpath("//*[@title='Clear messages']")
clear.click()
time.sleep(1)
delete = driver.find_element_by_xpath("//div[contains(text(),'Clear')]")
delete.click()
driver.close()


# Create note/list in Keep
import gkeepapi
keep = gkeepapi.Keep()
keep.login(README.email,README.password)


for note in notes:
    title, text = note.split(' - ')
    try:
        star,title = title.split('*')
        # We've got a list!
        items = []
        items_text = text.split(', ')
        for item_text in items_text:
            items.append((item_text, False))
        glist = keep.createList(title, items)
    except:
        gnote = keep.createNote(title, text)

keep.sync()
