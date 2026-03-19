import random

def main():
    def create_scoreboard(player,final_score):
        high_score = {player['name']:final_score}
        return high_score
    def setup_player():
        """
        Prompts the user to create their player profile.

        Returns:
            dict: A dictionary containing player stats with the following keys:
                - "name" (str): Player's name (entered by user)
                - "health" (int): Starting health, set to 10
                - "inventory" (list): Starts as an empty list
        Example:
            >>> setup_player()
            Enter your name: Ailene
            {'name': 'Ailene', 'health': 10, 'inventory': []}
        """
        # TODO: Ask the user for their name using input()
        # TODO: Initialize a dictionary with keys: "name", "health", and "inventory"
        # TODO: Return the dictionary
        player_one = input('Please enter your name: ')
        return  {'name':player_one,'health':10,'inventory':[]}
    

    def create_treasures():
        """
        Creates a dictionary of treasures, where each treasure has a value.

        Returns:
            dict: Example:
                {
                    "gold coin": 5,
                    "ruby": 10,
                    "ancient scroll": 7,
                    "emerald": 9,
                    "silver ring": 4
                }
        Tip:
            You can customize treasures or randomize the values using random.randint(3, 12).
        """
        # TODO: Create a dictionary of treasure names and integer values
        # TODO: Return the dictionary
        return {
            'gold coin' : int (random.randint(3,12)), 
            'ruby' : int (random.randint(5,15)),
            'ancient scroll' : int (random.randint(7,17)),
            'emerald' : int (random.randint(9,19)),
            'silver ring' : int (random.randint(11,21))
        }


    def create_traps():
        return{
            'trap1':int(random.randint(1,3)),
            'trap2':int(random.randint(2,4)),
            'trap3':int(random.randint(3,5))
        }
    
    def use_potion(player,used_potion):
            
            if used_potion != True:
                player['health'] = 10
                print('Congratulations your health is now 10')
            
    def display_options(room_number):
        """
        Displays available options for the player in the current room.

        Args:
            room_number (int): The current room number.

        Output Example:
            You are in room 3.
            What would you like to do?
            1. Search for treasure
            2. Move to next room
            3. Check health and inventory
            4. Health Potion
            5. Quit Game
        """
        # TODO: Print the room number and the 4 menu options listed above
        print (f'You are in room {room_number}\n What would you like to do?\n 1. Search for treasure\n2. Move to next room\n3. Check health and inventory\n 4. Health Potion\n 5. Quit game')
 
    def search_room(player, treasures,traps):
        """
        Simulates searching the current room.

        If the outcome is 'treasure', the player gains an item from treasures.
        If the outcome is 'trap', the player loses 2 health points.

        Args:
            player (dict): The player's current stats.
            treasures (dict): Dictionary of available treasures.

        Behavior:
            - Randomly choose outcome = "treasure" or "trap"
            - If treasure: choose a random treasure, add to player's inventory,
              and print what was found.
            - If trap: subtract 2 from player's health and print a warning.
        """
        # TODO: Randomly assign outcome = random.choice(["treasure", "trap"])
        # TODO: Write an if/else to handle treasure vs trap outcomes
        # TODO: Update player dictionary accordingly
        # TODO: Print messages describing what happened
        treasure_value=[]
        outcome = random.choice(["treasure","trap"])
        if outcome == "treasure":
            current_treasure = random.choice(list(treasures.keys()))
            player['inventory'].append(current_treasure)
            for item in treasures:
                if item == current_treasure:
                    treasure_value.append(treasures[current_treasure])  
            print (f"Congratulations you recieved: {current_treasure}")
            return player['inventory'], treasure_value
        else:
            current_trap = int (random.choice(list(traps.values())))
            player['health'] = player['health'] - current_trap
            health = player['health']
            print (f"WARNING you only have {health} remaining")
             
        
    def check_status(player):
        """
        Displays the player’s current health and inventory.

        Args:
            player (dict): Player stats including health and inventory.

        Example Output:
            Health: 8
            Inventory: ruby, gold coin
        or:
            Health: 10
            Inventory: You have no items yet.
        """
        # TODO: Print player health
        # TODO: If the inventory list is not empty, print items joined by commas
        # TODO: Otherwise print “You have no items yet.”
        health = player['health']
        print(f'Health: {health}')
        my_inventory = player['inventory']
        if my_inventory != (''):
            print(f'Inventory: {my_inventory}')
        else:
            print('Inventory: "You have no inventory"')

    def end_game(player, treasure_value):
        """
        Ends the game and displays a summary.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary for item value lookup.

        Output:
            Prints player’s final health, inventory contents, and total score value.
        """
        # TODO: Calculate total score by summing the value of collected treasures
        # TODO: Print final health, items, and total value
        # TODO: End with a message like "Game Over! Thanks for playing.
  
        final_health = player['health']
        final_score=0
        for item in treasure_value:
            final_score += treasure_value[item] + player['health']
        if player['health'] != 0:
            print("Congratulations good game!!")
        print (f'Final Health: {final_health}')
        print(f"Your Treasure: {", ".join(map(str, player['inventory']))}" )
        print (f'Final Score: {final_score}')
        
    
    def run_game_loop(player, treasures,traps):
        """
        Main game loop that manages the rooms and player decisions.

        Args:
            player (dict): Player stats.
            treasures (dict): Treasure dictionary.

        Flow:
            - There are 5 rooms (use for loop range(1, 6))
            - Inside each room, use a while loop for player actions:
                1. Search room
                2. Move to next room
                3. Check status
                4. Quit
            - Health below 1 ends the game early.
        """
        # TODO: Loop through 5 rooms (1–5)
        # TODO: Inside each room, prompt player choice using input()
        # TODO: Use if/elif to handle each choice (1–4)
        # TODO: Break or return appropriately when player quits or dies
        # TODO: Call end_game() after all rooms are explored
        rooms = [1,2,3,4,5]
        room = 1
        used_potion = False

        while room in rooms:
            if player['health'] == 0: 
                break
            while player['health'] != 0 and room != 6 :
                display_options(room)
                player_choice=input(print('Please enter your choice:(1-6)'))
                while player_choice != "5" :
                    if player_choice == "1":
                        search_room(player,treasures,traps)
                        if player['health'] == 0:
                            print("GAME OVER")
                            break
                        else:
                            display_options(room)
                            player_choice = input('Please enter your choice:(1-4)')
                    elif player_choice == "3":
                        check_status(player)
                        display_options(room)
                        player_choice = input('Please enter your choice:(1-4)')
                    elif player_choice == "2":
                        room += 1
                        break
                    elif player_choice == "4":
                        use_potion(player,used_potion)
                        break
                if player_choice == "5":
                        break
        end_game(player,treasures)        
                                                                     
                


    # -----------------------------------------------------
    # GAME ENTRY POINT (Leave this section unchanged)
    # -----------------------------------------------------
    player = setup_player()
    treasures = create_treasures()
    traps = create_traps()
    run_game_loop(player, treasures,traps)
        

if __name__ == "__main__":
    main()
