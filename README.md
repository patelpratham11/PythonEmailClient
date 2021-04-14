## Welcome to Python Email Client v0.0.1 ##

### Pre-usage instructions ###

1. Compile a list of email addresses that you would like to send an email to
  * Be sure to have the email address on the left column and the name on the right
  * Check the spacing between the email and names
  * Export the file as a CSV

2. Make sure your gmail account is set to allow for un-safe applications to access it
  * This is in order to make sure that this client can access your email and send the emails
  * You can access that site and turn it on [here](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4O58MFMjNVIKVEKaC111KA9L7cS9HSwvjSQY2cWjhFXBpv1nPrm99gWIG7A9jL7cpQp5I7SGoQNxDSNFRelflBjGluXDA)
3. Make sure all of your files are in the proper directory
  * CSV file should be in the same folder as the rest of this project
4. Edit/add your message in basic HTML with the person variable in {}
  * e.g. "<html lang="en" dir="ltr">
      \<head>\</head>

        \<body>

        \<p>Dear {}, \<br> I hope this email finds you in well health. I made this email using python, html, and a few import statements. I hope the formatting and everything works out fine. Please let me know if anything is messed up.\</p>

      \</body>

    \</html>"



### Important Notices ###
- Be sure to know the name of your CSV File, gmail account, and password
- If unsafe application access is turned *off* then you will get an error saying the system was *not able to login*
- the HTML portion can be changed/ deleted depending on use

### Development ###
This project was developed for Raj Patel by Pratham Patel, April 12, 2021 for personal usage

All bug reports can be submitted through GitHub
