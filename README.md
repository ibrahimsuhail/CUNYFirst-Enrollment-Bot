0. The enrollment works 100% but for me it didn't message me when it executed

1. Please look at the file and replace the variables with your info as I wrote

2. Download selenium and twilio libraries
   https://selenium-python.readthedocs.io/installation.html
   https://www.twilio.com/docs/usage/api

3. Download geckodriver (you can use chromedriver too but I like geckodriver)
   https://github.com/mozilla/geckodriver/releases

4. Go to 'https://twilio.com' and sign up for a free account. Once you are verified and have gotten a twilio number, take the **twilio number, auth token, and accountsid**, and put them in the code with quotes next to the variables that have the same name. This will allow you to receives text updates when your classes open up.
![Twilio Info](https://www.twilio.com/blog/wp-content/uploads/2016/08/oy1Q-OazNr90Wl8URRpS0KweZBf8I285WuRzabOWpLUvNGY18ftMbdmlRLckbQHS1RibmdszmnkGLrnO2pc1vDJyor1l74M-Eu_Dl45eDUUBXySUQfOzMwPWj04HSvSVyPr7B2X0.png?raw=true "Twilio Info")

5. Go to 'https://myaccount.google.com/security' and scroll all the way to he bottom. Then go to where it says 'Allow less secure apps: ON' and check OFF. You should get an email about the change. Go ahead and update the code to have your gmail email/user and password to send emails to your yourself
![Google Account](https://github.com/Maxthecoder1/CUNYFirst-Enrollment-Bot/blob/master/screenshots/myaccountgoogle.png?raw=true "Google Account Security")

6. Go to CUNYFIRST, Click Enroll. Then choose your Term. Once you are are on the Shopping Cart Page, Right + Click on the 'add' button and Click on 'Copy Link Location'.  Then paste the link next to self.addshoppingcartlink in the code. It should look like the link below:

    self.addshoppingcartlink = 'https://hrsa.cunyfirst.cuny.edu/psc/cnyhcprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?Page=SSR_SSENRL_CART&Action=A&ACAD_CAREER=UGRD&EMPLID=12345678&ENRL_REQUEST_ID=&INSTITUTION=BKL01&STRM=1172'
    

    
# How to Run
open vscode and press run
pls do not use or close the firefox browser running
you may open to see but don't press anything