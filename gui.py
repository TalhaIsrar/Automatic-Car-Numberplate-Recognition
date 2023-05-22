import tkinter as tk
import subprocess

def run_script():
    # Define the command and arguments
    command = [
        "python",
        "detect.py",
        "--weights",
        "runs/train/exp/weights/best.pt",
        "--conf",
        "0.3",
        "--source",
        "license-1/test/im"
    ]

    # Run the command
    subprocess.run(command)

# Create the main window
window = tk.Tk()
window.title("Run Script GUI")

# Create a button to run the script
button = tk.Button(window, text="Run Script", command=run_script)
button.pack()

# Start the main event loop
window.mainloop()
