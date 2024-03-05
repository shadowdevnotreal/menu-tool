import sys
import time
import subprocess

# ANSI escape codes for colors
colors = {
    "RED": "\033[31m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[33m",
    "BLUE": "\033[34m",
    "MAGENTA": "\033[35m",
    "CYAN": "\033[36m",
    "WHITE": "\033[37m",
    "RESET": "\033[0m",
}

# Function to print text like a typewriter
def typewriter(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()  # Move to next line

# Function to display the banner
def display_banner():
    banner_text = "Welcome to the Interactive Menu"
    color_sequence = ["RED", "YELLOW", "GREEN", "CYAN", "BLUE", "MAGENTA"]
    for i, char in enumerate(banner_text):
        sys.stdout.write(colors[color_sequence[i % len(color_sequence)]] + char)
    print(colors["RESET"])  # Reset to default terminal color

# Function to execute a command or script
def execute_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

# Function to display help information
def display_help():
    help_text = """
    HELP MENU
    ---------
    This menu allows you to interact with the system by selecting options. Each option performs a different task:
    - Option 1: Executes the 'echo Hello!' command.
    - Option 2: Lists the contents of the current directory using the 'ls' command.
    - Option 3: Exits the interactive menu.
    - Option 4: Displays this help information.
    
    To select an option, type the option number and press Enter.
    """
    typewriter(help_text, speed=0.01)

# Function to display the menu and handle user input
def display_menu():
    options = {
        "1": {"text": "Option 1: Say Hello (Echo Command)", "command": "echo Hello!"},
        "2": {"text": "Option 2: List current directory (ls Command)", "command": "ls"},
        "3": {"text": "Option 3: Exit", "command": "exit"},
        "4": {"text": "Option 4: Display Help", "command": "help"},
    }

    for key in options:
        typewriter(f'{key}: {options[key]["text"]}', speed=0.02)

    choice = input("Please select an option: ")
    if choice in options:
        if choice == "3":
            print("Exiting...")
            sys.exit()
        elif choice == "4":
            display_help()
        else:
            execute_command(options[choice]["command"])
    else:
        print("Invalid choice, please try again.")

# Main function to run the menu
def main():
    display_banner()
    display_menu()

if __name__ == "__main__":
    main()
