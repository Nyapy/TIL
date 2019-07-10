import os

os.chdir(r'C:\Users\student\TIL\00_StartCamp\02_Day\dummy')

for filename in os.listdir('.'): #모든파일을 다 가져올것임.
    #os.rename(filename,f'SAMSUNG_{filename}')


    os.rename(filename, filename.replace('SAMSUNG_', 'SSAFY_'))