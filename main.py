import pytesseract
from PIL import Image
import pandas as pd
import os

if("Kaplan_Data" not in os.getcwd()):
    DATA_IMAGES_PATH = f'{os.getcwd()}/Kaplan_Data/data/images/'
else:
    DATA_IMAGES_PATH = f'{os.getcwd()}/data/images/'
  
imgCount = 1
images = list()

for fileName in os.listdir(DATA_IMAGES_PATH):
    
    if fileName.endswith(".png"):
        if(not fileName[0].isdigit()):
            oldName = fileName
            fileName = imgCount + '.png'
            
            os.rename(DATA_IMAGES_PATH + oldName, DATA_IMAGES_PATH + fileName)
        
        imgCount = imgCount + 1
        images.append(Image.open(DATA_IMAGES_PATH + fileName))




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
# df = pd.DataFrame(data=table_data,columns=["Question","Topic","Difficulty","Seconds"])

# drop irrelevant 
#df.drop(0,axis=1,inplace=True)
# df.dropna(how='any', inplace=True)



# print(df)
# Save the DataFrame to a CSV file
#df.to_csv('LMH10.csv', index=False)
