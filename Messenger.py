import gspread
from oauth2client.service_account import ServiceAccountCredentials
import re

scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_id.json', scope)

gc = gspread.authorize(credentials)
WS=gc.open_by_url("GOOGLE SHEET URL")
worksheet = WS.worksheet("WORKSHEET NAME")

regex_name=re.compile(".+:")
regex_message=re.compile(":.+")

def getFirstEmptyRowByColumnArray(): 
  values = worksheet.col_values(2)
  ct = 0;
  while ( values[ct]): 
    ct=ct+1
  return (ct+1)

def getMessages():
  values = worksheet.range('B1:B100')
  for x in range(0,getFirstEmptyRowByColumnArray()):
    plaintext = decrypt(Name, values[x])
    if str(plaintext).find(Name) != -1:
      print ((plaintext)[12:-2])
      print ("\n")
  return

def sendMessage(): 
    rec=input("Reciever:  ")
    message=input("Message:  ")
    encmes=encrypt(Name, rec+":"+message+"-"+Name)
    worksheet.update_cell(getFirstEmptyRowByColumnArray(), 2, encmes)
    print ("\n")
    print("Cell: "+str(getFirstEmptyRowByColumnArray())+",2 Value: "+rec+":"+message)
    print ("\n")
    return

def clearMessage(): 
  values = worksheet.range('B1:B100')
  ct=0
  for cell in values:
    if (cell!='')and (str(cell).find(Name) != -1):
      cell.value = ''
  worksheet.update_cells(values)
  return
  
Name=input("Name: ")
while True:
    inpu=input("(S)end or (G)et or (C)lr  ")
    if (inpu.lower()=="g"):
      getMessages()
    elif (inpu.lower()=="s"):
      sendMessage()
    elif(inpu.lower()=="c"):
      clearMessage()
