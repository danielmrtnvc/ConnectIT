#Importing gooogle drive package made by Anton Burnashev
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Importing Twillo information
from twilio.rest import TwilioRestClient
account_sid = "ENTER YOUR account_sid HERE"
auth_token = "ENTER YOUR auth_token HERE"
clienttwillo = TwilioRestClient(account_sid, auth_token)

#Use creds in "client_secret.json" to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

#Find a workbook by name and open the first sheet
sheet = client.open("ENTER YOUR SPREADSHEET NAME HERE").sheet1

#Extract and print all of the values
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)


#Logic to find newest report row value. Takes all values from "test value" column(logs "1" for each report), pops out the first row(title row with string values), changes list into int then finds sum
#Very Hacky I know ;)
values_list = sheet.col_values(7)
values_list.pop(0)
print(values_list)

results = list(map(int, values_list))
print(results)

def sum(results):
    total = 0
    for x in results:
        total += x
    return total

newest_incident = sum(results) + 1
print(newest_incident)

#Get values for row and col cords to save different cells we want to report. In my spreadsheet those values fell under the 4, 1, 3, and 8 columns. So switch accordingly
issue_type = sheet.cell(newest_incident, 4).value
name = sheet.cell(newest_incident, 1).value
location = sheet.cell(newest_incident, 3).value
time_stamp = sheet.cell(newest_incident, 8).value

customMsg = 'Hello Maxwell, you have a new incident report! The tentant: ' + str(name) + ' is experiencing a ' + str(issue_type) + ' at ' + str(location) + '. Reported on: ' + str(time_stamp)
message = clienttwillo.messages.create(to="ENTER YOUR PHONE NUMBER HERE", from_="ENTER YOUR TWILLO NUMBER HERE", body=customMsg)

"""
Was in the process of adding more features but didn't have time.
To-do:
-Conditional logic for a certain frequency of reports are made (made x amount within x minutes?)
-Conditional logic for when urgent level reports are made (level 4 and up?)
-SMS commands so Maxwell can request certain information on his phone (i.e notes from reports, the number for each type of issue, etc)
-Add some cool shit :)

urgent = sheet.cell(newest_incident, 5).value
print(urgent)

if urgent == 5:
    customMsg2 = 'URGENT: ISSUE ' + str(issue_type) + ' at ' + str(location) + '. Reported on: ' + str(time_stamp)
    message2 = clienttwillo.messages.create(to="", from_="", body=customMsg2)
"""