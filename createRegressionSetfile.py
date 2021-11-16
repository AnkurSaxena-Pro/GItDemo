import time
import argparse
import pip

package_installer = ['selenium','requests']   #package to install
pip.main(['install'] + package_installer + ['--upgrade'])
# --upgrade is to install or upgrade package

from selenium import webdriver

#update after cloning from git



# Start Google Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


parser = argparse.ArgumentParser()
parser.add_argument("ipStr")
parser.add_argument("baseline")

args = parser.parse_args()

baseline = args.baseline
ipStr = args.ipStr

driver = webdriver.Chrome()

# Open Google.com
driver.get('http://cipgweb/testresults/results.jsp?status=regression&plat=0')

op1 = Select(driver.find_element_by_xpath("//*[@id='selectProject']"))
op1.select_by_visible_text('ADNX')
print(op1)
time.sleep(3)
op2 = driver.find_element_by_xpath("/html/body/form/p/table/tbody/tr/td[2]/table/tbody/tr[4]/td[1]")
print(op2)

op3 = Select(
    driver.find_element_by_xpath("/html/body/form/p/table/tbody/tr/td[1]/fieldset[2]/table/tbody/tr[1]/td[2]/select"))

op3.select_by_visible_text(ipStr)
time.sleep(3)
op3 = Select(driver.find_element_by_xpath("//*[@id='selectGroup']"))

try:

    op3.select_by_visible_text(baseline)
except:
    try:
        driver.close()
    except:
        pass

'''Take screen shot
element = driver.find_element_by_class_name("side")
driver.save_screenshot(screenshotFn)
return driver, element, ''
'''



T_body = driver.find_element_by_id("sortBody")
rows = T_body.find_elements_by_tag_name("tr")
# handle exception when t_body is not present



with open("D:\\workdir\\setfile\\test.set",'w',encoding = 'utf-8') as f:
    for row in rows:
        f.write((row.find_elements_by_tag_name('td')[1]).text)
        f.write('.seq\n')


driver.close()

