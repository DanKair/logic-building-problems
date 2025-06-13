# Display the table
# 1. Create the 3x3 grid matrix (1-9 positions)
# 2. every 3 steps, make a line break
# 3. Allow items in the collection type to be replaced (probably strings)

    
# Game Logic Functionality
# 1. Ask 2 user inputs (Probably would make someone make a first step randomly)
# 2. Create winning positions tuple (cause it shouldn't be)
# 3. Play the game while there are no empty position left or until someone win
# 4. Ask user to input the position, and replace it with his corresponidng symbol (X or O)
# 5. user1 or user2 on win_position: print("Congratulations🎉! {user} win✨!")

# User input Logic
# 1. After user enters the number, check which range it corresponds
# 2. if number > 3: go to 2nd row, elif number > 6: go to 3rd row and etc

# Validation Logics
# 1. Don't allow user to exceed the range of positions (position_num < 9 and position_num > 0)
# 2. Don't allow users to replace non-empty slot
# 3. Save user moves in some kinda array, if user_move already in moves list: position is already been used!

# Displaying Board Logic
grid = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]

"""for i in range(1, 10):
        print(i, end='|')

        # Seperates rows
        if i % 3 == 0:
            print("\n-+-+-+")  
"""
def display_grid(grid):
    print(f"{grid[0][0]}|{grid[0][1]}|{grid[0][2]}|\n-+-+-+") 
    print(f"{grid[1][0]}|{grid[1][1]}|{grid[1][2]}|\n-+-+-+")
    print(f"{grid[2][0]}|{grid[2][1]}|{grid[2][2]}|\n-+-+-+")   


# Replacing position with user_sign (X or O)
def replace_logic(user_input: int, turn):
    match user_input:
        case 1:
            grid[0][0] = turn

        case 2:
            grid[0][1] = turn  
            
        case 3:
            grid[0][2] = turn 

        case 4:
            grid[1][0] = turn 

        case 5:
            grid[1][1] = turn    

        case 6:
            grid[1][2] = turn 

        case 7:
            grid[2][0] = turn                     

        case 8:
            grid[2][1] = turn  

        case 9:
            grid[2][2] = turn 

        case _:
            print("You have entered invalid position!")
            user_input = int(input("Enter your step (1-9): ")) 

                            

        
print(display_grid(grid))

def main_game():
    win_positions = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7], 
                     [1, 3, 5, 7], [1, 3, 5, 9]
                     )
    
    turn = None
    moves_played = 0
    x_moves = []
    o_moves = []
    
    while True:
        user1_input = int(input("X's turn; Enter your step (1-9): "))

        if user1_input in o_moves:
            print("The Position is already used by 2nd player!")
            user1_input = int(input("Enter your step (1-9): "))

        elif user1_input in x_moves:
            print("You have already used this position!")
            user1_input = int(input("Enter your step (1-9): "))            

        x_moves.append(user1_input)
        x_moves.sort() # Why sort? You need to allow [1, 2, 3] == [1, 3, 2] be True, cause content of the list is same
        moves_played += 1
        replace_logic(user1_input, turn="X")
        print(display_grid(grid))

        if x_moves in win_positions:
            return f"1st Player win!"

        
        user2_input = int(input("O's turn; Enter your step (1-9): "))

        if user2_input in x_moves:
            print("The Position is already used by 1st player!")
            user2_input = int(input("Enter your position (1-9): "))

        elif user2_input in o_moves:
            print("You have already used this position!")
            user1_input = int(input("Enter your position (1-9): "))                   

        o_moves.append(user2_input)
        o_moves.sort() # Why sort? You need to allow [1, 2, 3] == [1, 3, 2] be True, cause content of the list is same
        moves_played += 1
        replace_logic(user2_input, turn="O")

        print(display_grid(grid))
        #print(f"Current move: {moves_played}")


        if o_moves in win_positions:
            return f"2nd Player win!"
        
        if moves_played == 9:
            print("⚖️ It's a draw!")
            break

        
print(main_game())

# Fix issues | Needs Imporvement
# 1. Add exception logic to don't allow users to replace their signs (e.g make same move) ✔
# 2. Handle less win positions, e.g allow unordered positions ✔
# 3. Make one replace logic, which will just replace with whosTurn variable ✔

