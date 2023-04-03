from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import mainFunc

def askBirthday():
    while True:
        try:
            while True:
                try:
                    month = int(input("Enter DOB Month: ").strip())
                    if not(1 <= month <= 12):
                        print("month must be valid.", end = " ")
                        raise ValueError
                    break
                except KeyboardInterrupt:
                    return None
                except:
                    print("Please enter correct input!", end = "\n\n")
            while True:
                try:
                    day = int(input("Enter DOB Day: ").strip())
                    if not(1 <= day <= 31):
                        print("day must be valid.", end = " ")
                        raise ValueError
                    break
                except KeyboardInterrupt:
                    return None
                except:
                    print("Please enter correct input!", end = "\n\n")
            while True:
                try:
                    year = int(input("Enter DOB Year: ").strip())
                    if not(1753 <= year <= 9999):
                        print("year must be valid.", end = " ")
                        raise ValueError
                    break
                except KeyboardInterrupt:
                    return None
                except:
                    print("Please enter correct input!", end = "\n\n")
            date = datetime.date(year, month, day)
            date = str(date.strftime("%m/%d/%Y"))
            return date
        except ValueError:
            print("Invalid Date\n")
        except KeyboardInterrupt:
            return None   

def askContestantRange():
    while True:
        try:
            StarNum = int(input("Contestant number to Start: ").strip())
            EndNum = int(input("Contestant number to End: ").strip())
            if not(1000 <= StarNum <= 9999 and 1000 <= EndNum <= 9999):
                print("Contestnat number must be within range.", end = " ")
                raise ValueError
            if EndNum <= StarNum:
                print("Start cannot be larger than or equal to End.", end = " ")
                raise ValueError
            break
        except KeyboardInterrupt:
            return None
        except:
            print("Please enter correct input!", end = "\n\n")
    return StarNum, EndNum

def mainLoop(driver, contNums, DOB, selection):
    try:
        found = False
        select = Select(driver.find_element(By.ID, "cboContest"))
        select.select_by_visible_text(selection)
        inputElementDate = driver.find_element(By.ID, "txtDOB")
        inputElementDate.clear()
        inputElementDate.send_keys(DOB)
        print("Searching...")
        for i in range(contNums[0], contNums[1]+1):
            inputElementContestant = driver.find_element(By.ID, "txtConSeq")
            inputElementContestant.clear()
            inputElementContestant.send_keys(str(i))
            inputElementContestant.send_keys(Keys.ENTER)
            texts = driver.find_element(By.ID, "lblError").text
            if texts == "":
                print("Found!")
                found = True
                name = driver.find_element(By.ID, "lblReportHeader1").text
                school = driver.find_element(By.ID, "lblReportHeader2").text
                # add, would you like to save this as a file
                output = f"{name}: {school}: {selection}: {i}: {DOB}\n"
                print(output)
                save = mainFunc.askSelectable("Would you like to save this information as a file?", ["Yes", "No"])
                if save == "Yes":
                    mainFunc.saveToFile(output)
                elif save == "No":
                    print(output)
                else:
                    pass
                break
        if not found:
            print(f"This DOB doesn't have the contestant number within the range {contNums[0]} - {contNums[1]}\nor didn't compete in this competion.")
            input("Press Enter to Exit ")
            return True
        else:
            input("Press Enter to Exit ")
            return True
    except:
        return None