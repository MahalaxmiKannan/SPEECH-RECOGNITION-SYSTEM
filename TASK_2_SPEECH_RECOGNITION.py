import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import threading

# Global variable to control the listening state
listening = False

# Function to convert speech to text
def listen_to_speech():
    recognizer = sr.Recognizer()
    
    # Using the default microphone as the audio source
    with sr.Microphone() as source:
        text_output.delete(1.0, tk.END)  # Clear previous text
        status_label.config(text="Listening... Please speak.")
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        
        while listening:  # Keep listening until stopped
            try:
                print("Listening for speech...")
                audio = recognizer.listen(source, timeout=5)
                status_label.config(text="Recognizing...")

                # Recognizing speech
                speech_text = recognizer.recognize_google(audio)
                print(f"Recognized: {speech_text}")
                text_output.insert(tk.END, speech_text + "\n")
                status_label.config(text="Ready to listen again.")
            except sr.UnknownValueError:
                status_label.config(text="Sorry, I did not understand the speech.")
            except sr.RequestError:
                status_label.config(text="Sorry, the service is unavailable.")
            except Exception as e:
                status_label.config(text=f"Error: {str(e)}")
                break

# Function to start the listening process
def start_listening():
    global listening
    listening = True
    threading.Thread(target=listen_to_speech, daemon=True).start()
    status_label.config(text="Listening... Please speak.")

# Function to stop the listening process
def stop_listening():
    global listening
    listening = False
    status_label.config(text="Stopped listening.")
    print("Recording stopped.")

# Create the main window
root = tk.Tk()
root.title("Speech to Text Converter")
root.geometry("500x400")

# Add a label to show the status of the speech-to-text process
status_label = tk.Label(root, text="Click 'Start' to begin.", font=("Times New Roman", 14))
status_label.pack(pady=10)

# Add a button to start the listening process
start_button = tk.Button(root, text="Start", font=("Times New Roman", 14), command=start_listening)
start_button.pack(pady=20)

# Add a button to stop the listening process
stop_button = tk.Button(root, text="Stop", font=("Times New Roman", 14), command=stop_listening)
stop_button.pack(pady=20)

# Text area to display recognized text
text_output = tk.Text(root, height=10, width=50, font=("Times New Roman", 12))
text_output.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
