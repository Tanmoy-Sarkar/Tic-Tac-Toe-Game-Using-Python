#function for showing the present state of the game
def game_canvas():
	print(str(num_states[0])+"|"+str(num_states[1])+"|"+str(num_states[2])+ "\n" +
		str(num_states[3])+"|"+str(num_states[4])+"|"+str(num_states[5])+ "\n" +
		str(num_states[6])+"|"+str(num_states[7])+"|"+str(num_states[8]))

#function for taking input from player 1
def user_input_1():
	turn_of_1=False
	while turn_of_1 == False:
		turn1=int(input("Which Position You Want To Put"))
		#checking if the given position is within range and if it is previously filled or not
		if turn1 in range(10) and num_states[turn1-1] != "o" and num_states[turn1-1] != "*":
			num_states[turn1-1]="o"
			turn_of_1=True
		else:
			print("Enter Within the Given Positions Available")

#function for taking input from player 1
def user_input_2():
	turn_of_2=False
	while turn_of_2 == False:
		turn2=int(input("Which Position You Want To Put"))
		#checking if the given position is within range and if it is previously filled or not
		if turn2 in range(10) and num_states[turn2-1] != "*" and num_states[turn2-1] != "o" :
			num_states[turn2-1]="*"
			turn_of_2=True	
		else:
			print("Enter Within the Given Positions Available")

#function for evaluating the outcome of the game
def evaluate(present_turn):
	
	#for checking if horizontal lines are matched
	for i in range(0,9,3):
		if num_states[i]==num_states[i+1]==num_states[i+2]:
			print("Game Over")
			print(present_turn + "won the game")
			game_canvas()
			return True
	#for checking if vertical lines are matched	 		
	for j in range(0,3,1):
		if num_states[j]==num_states[j+3]==num_states[j+6]:
			print("Game Over")
			print(present_turn + "won the game")
			game_canvas()
			return True
	#for checking the two diagonals from each side if they are matched
	temp = 4
	for k in range(0,3,2):
		if num_states[k]==num_states[k+temp]==num_states[k+(temp*2)]:
			print("Game Over")
			print(present_turn + "won the game")
			game_canvas()
			return True
		else:
			temp = 2
	return False
#main game function
def mainGame():
	global num_states
	num_states=[1,2,3,4,5,6,7,8,9]
	turn=0
	game_status = False
	while game_status == False:
		game_canvas()
		print("player(o) Enter Your Turn")
		user_input_1()
		present_turn = "player(o)"
		condition=evaluate(present_turn)
		turn += 1
		if condition == True:
			break
		#if nine turn is given and no result is found the match is given tied
		if turn == 9:
			print("Game is tied")
			break
		print("player(*) Enter Your Turn")
		game_canvas()
		user_input_2()
		present_turn = "player(*)"
		game_status=evaluate(present_turn)
		turn += 1
	#asking user if they want to continue the game
	print("Want To Play Again If Yes Press Y Else Press Any Other Key")
	n=input()
	if n == "y" or n=="Y":
		turn=0
		mainGame()
	else:
		exit()
		
if __name__ == '__main__':
	mainGame()
	
	 