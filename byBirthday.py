from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import date, timedelta
import mainFunc

# final
def askBirthdayRange():
    while True:
        try:
            StartYear = int(input("Birthday year to Start: ").strip())
            EndYear = int(input("Birthday year to End: ").strip())
            if not(1753 <= EndYear <= 9999 and 1753 <= StartYear <= 9999):
                print("Years must be within range.", end = " ")
                raise ValueError
            if EndYear <= StartYear:
                print("Start cannot be larger than or equal to End.", end = " ")
                raise ValueError
            break
        except KeyboardInterrupt:
            return None
        except:
            print("Please enter correct input!", end = "\n\n")
    return StartYear, EndYear

# final
def askContestantNum():
    while True: 
        try:
            contNum = int(input("Contestant's Number: ").strip())
            if not(1000 <= contNum <= 9999):
                print("Number must be within range.", end = " ")
                raise ValueError
            break
        except KeyboardInterrupt:
            return None
        except:
            print("Please enter correct input!", end = "\n\n")
    return contNum


def mainLoop(driver, years, contNum, selection):
    try:
        select = Select(driver.find_element(By.ID, "cboContest"))
        select.select_by_visible_text(selection)
        
        start_date = date(years[0], 1, 1)
        end_date = date(years[1], 1, 1)
        delta = timedelta(days=1)
        inputElementContestant = driver.find_element(By.ID, "txtConSeq")
        inputElementContestant.clear()
        inputElementContestant.send_keys(str(contNum))
        print("Searching...")
        while start_date <= end_date:
            dateIn = str(start_date.strftime("%m/%d/%Y"))
            inputElementDate = driver.find_element(By.ID, "txtDOB")
            inputElementDate.clear()
            inputElementDate.send_keys(dateIn)
            inputElementDate.send_keys(Keys.ENTER)
            texts = driver.find_element(By.ID, "lblError").text
            if texts == "":
                print("Found!")
                found = True
                name = driver.find_element(By.ID, "lblReportHeader1").text
                school = driver.find_element(By.ID, "lblReportHeader2").text
                # add, would you like to save this as a file
                output = f"{name}: {school}: {selection}: {contNum}: {dateIn}\n"
                print(output)
                save = mainFunc.askSelectable("Would you like to save this information as a file?", ["Yes", "No"])
                if save == "Yes":    
                    mainFunc.saveToFile(output)
                elif save == "No":
                    print(output)
                else:
                    pass
                break
            start_date += delta
        if not found:
            print(f"The contestant doesn't have a birthday within the range {years[0]} - {years[1]}\nor didn't compete in this competion.")
            input("Press Enter to Exit ")
            return True
        else:
            input("Press Enter to Exit ")
            return True
    except:
        return None