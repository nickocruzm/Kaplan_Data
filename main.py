import pytesseract
from PIL import Image
import pandas as pd
import os


cwd = os.getcwd()
if("Kaplan_Data" not in cwd):
    DATA_IMAGES_PATH = f'{cwd}/Kaplan_Data/data/images/'
else:
    DATA_IMAGES_PATH = f'{cwd}/data/images/'
  
imgCount = 1

# each element is a quiz formatted as a string.
quizzes = list()

for fileName in os.listdir(DATA_IMAGES_PATH):
    
    if fileName.endswith(".png"):
        if(not fileName[0].isdigit()):
            oldName = fileName
            fileName = imgCount + '.png'
            
            os.rename(DATA_IMAGES_PATH + oldName, DATA_IMAGES_PATH + fileName)
        
        imgCount = imgCount + 1
        img = Image.open(DATA_IMAGES_PATH + fileName)
        quizzes.append(pytesseract.image_to_string(img))

# iterate through images list and filter into buckets

Quiz = {
    "Question": [],
    "Subject": [],
    "Difficulty":[],
    "Duration":[],
    "Correct":[]
}


for quiz in quizzes:
    quiz_data = quiz.split()
    for x in quiz_data: 
        if(x in ['~v','xo','v','Vv']):
            Quiz["Correct"].append(1)
        elif(x == "Number" or x == "Data"):
            sub = x
        elif(x == "Properties" or x == "Interpretation"):
            sub += x
            Quiz["Subject"].append(sub)
            sub = ""
        elif(x in ["Algebra","Geometry","Arithmetic","Statistics"]):
            Quiz["Subject"].append(x)
        elif(x in ["Low","Medium","High"]):
            Quiz["Difficulty"].append(x)
        elif(x.isdigit() and int(x,10) <= 20):
            Quiz["Question"].append(x)
        elif(x.isdigit() and 30 <= int(x,10)):
            Quiz["Duration"].append(x)
        else:
            continue


            
        
    
        
        
        


# Create DataFrame









# # Use pytesseract to perform OCR on the image and extract text
# table_text = pytesseract.image_to_string(image)


# # Split the text into lines and create a list of lists for tabular data
# table_data = [line.split() for line in table_text.splitlines()]
# table_data.pop(0)
# for data in table_data:
#     if(len(data) <= 1): 
#         table_data.remove(data)
#         continue
#     else:   
#         data.pop(0)
#         if(len(data) > 4):
#             if(data[1] == "Number"):
#                 data[1] = "NumProp"
#                 data.pop(2)
#             elif(data[1] == "Sets"):
#                 data[1] = "Sets_n_Stats"
#                 data.pop(2)
#                 data.pop(2)
#         if(len(data) > 4):
#             data.pop(3)

                

    

# # Create a DataFrame from the table data

# drop irrelevant 
#df.drop(0,axis=1,inplace=True)
# df.dropna(how='any', inplace=True)



# print(df)
# Save the DataFrame to a CSV file
#df.to_csv('LMH10.csv', index=False)
