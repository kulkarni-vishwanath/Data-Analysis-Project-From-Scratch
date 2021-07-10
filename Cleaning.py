# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 19:23:04 2021

@author: kulka
"""

import pandas as pd
import numpy as np
import re
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# reading the data
raw_data = pd.read_csv("Raw_Data.csv")


# Cleaning the Reviews column (be aware of the missing values)
raw_data['Reviews'] = raw_data['Reviews'].dropna().apply(lambda x: int(x.split(" ")[0][1:]))


# cleaning the Experience column
raw_data['Min_Exp_Needed'] = raw_data['Experience'].dropna().apply(lambda x: x.split("-")[0])
raw_data['Max_Exp_Needed'] = raw_data['Experience'].dropna().apply(lambda x: x.split("-")[-1].split(" ")[0])


# cleaning the Posted column
raw_data['Posted'].replace({"JUST NOW":"0 DAYS AGO",
                            "FEW HOURS AGO":"0 DAYS AGO",
                            "TODAY":"0 DAYS AGO"}, inplace=True)

raw_data['Posted'] = raw_data['Posted'].dropna().apply(lambda x: x.split("DAYS")[0])
raw_data['Posted'] = raw_data['Posted'].dropna().apply(lambda x: x.split("DAY")[0])


# cleaning the Salary column
raw_data['Salary'].replace({'Not disclosed':np.NaN},inplace=True)

raw_data['Salary'] = raw_data['Salary'].dropna().apply(lambda x: x.replace(" PA.",""))
raw_data['Salary'] = raw_data['Salary'].dropna().apply(lambda x: x.replace("more than ",""))
raw_data['Salary'] = raw_data['Salary'].dropna().apply(lambda x: x.replace("1 Cr and above","1,00,00,000"))
raw_data['Salary'] = raw_data['Salary'].replace(to_replace=r"\([\w :\d+.%]+\)",value="",regex=True)

raw_data['Min_Salary'] = raw_data['Salary'].dropna().apply(lambda x: x.split("-")[0])
raw_data['Max_Salary'] = raw_data['Salary'].dropna().apply(lambda x: x.split("-")[0] if len(x.split("-"))==1 else x.split("-")[-1])

raw_data['Min_Salary'] = raw_data['Min_Salary'].dropna().apply(lambda x: int(x.replace(",","")))
raw_data['Max_Salary'] = raw_data['Max_Salary'].dropna().apply(lambda x: int(x.replace(",","")))

raw_data['Avg_Sal'] = (raw_data['Min_Salary']+raw_data['Max_Salary'])/2


# cleaning tags column
raw_data['Tags'] = raw_data['Tags'].dropna().apply(lambda x: x.split("\n"))
raw_data['Tags'] = raw_data['Tags'].dropna().apply(lambda x: ','.join([i for i in x]))


# cleaning the Location column
raw_data['Location'] = raw_data['Location'].dropna().apply(lambda x: re.sub(r'\([^)]*\)', '', x))

to_replace=["Bangalore/Bengaluru","Bengaluru/Bangalore","Hyderabad/Secunderabad","Gurgaon/Gurugram",
            "Delhi/NCR","Trivandrum/Thiruvananthapuram","Kochin/Cochin","Hyderabad, telangana",
            "Anywhere in India","india","Remote","Chennai, Chennai","not specified","Mysore/Mysuru","telangana",
            "Mohali/SAS Nagar","Gurgaon, haryana","Mysore","Kalyani, Nagar","Delhi / NCR",
            "Bengaluru / Bangalore","Not specified","Navi Mumbai","New Delhi","Tamil Nadu","remote","Kochi/Cochin",
            "India","Anywhere In India","Tiruchirapalli/Trichy","Panaji/Panjim","IN-BangaloreTi","KA","Delhi NCR",
            "Navi Mumbai","Not Specified","WFH","goa","Varanasi/Benaras","PAN India","Nowrangapur/Nabarangpur",
            "Other City in Punjab","Andhra Pradesh","Other","Others","Work from home","Noida/Greater Noida",
            "Varanasi / Banaras","karnataka","kerala","uttar pradesh","thiruvananthapuram","punjab","mohali",
            "haryana","gujarat","goregaon east,mumbai","bidadi, karnataka","anywhere in Anywhere","anywhere",
            "maharashtra","bidadi, Bengaluru","Thrissur/Trichur","Tiruchirapalli/USA",
            "TAMILNADU, Thiruvananthapuram, RNATA","Pondicherry/Puducherry","Sonipat/Sonepat","REMOTE","Pune City"]

replace_with=["Bengaluru","Bengaluru","Hyderabad","Gurugram","Delhi","Thiruvananthapuram","Kochin","Hyderabad",
              "Anywhere","Anywhere","Anywhere","Chennai","Anywhere","Mysuru","Hyderabad","Mohali","Gurugram","Mysuru",
              "Kalyani","Delhi","Bengaluru","Anywhere","Mumbai","Delhi","","Anywhere","Kochin","Anywhere","Anywhere",
              "Trichy","Goa","","","Delhi","Mumbai","Anywhere","Anywhere","Goa","Varanasi","Anywhere","Nowrangapur",
              "Chandigarh","Hyderabad","Anywhere","Anywhere","Anywhere","Noida","Varanasi","Bengaluru","Thiruvananthapuram","Lucknow",
              "Thiruvananthapuram","Chandigarh","Mohali","Gurugram","Ahmedabad","Mumbai","Bengaluru","Anywhere","Anywhere",
              "Mumbai","Bengaluru","Thrissur","Tiruchirapalli, USA","Thiruvananthapuram","Puducherry","Sonipat","Anywhere",""]

raw_data['Location'] = raw_data['Location'].replace(to_replace,replace_with,regex=True)


# creating cleaned data file
raw_data.to_csv("Cleaned_Data.csv",index=None)













































