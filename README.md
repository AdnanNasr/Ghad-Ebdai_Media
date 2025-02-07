# Telegram Bot Setup Guide  

## Step 1: Create a Telegram Token  
To start, you need to create a **Telegram Bot Token**. Follow these steps to generate a token using the **BotFather**:  

1. Open Telegram and search for `@BotFather`.  
2. Start a chat with BotFather and send the command: `/newbot`  
3. Follow the on-screen instructions to complete the bot creation process.  
4. Once done, BotFather will provide you with an **API token**. Keep this token safe, as you will need it in the next steps.  

## Step 2: Download the Bot Code  
After obtaining your token, you need to set up the bot on your system:  

1. Clone the bot's repository using **Git**: `git clone <repository_url>` then navigate to the project folder using `cd <repository_name>`.  
2. Install the required dependencies using **pip**: `pip install -r requirements.txt`.  

## Step 3: Configure and Run the Bot  
1. Open the `app.py` file and insert your **Telegram Bot Token** in the appropriate section.  
2. Start the bot by running the following command: `python app.py`.  
3. Your bot is now active! Enjoy downloading media from the internet using your new Telegram bot.  

**Notes:**  
- Replace `<repository_url>` with the actual Git repository URL.  
- Ensure you have **Python** installed before proceeding with the setup.
