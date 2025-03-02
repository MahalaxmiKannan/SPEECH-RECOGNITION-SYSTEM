# SPEECH-RECOGNITION-SYSTEM
COMPANY: CODETECH IT SOLUTIONS

NAME: MAHALAXMI K

INTERN ID: CT08RQW

COMPANY: AI

DURATION: 4 WEEKS

MENTOR: NEELA SANTHOSH KUMAR

DESCRIPTION OF THE PROJECT

This project is a **Speech-to-Text Converter**, which allows users to convert spoken words into written text using a microphone. The main functionality revolves around capturing live audio from the user, processing it with speech recognition technology, and displaying the transcribed text in a graphical user interface (GUI). The user can start and stop the speech recognition process using two buttons, making the application interactive and user-friendly. The project uses the **Tkinter** library for the graphical interface, the **SpeechRecognition** library for speech-to-text conversion, and **threading** to ensure that the GUI remains responsive during the listening process. The tool enables real-time conversion of spoken words to text, providing a seamless and efficient way to transcribe audio.

The core technology behind this project is **Google’s Speech Recognition API**, which is used through the `SpeechRecognition` Python package. The API takes audio input, processes it, and returns the recognized speech in the form of text. The application continuously listens for speech input until the user presses the "Stop" button. This is managed using a flag (`listening`), which ensures the program continues to record audio until explicitly stopped. The **Tkinter** library is used to create the user interface, allowing the user to interact with the program. The interface includes buttons to start and stop the speech recognition process, a text output area to display the transcribed text, and a status label that provides real-time feedback about the system’s state.

The tech stack used in this project includes **Python**, **Tkinter**, **SpeechRecognition**, and **threading**. Python is the primary language, chosen for its simplicity and flexibility, making it ideal for rapid prototyping and integration with external libraries. **Tkinter** is the default GUI toolkit for Python, which is lightweight and easy to use for building simple desktop applications. **SpeechRecognition** is an essential library for implementing speech-to-text functionality and utilizes Google's cloud-based speech recognition API. **Threading** is used to run the speech recognition process in a separate thread, ensuring the GUI doesn’t freeze while recording or processing speech.

Through working on this project, I learned several key skills. First, I gained experience with integrating **speech recognition technology** into Python applications, using **SpeechRecognition** to access and process real-time audio input. I also enhanced my understanding of **multithreading** in Python, which is crucial for maintaining a responsive user interface while performing tasks that take time, such as speech recognition. Additionally, I deepened my knowledge of **GUI development** with Tkinter, learning how to create functional interfaces with interactive components like buttons, text areas, and labels. The project also taught me how to manage application flow with flags and conditions, such as using the `listening` variable to control when the recording starts and stops. This project improved my ability to design user-centric applications and handle external APIs and asynchronous tasks, laying a solid foundation for further work in speech processing and user interface design.

OUTPUT OF THE PROJECT

![Image](https://github.com/user-attachments/assets/2d7c46ae-20fe-43b6-a8bd-648e5e945862)
