# ConnectIT
Ingram Mirco Case Competition

# Problem Statement

Maxwell, head of Building Operations at 55 Standish Court, Mississauga, Ontario, is experiencing some problems with getting insight into the building systems. Everything is reactive. Some of the issues that have occurred include the HVAC system breaking down twice in November and the elevator failing at least once per week over four weeks. Occupancy comfort is also an issue – sometimes, it’s too hot, and other times, it’s just so cold that the occupants need a sweater! There have also been several cases of water leakage that caused severe damages. Your goal is to help Maxwell gain real operational insight with an early warning system. Help him become the proactive Building Operations Manager he wants to be. What would you recommend to Maxwell?


# Solution

We decided to create a two part solution. The first being a concept idea using a sensor relay to make issues with the building interconnected through different sensors; air pressure, temperature, humidity, etc. We will then connect these sensors to a router to collect data from around the building. We will have this data accesible to Maxwell with a dashboard and implement a machine learning backend to figure out why the problems occured by taking into account the frequency, intensity, and location of the data. 

The second part is our more tangible end user experience. For this we created a simple python script utilizing Twillo API and Google Drive API. With these we implement the gspread package made by Anton Burnashev to read the spreadsheet data. 

# SETUP

Make an account on twillo.com for;
    account_sid:
    auth_token:
    Phone number:
 
 We will use these to integrate the twillo API
 
Next we want to be able to access our spreadsheet data and to do this we will need to create a service account and OAuth2 credentials from the Google API console. 

1. Visit https://console.developers.google.com/
2. Create a new project
3. Go to "Enable API" and search for Google Drive API. As you might have guessed you will want to enable it!
4. Now click "Create credentials". In the dropdowns select "Web Server" and bubble in "Application Data"
5. Give the service account a name so you can reference it easier and give it "Project" then "Editor" roles after
6. Download the client_secret.JSON file and replace it with the clien_secret_blank.JSON I have left in the project folder

Now that you have the JSON file you need to actually complete one more step so that the service account can access your specific spreadsheet. 

1. Open the client_secret.json and copy the string inside of the client_email field. 
2. Open your spreadsheet and click share, and copy the client_email in with edit perms. 
 
 
INSTALL THESE PACKAGES (I used Git Bash to do so) 

  $pip install gspread
  $pip install oauth2client
  
We implement these packges with the following code in the spreadsheet_to_SMS.py

===============================================================================

'''import gspread
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
'''
