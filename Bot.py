import AI
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

def EnterForm():
    #url = input("Enter form URL: ")
    url = "https://docs.google.com/forms/d/e/1FAIpQLSfgq-HEtgUvYgGHB1oDqvmTJO9XR6EvIxLHv1kW8j9aZowW5w/viewform"
    driver.get(url)

def DetectQuestions():
    questionElements = driver.find_elements("class name","M7eMe")
    questionBoxs = driver.find_elements("class name","Qr7Oae")

    return questionElements , questionBoxs

def DetectAnswerType(questionBox):
    counter = 0
    answerTypes = ["MocG8c HZ3kWc mhLiyf LMgvRb KKjvXb DEh1R" , "whsOnd zHQkBf" , "d7L4fc bJNwt  FXLARc aomaEc ECvBRb" , "YEVVod"]
    for i in answerTypes:
        try:
            questionBox.find_element("class name",i)
            return counter
        except:
            counter = counter + 1

def DetectAnswers(answerType,questionBox):
    answerTypes = ["MocG8c HZ3kWc mhLiyf LMgvRb KKjvXb DEh1R" , "whsOnd zHQkBf" , "d7L4fc bJNwt  FXLARc aomaEc ECvBRb" , "YEVVod"]
    return questionBox.find_element("class name",answerTypes[answerType])

def Start():
    EnterForm()

Start()

input("Thanks for using our service ...")