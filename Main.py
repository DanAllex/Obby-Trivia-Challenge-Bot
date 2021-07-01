from ahk import AHK
import time
# cv2.cvtColor takes a numpy ndarray as an argument
import numpy as nm
import pytesseract
# importing OpenCV
import cv2
from PIL import ImageGrab, Image, ImageEnhance
import PIL.ImageOps
import pymongo
from waiting import wait
import random

client = pymongo.MongoClient("mongodb://localhost:27017/")
database = client["TriviaQA"]
collection = database["Questions"]

for x in collection.find():
  print(x)

#x = collection.delete_many({})

#print(x.deleted_count, " documents deleted.")

#newEntry = { "Question": "Sample Question", "Answer": "Sample answer" }
#collection.insert_one(newEntry)


pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'

ahk = AHK()

def activateProgram(name, xCoord, yCoord, xSize, ySize):
    win = ahk.find_window(title=name) # Find the opened window
    win.activate() # Give the window focus
    win.move(x=xCoord, y=yCoord, width=xSize, height=ySize)

def exitProgram(name):
    win = ahk.find_window(title=name)
    win.close()

def chat(Text):
    ahk.key_press('/')
    ahk.type(Text)
    ahk.key_press('Enter')

def getStringfromImage(x1, y1, x2, y2, foreground):
    background = ImageGrab.grab(bbox =(x1, y1, x2, y2))
    foreground = Image.open(foreground)
    background.paste(foreground, (0, 0), foreground.convert('RGBA'))
    colorFilter = ImageEnhance.Color(background)
    new_image = colorFilter.enhance(0)
    brightnessFilter = ImageEnhance.Brightness(new_image)
    new_image2 = brightnessFilter.enhance(0.025)
    contrastFilter = ImageEnhance.Contrast(new_image2)
    new_image3 = contrastFilter.enhance(100)
    final_image = PIL.ImageOps.invert(new_image3)

    #final_image.show()
    tesstr = pytesseract.image_to_string(
                cv2.cvtColor(nm.array(final_image), cv2.COLOR_BGR2GRAY), 
                lang ='eng')

    if str.strip(tesstr) == "":
        tesstr = pytesseract.image_to_string(
                cv2.cvtColor(nm.array(final_image), cv2.COLOR_BGR2GRAY), 
                lang ='eng', config=("-c tessedit"
                  "_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
                  " --psm 10"
                  " -l osd"
                  " "))
    
    return tesstr



def checkForEvent(change):
    if change:
        return True
    return False

newGame = ["gonna be a ez game", "hyped", "u guys ready?", "wooow"]
voteReady = ["guys vote ready", "ready", "VOTE READY", "hurry guys, vote ready", "voted ready", "vote", "skip", "SKIP", "skip guys", "everyone skip"]
questionRight = ["lol that was such an easy question", "ez", "wooow", "?????", "imagine getting that wrong", "common sense", "ngl, that was rlly easy", "learned this in college", "my phd didnt go to waste"]
questionWrong = ["ngl, that was pretty hard", "these questions r impossible", "howd i get that wrong???", "misclicked", "shoot", "????", "woooow", "bruhhhh"]

activateProgram(b"Roblox", 0, 0, 1300, 900)
print("ACTIVATED")

while True:
    print("Waiting for an event")
    wait(lambda: ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesSmallServer.png') is not None or ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesPlatformSkins.png') is not None or ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesNewGame.png') is not None or ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesGameProgress.png') is not None or ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesVoteSkip.png') is not None or ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesQuestionBox.png') is not None or (ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesSpectate1.png') is not None and ahk.pixel_get_color(325, 866) == "0x00B400") or (ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesSpectate2.png') is not None and ahk.pixel_get_color(325, 866) == "0xFF6400"), timeout_seconds=250, waiting_for="Changed Event")
    print("Event happened")
    if ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesSmallServer.png') is not None:
        exitProgram(b"Roblox")
        ahk.mouse_move(random.randrange(1054,1305), random.randrange(399,433), speed=random.randrange(8,11), relative=False)
        ahk.click()
        time.sleep(3.5)
        activateProgram(b"Roblox", 0, 0, 1300, 900)
    elif ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesGameProgress.png'):
        print("Game Progress appeared")
        ahk.mouse_move(random.randrange(792,934), random.randrange(598,610), speed=random.randrange(8,11), relative=False)
        ahk.click()
    elif ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesPlatformSkins.png'):
        print("PlatformSkins appeared")
        ahk.mouse_move(random.randrange(680,880), random.randrange(690,713), speed=random.randrange(8,11), relative=False)
        ahk.click()
    elif ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesNewGame.png') is not None:
        chosen = random.randrange(1, 3)
        if chosen == 1:
            time.sleep(random.randrange(3, 5) / 10.0)
            chat(random.choice(newGame))
        wait(lambda: checkForEvent(ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesNewGame.png') is None), timeout_seconds=30, waiting_for="Question to go away")
    elif ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesVoteSkip.png'):
        print("Vote skip appeared")
        ahk.mouse_move(random.randrange(503,797), random.randrange(701,744), speed=random.randrange(8,11), relative=False)
        ahk.click()
        chosen = random.randrange(1, 2)
        if chosen == 1:
            time.sleep(random.randrange(3, 5) / 10.0)
            chat(random.choice(voteReady))
        ahk.mouse_move(0, 0, speed=random.randrange(8,11), relative=False)
        wait(lambda: checkForEvent(ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesVoteSkip.png') is None and ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesIntro1.png') is None and ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesIntro2.png') is None and ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesIntro3.png') is None and ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesIntro4.png') is None), timeout_seconds=50, waiting_for="Vote Skip to go Away")
    elif ahk.pixel_get_color(363, 517) == "0x00A0FF" and ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesQuestionBox.png') is not None and ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesCongratulations.png') is None and ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesIntro1.png') is None and ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesIntro2.png') is None and ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesIntro3.png') is None and ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesIntro4.png') is None:
        print("Going to answer a question")
        time.sleep(2)
        Question = str.strip(getStringfromImage(265, 513, 1034, 573, "C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesQuestionMask.png"))
        print("The question is: " + Question)
        if Question is not None:
            query = { "Question": Question }
            matches = collection.find_one(query)
            if matches is None:
                answer = None

                randomAnswer = random.randrange(1,4)
                if randomAnswer == 1:
                    ahk.mouse_move(random.randrange(479,820), random.randrange(598,631), speed=random.randrange(8,11), relative=False)
                    ahk.click()
                elif randomAnswer == 2:
                    ahk.mouse_move(random.randrange(479,820), random.randrange(648,682), speed=random.randrange(8,11), relative=False)
                    ahk.click()
                elif randomAnswer == 3:
                    ahk.mouse_move(random.randrange(479,820), random.randrange(695,731), speed=random.randrange(8,11), relative=False)
                    ahk.click()
                elif randomAnswer == 4:
                    ahk.mouse_move(random.randrange(479,820), random.randrange(746,782), speed=random.randrange(8,11), relative=False)
                    ahk.click()
                    
                ahk.mouse_move(0, 0, speed=random.randrange(8,11), relative=False)

                wait(lambda: checkForEvent(ahk.pixel_get_color(670, 595) == '0x00B400' or ahk.pixel_get_color(670, 645) == '0x00B400' or ahk.pixel_get_color(670, 694) == '0x00B400' or ahk.pixel_get_color(670, 744) == '0x00B400'), timeout_seconds=30, waiting_for="Answer")
                if ahk.pixel_get_color(670, 595) == '0x00B400':
                    answer = str.strip(getStringfromImage(457, 595, 842, 635, "C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesCorrectMask.png"))
                elif ahk.pixel_get_color(670, 645) == '0x00B400':
                    answer = str.strip(getStringfromImage(457, 645, 842, 685, "C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesCorrectMask.png"))
                elif ahk.pixel_get_color(670, 694) == '0x00B400':
                    answer = str.strip(getStringfromImage(457, 694, 842, 734, "C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesCorrectMask.png"))
                elif ahk.pixel_get_color(670, 744) == '0x00B400':
                    answer = str.strip(getStringfromImage(457, 744, 842, 784, "C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesCorrectMask.png"))

                if answer is not None:
                    newEntry = { "Question": Question, "Answer": answer }
                    collection.insert_one(newEntry)
                    print("Answer (" + answer + ") added")
                else:
                    print("Failed to see answer")
                if ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesWrong.png', upper_bound=(439, 586), lower_bound=(856, 789)) is not None:
                    chosen = random.randrange(1, 7)
                    if chosen == 1:
                        time.sleep(random.randrange(3, 5) / 10.0)
                        chat(random.choice(questionWrong))
            else:
                answer = matches.get("Answer")
                print(answer)
                chosen = random.randrange(1, 5)
                if chosen == 1:
                    time.sleep(random.randrange(3, 5) / 10.0)
                    chat(random.choice(questionRight))

                if str.strip(getStringfromImage(457, 595, 842, 635, "C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesChoiceMask.png")) == answer:
                    ahk.mouse_move(random.randrange(457, 645), random.randrange(598,631), speed=random.randrange(8,11), relative=False)
                    ahk.click()
                    time.sleep(random.randrange(3, 5) / 10.0)
                    chat(str.strip(getStringfromImage(457, 645, 842, 685, "C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesChoiceMask.png")))
                elif str.strip(getStringfromImage(457, 645, 842, 685, "C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesChoiceMask.png")) == answer:
                    ahk.mouse_move(random.randrange(479,820), random.randrange(648,682), speed=random.randrange(8,11), relative=False)
                    ahk.click()
                    time.sleep(random.randrange(3, 5) / 10.0)
                    chat(str.strip(getStringfromImage(457, 595, 842, 635, "C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesChoiceMask.png")))
                elif str.strip(getStringfromImage(457, 694, 842, 734, "C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesChoiceMask.png")) == answer:
                    ahk.mouse_move(random.randrange(479,820), random.randrange(695,731), speed=random.randrange(8,11), relative=False)
                    ahk.click()
                    time.sleep(random.randrange(3, 5) / 10.0)
                    chat(str.strip(getStringfromImage(457, 595, 842, 635, "C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesChoiceMask.png")))
                else:
                    ahk.mouse_move(random.randrange(479,820), random.randrange(746,782), speed=random.randrange(8,11), relative=False)
                    ahk.click()
                    time.sleep(random.randrange(3, 5) / 10.0)
                    chat(str.strip(getStringfromImage(457, 595, 842, 635, "C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesChoiceMask.png")))
                
                ahk.mouse_move(0, 0, speed=random.randrange(8,11), relative=False)

        wait(lambda: checkForEvent(ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesQuestionBox.png') is None), timeout_seconds=100, waiting_for="Question to go away")
    elif (ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesSpectate1.png') is not None and ahk.pixel_get_color(325, 866) == "0x00B400") or (ahk.image_search('C:/Users/danny/Documents/Files/Obby-Trivia-Challenge-Bot/ImagesSpectate2.png') is not None and ahk.pixel_get_color(325, 866) == "0xFF6400"):
        time.sleep(3)
        ahk.mouse_move(random.randrange(327,513), random.randrange(862,879), speed=random.randrange(8,11), relative=False)
        ahk.click()