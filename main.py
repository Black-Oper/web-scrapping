from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

def selecionarOpcao(num):
    div = driver.find_element(By.CLASS_NAME, 'top-border')
    select = div.find_element(By.CLASS_NAME, 'tb-select')
    optionList = select.find_elements(By.TAG_NAME, 'option')
    if len(optionList) > num:
        optionList[num].click()


def adicionarListaPagina(arq, type):
    div = driver.find_element(By.CLASS_NAME, 'col-xs-9')
    h4List = div.find_elements(By.TAG_NAME, 'h4')

    unique_texts = set()

    with open(arq, type) as f:
        for h4 in h4List:
            if h4.text not in unique_texts and h4.text != '':
                f.write(h4.text + '\n')


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.bestbuy.com')

div = driver.find_element(By.CLASS_NAME, 'country-selection')
a = div.find_element(By.CLASS_NAME, 'us-link')
a.click()

sleep(1.5)

div = driver.find_element(By.CLASS_NAME, 'top-nav')
input1 = div.find_element(By.CLASS_NAME, 'search-input')
input1.send_keys('notebook')

input1.send_keys(Keys.RETURN)

sleep(1.5)

selecionarOpcao(1)

sleep(1.5)

adicionarListaPagina('best-sell.txt', 'w')

sleep(1.5)

div = driver.find_element(By.CLASS_NAME, 'footer-pagination')
auxList = div.find_elements(By.TAG_NAME, 'a')
auxList[1].click()

sleep(1.5)

adicionarListaPagina('best-sell.txt', 'a')

sleep(1.5)

div = driver.find_element(By.CLASS_NAME, 'footer-pagination')
auxList = div.find_elements(By.TAG_NAME, 'a')
auxList[2].click()

sleep(1.5)

adicionarListaPagina('best-sell.txt', 'a')

sleep(1.5)

selecionarOpcao(2)

sleep(1.5)

adicionarListaPagina('best-discount.txt', 'w')

sleep(1.5)

div = driver.find_element(By.CLASS_NAME, 'footer-pagination')
auxList = div.find_elements(By.TAG_NAME, 'a')
auxList[1].click()

sleep(1.5)

adicionarListaPagina('best-discount.txt', 'a')

sleep(1.5)

div = driver.find_element(By.CLASS_NAME, 'footer-pagination')
auxList = div.find_elements(By.TAG_NAME, 'a')
auxList[2].click()

sleep(1.5)

adicionarListaPagina('best-discount.txt', 'a')

sleep(1.5)

selecionarOpcao(3)

sleep(1.5)

adicionarListaPagina('price-low-high.txt', 'w')

sleep(1.5)

div = driver.find_element(By.CLASS_NAME, 'footer-pagination')
auxList = div.find_elements(By.TAG_NAME, 'a')
auxList[1].click()

sleep(1.5)

adicionarListaPagina('price-low-high.txt', 'a')

sleep(1.5)

div = driver.find_element(By.CLASS_NAME, 'footer-pagination')
auxList = div.find_elements(By.TAG_NAME, 'a')
auxList[2].click()

sleep(1.5)

adicionarListaPagina('price-low-high.txt', 'a')

sleep(3)


def find_common_items(file1, file2, file3):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'r') as f3:
        list1 = f1.read().splitlines()
        list2 = f2.read().splitlines()
        list3 = f3.read().splitlines()

    common_items = set(list1) & set(list2) & set(list3)

    return common_items


def add_common_items_to_file(common_items, filename):
    with open(filename, 'w') as f:
        for item in list(common_items)[:5]:
            f.write(item + '\n')


common_items = find_common_items('best-sell.txt', 'best-discount.txt', 'price-low-high.txt')
add_common_items_to_file(common_items, 'common_items.txt')

driver.quit()
