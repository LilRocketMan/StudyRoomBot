import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

hiddenCheck = "hidden"

driver = webdriver.Firefox()  # Optional argument, if not specified will search path.
driver.get("http://root.evanced.info/uvu/evanced/roomrequest.asp?mm=1")
time.sleep(1) # Let the user actually see something!
library_room_options = driver.find_element_by_id('td1').click()
print("The Times Avaible are")
for i in range(50, 25, -1):
    roomNumber = driver.find_element_by_id('roomlist'+str(i))
    print(roomNumber.text)
    roomNumber.click()
   
    for j in range(32):
        roomTime = driver.find_element_by_name('TimeBox' + str(j))
        if roomTime.find_element_by_name('disabled').size() == 0:
            print(roomTime.text)
        
            
        
        
        
   
        #print(driver.find_element_by_name('TimeBox' + str(i)).get_attribute("value"))
    
    
#driver.find_element_by_id('roomlist47').click()
#driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td[2]/div/table/tbody/tr[2]/td/table/tbody/tr[31]/td[1]/input").click()
#driver.find_element_by_xpath("/html/body/form/table/tbody/tr/td [2]/div/table/tbody/tr[2]/td/div[3]/input[1]").click()
#time.sleep(10) # Let the user actually see something!
#driver.quit()

#driver.get("http://www.python.org")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.clear() 
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()