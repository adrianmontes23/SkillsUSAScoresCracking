from urllib.request import urlopen
import inquirer
import time

def attemptConnection(LINK):
    try:
        for i in range(10):
            try:
                if urlopen(LINK): break
            except:
                print("Please Connect to a network. Retrying...")
                time.sleep(3)
        if i == 9:
            print("No Connection Found")
            return False
        return True
    except KeyboardInterrupt:
        print("Cancelled by user")
        return False
    except Exception as E:
        print(E)


def askSelectable(question, choices):
    try:
        questions = [inquirer.List('choice', 
            message=question,
            choices=choices,),]
        answers = inquirer.prompt(questions)
        return(answers["choice"])
    except:
        return None

def saveToFile(output):
    try:
        with open("Contestants.txt", "x") as f:
            f.write(output)  
        print("The file has been saved in the same folder as the program")
        
    except FileExistsError:
        with open("Contestants.txt", "a") as f:
            f.write(output)
        print(output)

def selectComp():
    return askSelectable("Select a competition", 
        
["3D Visualization and Animation - Secondary",
"Action Skills - Secondary",
"Additive Manufacturing - Secondary",
"Advertising Design - Secondary",
"American Spirit - Secondary",
"Applied Engineering - Secondary",
"Architectural Drafting - Secondary",
"Automobile Maintenance & Light Repair - Secondary",
"Automotive Refinishing Technology - Secondary",
"Automotive Service Quiz Bowl - Secondary",
"Automotive Service Technology - Secondary",
"Automotive Tool ID - Secondary",
"Aviation Maintenance Technology - Secondary",
"Barbering - Secondary",
"Basic Health Care Skills - Secondary",
"Broadcast News Production (Video News Production) - Secondary",
"Building Maintenance - Secondary",
"Building Search - Secondary",
"Cabinetmaking - Secondary",
"Career Pathway (HTHS) Health Science - Secondary",
"Career Pathway (IET) Architecture & Construction - Secondary",
"Career Pathway (IET) Manufacturing - Secondary",
"Career Pathway (IET) Science, Technology & Math - Secondary",
"Career Pathway (IET) Transport, Distribute & Logistics - Secondary",
"Career Promotion Demonstration - Secondary",
"Carpentry - Secondary",
"Chapter Business Procedure - Secondary",
"Chapter Display - Secondary",
"CNC 5 Axis (CNC 5 Axis Milling Programmer) - Secondary",
"Collision Damage Appraisal - Secondary",
"Collision Repair Technology - Secondary",
"Commercial Baking (Baking & Pastry Arts) - Secondary",
"Commercial UAS Drone - Secondary",
"Community Emergency Response Team - Secondary",
"Community Service - Secondary",
"Computer Programming - Secondary",
"Construction Materials ID - Secondary",
"Construction Tool ID - Secondary",
"Cosmetology - Secondary",
"Cosmetology 3D Freehand Nail Art Acrylic - Secondary",
"Cosmetology Quiz Bowl - Secondary",
"Crime Scene Investigation - Secondary",
"Criminal Justice - Secondary",
"Criminal Justice Quiz Bowl - Secondary",
"Culinary Arts - Secondary",
"Culinary Arts Quiz Bowl - Secondary",
"Customer Service - Secondary",
"Cyber Security - Secondary",
"Dental Assisting - Secondary",
"Diesel Equipment Technology - Secondary",
"Digital Cinema Production - Secondary",
"Early Childhood Education - Secondary",
"Electrical Construction Wiring - Secondary",
"Emblem Ceremony - Secondary",
"Emergency Medical Technician - Secondary",
"Engineering Technology/Design - Secondary",
"Entrepreneurship - Secondary",
"Esthetics - Secondary",
"Extemporaneous Speaking - Secondary",
"Felony Traffic Stop - Secondary",
"First Aid-CPR - Secondary",
"Forensic Science Team - Secondary",
"Health Knowledge Bowl - Secondary",
"Health Occupations Professional Portfolio - Secondary",
"Heating, Ventilation, Air Conditioning and Refrigeration - Secondary",
"Information Technology Services - Secondary",
"Interactive Application & Game Development - Secondary",
"Internet of Things Smart Home - Secondary",
"Internetworking - Secondary",
"IT Quiz Bowl - Secondary",
"Job Interview - Secondary",
"Job Skill Demonstration A - Secondary",
"Job Skill Demonstration Open - Secondary",
"Land Surveying - Secondary",
"Marine Service Technology - Secondary",
"Mechanical Drafting - Secondary",
"Mechatronics - Secondary",
"Medical Assisting - Secondary",
"Medical Math - Secondary",
"Medical Terminology - Secondary",
"Mobile Robotic Technology - Secondary",
"Motorcycle Service Technology - Secondary",
"Nail Art - Secondary",
"Nail Care - Secondary",
"National Electrical Code Test - Secondary",
"Nurse Assisting - Secondary",
"Occupational Health & Safety Multiple - Secondary",
"Occupational Health & Safety Single - Secondary",
"Opening and Closing Ceremonies - Secondary",
"Photography - Secondary",
"Pin Design - Secondary",
"Plumbing - Secondary",
"Power Equipment Technology - Secondary",
"Practical Nursing - Secondary",
"Precision Machining Technology - Secondary",
"Prepared Speech - Secondary",
"Principles of Engineering/Technology - Secondary",
"Promotional Bulletin Board - Secondary",
"Quiz Bowl - Secondary",
"Related Technical Math - Secondary",
"Residential Commericial Appliance Technology - Secondary",
"Restaurant Service - Secondary",
"Robotics & Automation Technology - Secondary",
"Robotics Urban Search and Rescue - Secondary",
"Sheet Metal - Secondary",
"SkillsUSA Texas Outstanding Member - Secondary",
"T-Shirt Design - Secondary",
"TeamWorks - Secondary",
"Technical Computer Applications - Secondary",
"Telecommunications Cabling - Secondary",
"Television (Video) Production - Secondary",
"Web Design & Development - Secondary",
"Welding - Secondary",
"Welding 1 - Secondary",
"Welding Applications - Secondary",
"Welding Fabrication - Secondary",
"Welding Sculpture - Secondary"])

