import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

# Create a chatbot using the provided pairs of patterns and responses
pairs = [
    [
        r"hi|hello",
        ["Hello!", "Hi there!", "How can I assist you today?"]
    ],
    [
        r"book a bus|bus booking",
        ["Sure! To which destination would you like to book a bus?"]
    ],
    [
        r"(.*) to (.*)",
        ["I can help you find available buses from %1 to %2 . Please provide the date of travel."]
    ],
    [
        r"hi|hello|hey",
        ["Hello", "Hey there",]
    ],
    [
        r"book a bus ticket",
        ["Sure, I can assist you with that. Please provide the source and destination locations, as well as the travel date."]
    ],
    [
        r"I want to travel from (.*) to (.*) on (.*)",
        ["Great! Let me check the availability of buses from %1 to %2 on %3."]
    ],
    [
        r"available buses",
        ["Here are the available buses for your selected route: \n1. Bus 1 \n2. Bus 2 \n3. Bus 3"]
    ],
    [
        r"book bus (\d+)",
        ["Bus %1 has been booked successfully. Please provide your contact details for ticket confirmation."]
    ],
    [
        r"my name is (.*)",
        ["Nice to meet you, %1. Can you please provide your phone number?"]
    ],
    [
        r"phone number is (\d+)",
        ["Thank you for providing your contact details. Your ticket will be sent to %1. Have a pleasant journey!"]
    ],
    [
        r"quit",
        ["Thank you for using our Redbus chatbot. Goodbye!"]
    ],
    [
        r"(.*) 2023",
        ["Ok , I'll see if any buses are available. Yes available ! Do you want to book a bus on %1"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand. Could you please rephrase your query?"]
    ]
]

# Create a chat bot based on the defined pairs
chatbot = Chat(pairs, reflections)

# Function to handle user input and display responses
def send():
    user_input = user_entry.get()
    response = chatbot.respond(user_input)
    chat_display.insert(tk.END, "User     >>  " + user_input + "\n")
    chat_display.insert(tk.END, "ChatBot  >>  " + response + "\n\n")
    user_entry.delete(0, tk.END)

# Create the main window
window = tk.Tk()
window.title("Redbus Customer Interaction")

# Create the chat display area
chat_display = scrolledtext.ScrolledText(window, width=80, height=25)
chat_display.insert(tk.END, "WELCOME TO REDBUS ... BOOK FROM ANYWHERE ANYTIME \n\n")
chat_display.pack()
chat_display.configure(fg='red')

# Create the user input field
user_entry = tk.Entry(window, width=100)
user_entry.pack()


# Create the send button
send_button = tk.Button(window, text="Send", command=send, fg='green', width=20)
send_button.pack()

quit_button = tk.Button(window, text="Quit" , command=window.destroy, fg='red', width=20)
quit_button.pack()
# Run the main loop

window.mainloop()
