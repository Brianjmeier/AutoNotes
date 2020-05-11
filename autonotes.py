import README
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import gkeepapi
from selenium.webdriver.common.action_chains import ActionChains

def itemize(items):
    res = []
    for item in items:
        if item[-1] == '#':
            res.append((item[:-1], True))
        else:
            res.append((item, False))
    return res


class AutoNotes:
    def __init__(self, whatsapp, qr_time):
        self.driver = webdriver.Firefox() if README.browser else webdriver.Chrome()
        self.web = whatsapp
        self.qr_time = qr_time
        self.keep = gkeepapi.Keep()
        self.email = README.email
        self.password = README.password

    def get_notes(self):
        self.driver.get(self.web)
        time.sleep(self.qr_time)
        xpath = "//*[@title='{}']".format(README.group_name)
        elem = self.driver.find_element_by_xpath(xpath)
        elem.click()
        notes_ob = self.driver.find_elements_by_class_name("_3zb-j")
        time.sleep(1)
        notes = list(map(lambda note_ob: note_ob.text, notes_ob))
        return notes

    def clear_notes(self):
        empty_chat = self.driver.find_element_by_class_name("wml2-")
        action_chains = ActionChains(self.driver)
        action_chains.context_click(empty_chat).perform()
        time.sleep(1)
        clear = self.driver.find_element_by_xpath("//*[@title='Clear messages']")
        clear.click()
        time.sleep(1)
        delete = self.driver.find_element_by_xpath("//div[contains(text(),'Clear')]")
        delete.click()

    def close_driver(self):
        self.driver.close()

    def keep_log_in(self):
        self.keep.login(self.email, self.password)

    def keep_sync(self):
        self.keep.sync()

    def create_notes(self, notes):
        for note in notes:
            try:
                title, text = note.split(' - ')
            except:
                print("Please write notes in the correct format.")
            try:
                star, title = title.split('*')
                texts = text.split(', ')
                items = itemize(texts)
                self.keep.createList(title, items)
            except:
                self.keep.createNote(title, text)


if __name__ == '__main__':
    auto_notes = AutoNotes('https://web.whatsapp.com', 7)
    notes = auto_notes.get_notes()
    auto_notes.clear_notes()
    auto_notes.close_driver()
    auto_notes.keep_log_in()
    auto_notes.create_notes(notes)
    auto_notes.keep_sync()
