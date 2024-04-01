# Automated email task scheduler
This project highlights a Python script that upon request, automatically returns a user a task and an interval of time to spend doing that task. This script runs periodically according to a predefined schedule, maintained by cron for task scheduling on UNIX systems. It automatically checks for emails from the user and replies with a task without the need for manual intervention.

# Opportunities
Users can customize their scripts for their specific purpose.

# Setup
1. Clone repo.
2. Make sure Python installed.
3. Create your own credentials.py with your own relevant information:
   - EMAIL, PASSWORD, SENDER_EMAIL, ACTIVITIES, INTERVALS
4. You can adjust email_me.py as it suits your own purpose. Once you create your credentials file, it is read to use as is.
5. You can also schedule it using the task scheduler available to you. If on a UNIX-like system, use cron in your terminal.
  - crontab -e to edit your crontab file.
  - add the cron job according to your desired intervals.

# How to use
As written, this script checks for an email with the word 'task' in the body from the user. For example, "Please give me a task." or "One task please.". Then, it returns a randomly-selected task and a randomly-selected time interval (user-customizable) and returns it to the user in an email. 
