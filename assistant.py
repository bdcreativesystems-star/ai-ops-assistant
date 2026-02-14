from automations.file_organizer import organize_files
from automations.system_report import generate_report

class AIOpsAssistant:
    def run(self):
        print("AI Ops Assistant")
        print("1. Organize Files")
        print("2. System Report")

        choice = input("Select task: ")

        if choice == "1":
            organize_files()
        elif choice == "2":
            generate_report()
        else:
            print("Invalid option")
