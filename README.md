# ConnectIT
Ingram MircoCase Competition


SETUP:

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

