individual_spots = 20 # number of spots in each individual
num_teams = 4
team_size = 5
num_events_per_participant = 5
team_events = ["Football", "Basketball", "Spelling", "Math Quiz", "Golf"] # events for each team
def get_participant_type():
    while True:
        participant_type = input("Are you registering as an individual or a team? ").lower() 
    
        if participant_type in ["individual", "team"]:
            return participant_type 
        else:
            print("Invalid participant type. Please choose 'individual' or 'team.'") 

def individual_registration():
    name = input("Enter your name: ")
    contact_details = input("Enter your contact details: ")
    return name, contact_details, ""
# Function to handle team registration
def team_registration():
    team_name = input("Enter your team name: ")
    return "", "", team_name
# Function to handle event registration
def select_events():
    selected_events = []
    print("\nAvailable events:")
    for index, event in enumerate(team_events, start=1):
        print(f"{index}. {event}")

    while True:
        event_type = input("Select event type (Sporting/Academic): ").lower()
        if event_type in ["sporting", "academic"]:
            break
        else:
            print("Invalid event type. Please choose 'Sporting' or 'Academic'.")

    while True:
        try:
            num_events = int(input("How many events do you want to participate in? (1-5): "))
            if 1 <= num_events <= 5:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    for _ in range(num_events):
        while True:
            try:
                event_choice = int(input("Enter the number of the event you want to participate in: "))
                if 1 <= event_choice <= len(team_events):
                    selected_events.append(team_events[event_choice - 1])
                    break
                else:
                    print("Invalid event choice. Please enter a valid number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    return selected_events
# Calculate points for each rank
def calculate_points(rank):
    if rank == 1:
        return 10
    elif rank == 2:
        return 8
    elif rank == 3:
        return 6
    else:
        return 0

def display_separator():
    print("»»————- ★ ————-««")

def main():
    print("=====================================")
    print("      TOURNAMENT SCORING SYSTEM")
    print("=====================================")
    print("Welcome to the tournament registration system!")
# Get participant type 
    participant_type = get_participant_type()

    if participant_type == "individual":
        name, contact_details, team_name = individual_registration()
    elif participant_type == "team":
        name, contact_details, team_name = team_registration()
    else:
        print("Invalid participant type. Exiting.")
        return
# Select events
    events = select_events()

    event_ranks = {}
    for event in events:
        ranks = []
        print(f"\nEvent: {event}")
        for _ in range(num_teams if participant_type == "team" else individual_spots):
            while True:
                try:
                    rank = int(input("Enter your rank in the event: "))
                    if 1 <= rank <= (num_teams if participant_type == "team" else individual_spots):
                        ranks.append(rank)
                        break
                    else:
                        print("Invalid rank. Please enter a valid rank.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        event_ranks[event] = ranks
# Calculate points
    print("\nThank you for registering!")
    print("Here is your registration summary:")
    print(f"Participant Type: {participant_type}")
    print(f"Name: {name}")
    print(f"Contact Details: {contact_details}")
    if participant_type == "team":
        print(f"Team Name: {team_name}")
    print(f"Selected Events: {', '.join(map(str, events))}")

    print("\nLeaderboard:")
    for event, ranks in event_ranks.items():
        print(f"\nEvent: {event}")
        display_separator()
        for i, rank in enumerate(sorted(ranks), start=1):
            participant_name = name if participant_type == "individual" else f"Team {team_name}"
            points = calculate_points(i)
            print(f"{i}. {participant_name} - Rank: {rank}, Points: {points}")
        display_separator()

if __name__ == "__main__":
    main()
