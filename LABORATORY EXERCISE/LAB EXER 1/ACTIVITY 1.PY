tickets = [
    ["INC1392939", "BOT-Inventory", "Failed to generate the daily report"],
    ["INC1392940", "BOT-Email", "Failed to send the scheduled notification"],
    ["INC1392941", "BOT-DataSync", "Encountered an error during data transfer"],
    ["INC1392942", "BOT-Invoice", "Failed to process an invoice"],
    ["INC1392943", "BOT-Report", "Failed to generate the weekly report"],
    ["INC1392944", "BOT-FileTransfer", "Failed to upload the required file"],
    ["INC1392945", "BOT-DataEntry", "Encountered an error while entering records"],
    ["INC1392946", "BOT-Backup", "Failed to complete the scheduled backup"],
    ["INC1392947", "BOT-Validation", "Failed to validate the submitted records"],
    ["INC1392948", "BOT-Notification", "Failed to send the system alert"]
]

while True:
    print("\nAUTOMATION INCIDENT TICKET MANAGER")
    print("1. Add Incident Ticket")
    print("2. Display All Active Tickets")
    print("3. Search Incident Ticket")
    print("4. Remove Resolved Ticket")
    print("5. Count Active Tickets")
    print("6. Exit")

    choice = input("Enter number: ")

    if choice == "1":
        incident_id = input("Enter Incident ID: ")
        bot = input("Enter Bot: ")
        description = input("Enter Description: ")

        ticket = [incident_id, bot, description]
        tickets.append(ticket)

        print("Incident ticket added successfully!")

    elif choice == "2":
        if len(tickets) == 0:
            print("No active incident tickets.")
        else:
            print("\n===== ACTIVE INCIDENT TICKETS =====")
            for ticket in tickets:
                print("Incident ID:", ticket[0])
                print("Bot:", ticket[1])
                print("Description:", ticket[2])
                print("-----------------------------------")

    elif choice == "3":
        search_id = input("Enter Incident ID to search: ")
        found = False

        for ticket in tickets:
            if ticket[0] == search_id:
                print("\nIncident Ticket Found!")
                print("Incident ID:", ticket[0])
                print("Bot:", ticket[1])
                print("Description:", ticket[2])
                found = True
                break

        if not found:
            print("Incident ticket not found.")

    elif choice == "4":
        remove_id = input("Enter Incident ID to remove: ")
        found = False

        for ticket in tickets:
            if ticket[0] == remove_id:
                tickets.remove(ticket)
                print("Incident ticket removed successfully!")
                found = True
                break

        if not found:
            print("Incident ticket not found.")

    elif choice == "5":
        print("Total number of active incident tickets:", len(tickets))

    elif choice == "6":
        print("Exit successful")
        break

    else:
        print("Invalid choice. Please try again.")