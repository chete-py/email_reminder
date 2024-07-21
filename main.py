import pandas as pd
from datetime import date, datetime
from google.oauth2 import service_account
import gspread
from reminder import send_email


# Define your Google Sheets credentials JSON file (replace with your own)
credentials_path = 'retail-430014-bef39e7146a8.json'
    
# Authenticate with Google Sheets using the credentials
credentials = service_account.Credentials.from_service_account_file(credentials_path, scopes=['https://spreadsheets.google.com/feeds'])
    
# Authenticate with Google Sheets using gspread
gc = gspread.authorize(credentials)
    
# Your Google Sheets URL
# https://docs.google.com/spreadsheets/d/1e09gr3_1UI7yaX_Kjo21nh4m-5d6n0ITJwyA4-L1fTw/edit?gid=0#gid=0
url = "https://docs.google.com/spreadsheets/d/1e09gr3_1UI7yaX_Kjo21nh4m-5d6n0ITJwyA4-L1fTw/edit?gid=0#gid=0"
    
# Open the Google Sheets spreadsheet
worksheet = gc.open_by_url(url).worksheet("Renewals")
new = worksheet.get_all_values()        
second_headers = new[0]
new_data_fra

me = new[1:]              
newdf =  pd.DataFrame(new_data_frame, columns=second_headers)  

def convert_to_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').date()

newdf['Date'] = newdf['Date'].apply(convert_to_date)  

def load_df(newdf):    
    parse_dates = newdf["Date"]    
    return newdf

def query_data_and_send_emails(newdf):
    present = date.today()
    email_counter = 0
    for _, row in newdf.iterrows():
        if (present == row["Date"]) and (row["Status"] not in ["Renewed", "Exits"]):
            send_email(
                subject=f'{row["Remarks"]}',
                receiver_email= 'collins.chetekei@ke.grassavoye.com',
                name = row["Remarks"],
                reminder_date= row["Date"].strftime("%d, %b %Y"),                  
            )
            email_counter += 1
    return f"Total Emails Sent: {email_counter}"

newdf = load_df(newdf)
result = query_data_and_send_emails(newdf)
print(result)