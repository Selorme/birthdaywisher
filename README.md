# Birthday Reminder and Email Automation

This Python script automates sending personalized birthday emails to individuals based on the data provided in a `birthdays.csv` file. It checks if today matches any birthday and, if a match is found, selects a random birthday letter template to customize and send via email.

## Features
- **Automatic Birthday Matching**: The script reads a CSV file (`birthdays.csv`) and checks if today's date matches any birthday.
- **Randomized Email Templates**: A random letter template is selected and customized with the recipient's name.
- **Email Automation**: Emails are automatically sent to the birthday celebrants via SMTP.

## How It Works

1. **Update `birthdays.csv`**:  
   The script first updates the `birthdays.csv` file with a new set of birthdays. The file contains the following fields:
   - `name`: The name of the person.
   - `email`: The person's email address.
   - `year`: The birth year.
   - `month`: The birth month.
   - `day`: The birthday.

2. **Check for Today's Birthdays**:  
   The script compares today's date with the birthdays in the CSV file. If there’s a match, it retrieves the person's name and email address.

3. **Select a Random Letter Template**:  
   The script contains three pre-written letter templates in the `letter_templates` folder:
   - `letter_1.txt`
   - `letter_2.txt`
   - `letter_3.txt`

   One of these templates is randomly chosen, and the placeholder `[NAME]` is replaced with the actual name of the recipient.

4. **Send the Email**:  
   Using the `smtplib` library, the script connects to Gmail's SMTP server and sends the customized email to the recipient.

## Setup Instructions

### Prerequisites
- Python 3.x
- Required libraries: `pandas`, `smtplib`
- Gmail account for sending emails

### Step-by-Step Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Selorme/birthdaywisher.git
   cd birthday-email-automation
   ```

2. **Install Required Libraries**:
   Install the necessary Python packages:
   ```bash
   pip install pandas
   ```

3. **Create Your `birthdays.csv` File**:
   Create a CSV file with the following fields:
   ```csv
   name,email,year,month,day
   Becky,alekayuen51@gmail.com,2000,8,9
   Joy,awalikahadome@gmail.com,2000,2,5
   Mom,patiencemodzaka@gmail.com,1978,6,26
   Desmond,desmond.boateng@aims.ac.rw,1998,6,18
   Selorme,selormepythontest@gmail.com,2000,6,21
   ```

4. **Prepare Letter Templates**:
   Add your birthday email templates under a folder named `letter_templates`. The letter templates should contain a placeholder `[NAME]` for the recipient's name. Example content of `letter_1.txt`:
   ```
   Dear [NAME],

   Happy Birthday! Wishing you a wonderful year ahead filled with joy and success.

   Best regards,
   [Your Name]
   ```

5. **Configure Environment Variables** (Optional but recommended):
   Store your sensitive data like email and password securely using environment variables. You can use `dotenv` to load them.

6. **Run the Script**:
   Execute the script to automatically send birthday emails:
   ```bash
   python main.py
   ```

## Email Credentials
The script uses Gmail's SMTP server (`smtp.gmail.com`). Update the following variables in the script with your email credentials:

- `my_email`: Your Gmail address.
- `password`: Your Gmail app-specific password (enable 2-factor authentication and create an app-specific password for Gmail).

```python
my_email = "your-email@gmail.com"
password = "your-app-specific-password"
```

## Security Considerations
Ensure that you use **app-specific passwords** if using Gmail and avoid hardcoding sensitive information like your password in the script. Instead, use environment variables or secure password management.

## Future Enhancements
- Add support for multiple email providers (e.g., Outlook, Yahoo).
- Implement a GUI for easier birthday management and email customization.
- Add an option for sending birthday reminders via SMS.

## License
This project is licensed under the MIT License.