from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import byContestant
import byBirthday
import mainFunc
import time
import sys
import os

driver = None
# ends the program, main function called to close the program
def end(driver = None):
    if driver is not None:
        driver.close()
    sys.exit()    

# will open chrome and sent the selenium driver off to be used elsewhere
def openChrome():
    #Opens chrome window
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    try:
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
        driver.get("https://skillsusa-register.org/rpts/EventScoreDetails.aspx")
        time.sleep(1)
        # Selects Texas Comp (final)
        select = Select(driver.find_element(By.ID, "cboEvent"))
        select.select_by_visible_text("TX - 2023 SkillsUSA Texas Leadership and Skills Conference")
        return driver 
    except NoSuchWindowException:
        print("Cancelled by user")
        end(driver)
    except:
        print("Please Download Chrome and Run Again")
        end()

# main function that will run and do the magic i guess
def main():
    found = False
    # Checks to see if they user has an internet connection (final)
    if not mainFunc.attemptConnection("https://skillsusa-register.org/rpts/EventScoreDetails.aspx"): end()

    select = mainFunc.askSelectable("Search with range of", ["Date of Birth", "Contestant Numbers"])
    if select == "Date of Birth":
        contNum = byBirthday.askContestantNum()
        if contNum is None: 
            print("Cancelled by user")
            end()
        years = byBirthday.askBirthdayRange()
        if years is None:
            print("Cancelled by user")
            end()
        selection = mainFunc.selectComp()
        if selection is None: 
            print("Cancelled by user")
            end()

        print("Opening Chrome...")
        driver = openChrome()
        try:
            if byBirthday.mainLoop(driver, years, contNum, selection) is None: end(driver)
        except:
            print("Cancelled by user")
            end()
    elif select == "Contestant Number":
        dateOfBirth = byContestant.askBirthday()
        if dateOfBirth is None: 
            print("Cancelled by user")
            end()
        contNums = byContestant.askContestantRange()
        if contNums is None: 
            print("Cancelled by user")
            end()
        selection = mainFunc.selectComp()
        if selection is None: 
            print("Cancelled by user")
            end()

        print("Opening Chrome...")
        driver = openChrome()
        try:
            if byContestant.mainLoop(driver, contNums, dateOfBirth, selection) is None: end(driver)
        except:
            print("Cancelled by user")
            end()
    else:
        end()

main()