import math
import copy
import turtle as t
e = t.Turtle()
e.speed(0)
t.speed(0)

t.penup()
t.goto(-200, 0)
t.pendown()

def showTitle():
	print("■■■ omok ai v2 ■■■")

def showBoard():
	for i in range(LENGTH):
		for j in range(LENGTH):
			c = BLANK_ICON

			if board[4 + i][4 + j] == PLAYER:
				c = PLAYER_ICON
			elif board[4 + i][4 + j] == AI:
				c = AI_ICON

			print(c, end="")
		print()
	print()

def checkReGame():
	global board
	global past_board
	
	print("do you want to regame? (y/n)")
	temp = input(">>")

	if temp == "y":
		print("init...")

		t.clear()
		e.clear()
		
		board = [[BLANK for j in range(LENGTH + 8)] for i in range(LENGTH + 8)]
		past_board = [[BLANK for j in range(LENGTH + 8)] for i in range(LENGTH + 8)]

		print("ok")

		showTitle()

		#첫 돌이 AI돌 일때
		board[4 + (LENGTH // 2) - 1 + 1][4 + (LENGTH // 2) - 1 + 1] = AI

		drawInitBoard()
		drawBoard()
		
	else:
		print("close")

def calAiO():
	bo_list = []
	rx, ry = 1, 1

	for y in range(1, LENGTH + 1):
		for x in range(1, LENGTH + 1):
			index_x = 4 + x - 1
			index_y = 4 + y - 1
			
			o_type = board[index_y][index_x]

			if o_type != BLANK:
				print("("+str(index_x+1)+","+str(index_y+1)+") check")
				
				continue

			av = 0
			dv = 0
			
			#set 1
			avt, dvt = 0, 0
			#위
			o_count = INIT_COUNT
			alpha = 0
			leado_type1 = board[index_y - 1][index_x]
			endo_type = BLANK
			for i in range(2, 6):
				judgeo_type = board[index_y - i][index_x]
				
				if judgeo_type == BLANK:
					break

				if leado_type1 != judgeo_type:
					endo_type = judgeo_type
					break

				o_count = o_count + 1

			if (endo_type != BLANK) and (leado_type1 != endo_type):
				alpha = ALPHA_V

			if leado_type1 == AI:
				avt = avt + math.pow(AV, o_count)
			if leado_type1 == PLAYER:
				dvt = dvt + math.pow(DV, o_count)
				
			av = av + alpha
			dv = dv + alpha

			#아래
			o_count = INIT_COUNT
			alpha = 0
			leado_type2 = board[index_y + 1][index_x]
			endo_type = BLANK
			for i in range(2, 6):
				judgeo_type = board[index_y + i][index_x]
				
				if judgeo_type == BLANK:
					break

				if leado_type2 != judgeo_type:
					endo_type = judgeo_type
					break

				o_count = o_count + 1

			if (endo_type != BLANK) and (leado_type2 != endo_type):
				alpha = ALPHA_V

			if leado_type2 == AI:
				if leado_type1 == leado_type2:
					avt = avt * math.pow(AV, o_count)
				else:
					avt = avt + math.pow(AV, o_count)
					
			if leado_type2 == PLAYER:
				if leado_type1 == leado_type2:
					dvt = dvt * math.pow(DV, o_count)
				else:
					dvt = dvt + math.pow(DV, o_count)
			
			av = av + alpha
			dv = dv + alpha
			
			#set 1 end
			av = av + avt
			dv = dv + dvt
			
			#set 2
			avt, dvt = 0, 0
			#오른쪽
			o_count = INIT_COUNT
			alpha = 0
			leado_type1 = board[index_y][index_x + 1]
			endo_type = BLANK
			for i in range(2, 6):
				judgeo_type = board[index_y][index_x + i]
				
				if judgeo_type == BLANK:
					break

				if leado_type1 != judgeo_type:
					endo_type = judgeo_type
					break

				o_count = o_count + 1

			if (endo_type != BLANK) and (leado_type1 != endo_type):
				alpha = ALPHA_V

			if leado_type1 == AI:
				avt = avt + math.pow(AV, o_count)
			if leado_type1 == PLAYER:
				dvt = dvt + math.pow(DV, o_count)
				
			av = av + alpha
			dv = dv + alpha

			#왼쪽
			o_count = INIT_COUNT
			alpha = 0
			leado_type2 = board[index_y][index_x - 1]
			endo_type = BLANK
			for i in range(2, 6):
				judgeo_type = board[index_y][index_x - i]
				
				if judgeo_type == BLANK:
					break

				if leado_type2 != judgeo_type:
					endo_type = judgeo_type
					break

				o_count = o_count + 1

			if (endo_type != BLANK) and (leado_type2 != endo_type):
				alpha = ALPHA_V

			if leado_type2 == AI:
				if leado_type1 == leado_type2:
					avt = avt * math.pow(AV, o_count)
				else:
					avt = avt + math.pow(AV, o_count)
			if leado_type2 == PLAYER:
				if leado_type1 == leado_type2:
					dvt = dvt * math.pow(DV, o_count)
				else:
					dvt = dvt + math.pow(DV, o_count)

			av = av + alpha
			dv = dv + alpha
			
			#set 2 end
			av = av + avt
			dv = dv + dvt
			
			#set 3
			avt, dvt = 0, 0
			#오른위
			o_count = INIT_COUNT
			alpha = 0
			leado_type1 = board[index_y - 1][index_x + 1]
			endo_type = BLANK
			for i in range(2, 6):
				judgeo_type = board[index_y - i][index_x + i]
				
				if judgeo_type == BLANK:
					break

				if leado_type1 != judgeo_type:
					endo_type = judgeo_type
					break

				o_count = o_count + 1

			if (endo_type != BLANK) and (leado_type1 != endo_type):
				alpha = ALPHA_V

			if leado_type1 == AI:
				avt = avt + math.pow(AV, o_count)
			if leado_type1 == PLAYER:
				dvt = dvt + math.pow(DV, o_count)
			
			av = av + alpha
			dv = dv + alpha

			#왼아래
			o_count = INIT_COUNT
			alpha = 0
			leado_type2 = board[index_y + 1][index_x - 1]
			endo_type = BLANK
			for i in range(2, 6):
				judgeo_type = board[index_y + i][index_x - i]
				
				if judgeo_type == BLANK:
					break

				if leado_type2 != judgeo_type:
					endo_type = judgeo_type
					break

				o_count = o_count + 1

			if (endo_type != BLANK) and (leado_type2 != endo_type):
				alpha = ALPHA_V

			if leado_type2 == AI:
				if leado_type1 == leado_type2:
					avt = avt * math.pow(AV, o_count)
				else:
					avt = avt + math.pow(AV, o_count)
			if leado_type2 == PLAYER:
				if leado_type1 == leado_type2:
					dvt = dvt * math.pow(DV, o_count)
				else:
					dvt = dvt + math.pow(DV, o_count)
					
			av = av + alpha
			dv = dv + alpha
			
			#set 3 end
			av = av + avt
			dv = dv + dvt
			
			#set 4
			avt, dvt = 0, 0
			#오른아래
			o_count = INIT_COUNT
			alpha = 0
			leado_type1 = board[index_y + 1][index_x + 1]
			endo_type = BLANK
			for i in range(2, 6):
				judgeo_type = board[index_y + i][index_x + i]
				
				if judgeo_type == BLANK:
					break

				if leado_type1 != judgeo_type:
					endo_type = judgeo_type
					break

				o_count = o_count + 1

			if (endo_type != BLANK) and (leado_type1 != endo_type):
				alpha = ALPHA_V

			if leado_type1 == AI:
				avt = avt + math.pow(AV, o_count)
			if leado_type1 == PLAYER:
				dvt = dvt + math.pow(DV, o_count)
				
			av = av + alpha
			dv = dv + alpha

			#왼위
			o_count = INIT_COUNT
			alpha = 0
			leado_type2 = board[index_y - 1][index_x - 1]
			endo_type = BLANK
			for i in range(2, 6):
				judgeo_type = board[index_y - i][index_x - i]
				
				if judgeo_type == BLANK:
					break

				if leado_type2 != judgeo_type:
					endo_type = judgeo_type
					break

				o_count = o_count + 1

			if (endo_type != BLANK) and (leado_type2 != endo_type):
				alpha = ALPHA_V

			if leado_type2 == AI:
				if leado_type1 == leado_type2:
					avt = avt * math.pow(AV, o_count)
				else:
					avt = avt + math.pow(AV, o_count)
			if leado_type2 == PLAYER:
				if leado_type1 == leado_type2:
					dvt = dvt * math.pow(DV, o_count)
				else:
					dvt = dvt + math.pow(DV, o_count)

			av = av + alpha
			dv = dv + alpha
			
			#set 4 end
			av = av + avt
			dv = dv + dvt

			rv = (WEIGHT_V*av)+dv
			v = av
			v_type = 1
			
			if dv > v:
				rv = (WEIGHT_V*dv)+av
				v = dv
				v_type = 0

			bo_list.append({
				"x": x,
				"y": y,
				"v": rv,
				"vt": v_type
			})

			print("("+str(index_x+1)+","+str(index_y+1)+")", "av:", av, "dv:", dv, "rv:", rv)
	
	max_v = 0
	max_vt = "X"
	for bo in bo_list:
		x = bo["x"]
		y = bo["y"]
		v = bo["v"]
		if v > max_v:
			rx = x
			ry = y
			max_v = v
			max_vt = bo["vt"]

	return (rx, ry, max_v, max_vt)

def judgeWl():
	print("return win or lose...")

	for y in range(1, LENGTH + 1):
		for x in range(1, LENGTH + 1):
			o_type = board[4 + y - 1][4 + x - 1]

			if o_type == BLANK:
				continue

			index_x = 4 + x - 1
			index_y = 4 + y - 1

			for i in range(1, 5):
				judgeo_type = board[index_y - i][index_x]

				if o_type != judgeo_type:
					break
				else:
					if i == 4:
						if o_type == PLAYER:
							return 1
						else:
							return 0

			index_x = 4 + x - 1
			index_y = 4 + y - 1

			for i in range(1, 5):
				judgeo_type = board[index_y][index_x + i]

				if o_type != judgeo_type:
					break
				else:
					if i == 4:
						if o_type == PLAYER:
							return 1
						else:
							return 0

			index_x = 4 + x - 1
			index_y = 4 + y - 1

			for i in range(1, 5):
				judgeo_type = board[index_y + i][index_x]

				if o_type != judgeo_type:
					break
				else:
					if i == 4:
						if o_type == PLAYER:
							return 1
						else:
							return 0
						
			index_x = 4 + x - 1
			index_y = 4 + y - 1

			for i in range(1, 5):
				judgeo_type = board[index_y][index_x - i]

				if o_type != judgeo_type:
					break
				else:
					if i == 4:
						if o_type == PLAYER:
							return 1
						else:
							return 0

			index_x = 4 + x - 1
			index_y = 4 + y - 1

			for i in range(1, 5):
				judgeo_type = board[index_y - i][index_x + i]

				if o_type != judgeo_type:
					break
				else:
					if i == 4:
						if o_type == PLAYER:
							return 1
						else:
							return 0

			index_x = 4 + x - 1
			index_y = 4 + y - 1

			for i in range(1, 5):
				judgeo_type = board[index_y + i][index_x - i]
				
				if o_type != judgeo_type:
					break
				else:
					if i == 4:
						if o_type == PLAYER:
							return 1
						else:
							return 0

			index_x = 4 + x - 1
			index_y = 4 + y - 1

			for i in range(1, 5):
				judgeo_type = board[index_y + i][index_x - i]

				if o_type != judgeo_type:
					break
				else:
					if i == 4:
						if o_type == PLAYER:
							return 1
						else:
							return 0

			index_x = 4 + x - 1
			index_y = 4 + y - 1

			for i in range(1, 5):
				judgeo_type = board[index_y - i][index_x - i]

				if o_type != judgeo_type:
					break
				else:
					if i == 4:
						if o_type == PLAYER:
							return 1
						else:
							return 0

	return -1;

def runPlayerOrder(x, y):
	print("---player time---")
	print("ai:", AI_ICON, "player:", PLAYER_ICON, "board size:", str(LENGTH) + "×" + str(LENGTH))
	showBoard()
	px, py = x, y

	if board[4 + py - 1][4 + px - 1] != BLANK:
		return -1

	board[4 + py - 1][4 + px - 1] = PLAYER
	return 1
	
def runAiOrder():
	print("---ai time---")
	print("ai calculating...")
	temp = calAiO()
	rx, ry, max_v, max_vt = temp[0], temp[1], temp[2], temp[3]
	
	board[4 + ry - 1][4 + rx - 1] = AI
	
	print("[cal result]")
	print("x:", rx, "y:", ry)
	if max_vt == 1:
		print("type: attack")
	elif max_vt == 0:
		print("type: defense")
	else:
		print("type: none")
	print("v:", max_v)

def drawBoard():
	global board
	global past_board

	print("draw board...")
	
	t.penup()
	t.goto(0, 0)
	
	for i in range(LENGTH):
		for j in range(LENGTH):
			if board[4 + i][4 + j] == AI and board[4 + i][4 + j] != past_board[4 + i][4 + j]:
				t.color("black", "white")
			elif board[4 + i][4 + j] == PLAYER and board[4 + i][4 + j] != past_board[4 + i][4 + j]:
				t.color("black", "black")
			else:
				continue
								
			t.goto(pos[i][j][0][0], (pos[i][j][0][1]+pos[i][j][1][1])//2)
			t.pendown()
			t.setheading(270)
			t.begin_fill()
			t.circle(SIZE//2)
			t.end_fill()
			t.setheading(0)
			t.penup()
			
	past_board = copy.deepcopy(board)

	print("finish")

def drawInitBoard():
	print("draw init board...")

	t.penup()
	t.goto(0, 0)
	
	t.color("black", "chocolate")
	t.goto(pos[0][0][0][0], pos[0][0][0][1])
	t.begin_fill()
	t.goto(pos[0][LENGTH-1][1][0], pos[0][LENGTH-1][0][1])
	t.goto(pos[0][LENGTH-1][1][0], pos[0][LENGTH-1][0][1]-(SIZE*LENGTH))
	t.goto(pos[0][0][0][0], pos[0][LENGTH-1][0][1]-(SIZE*LENGTH))
	t.goto(pos[0][0][0][0], pos[0][0][0][1])
	t.end_fill()
	
	for i in range(LENGTH):
		t.goto(pos[0][i][0][0], pos[0][i][0][1])
		t.pendown()
		t.goto(pos[0][i][0][0], pos[0][i][0][1]-(SIZE*LENGTH))
		t.penup()
	
	t.goto(pos[0][LENGTH-1][1][0], pos[0][LENGTH-1][0][1])
	t.pendown()
	t.goto(pos[0][LENGTH-1][1][0], pos[0][LENGTH-1][0][1]-(SIZE*LENGTH))
	t.penup()
		
	for i in range(LENGTH):
		t.goto(pos[i][0][0][0], pos[i][0][0][1])
		t.pendown()
		t.goto(pos[i][0][0][0]+(SIZE*LENGTH), pos[i][0][0][1])
		t.penup()
	
	t.goto(pos[LENGTH-1][0][0][0], pos[LENGTH-1][0][1][1])
	t.pendown()
	t.goto(pos[LENGTH-1][0][0][0]+(SIZE*LENGTH), pos[LENGTH-1][0][1][1])
	t.penup()

	print("finish")

def click(x, y):	
	px, py = "a", "a"
	
	for i in range(LENGTH):
		for j in range(LENGTH):
			if (x >= pos[i][j][0][0] and x <= pos[i][j][1][0]) and (y <= pos[i][j][0][1] and y >= pos[i][j][1][1]):
				px, py = j+1, i+1
				break
		if px != "a":
				break
	if px != "a":
		j = runPlayerOrder(px, py)

		if j == -1:
			print("[warning]")
			print("you click two times")
			t.write("warning")
		else:
			drawBoard()
			j = judgeWl()
	
			if j == 1:
				print("[cal result]")
				print("player win / ai lose")
				t.color("red")
				t.write("player win")

				checkReGame()
				
			elif j == 0:
				print("[cal result]")
				print("player lose / ai win")
				t.color("red")
				t.write("ai win")

				checkReGame()
				
			else:
				print("[cal result]")
				print("nothing")
				
				runAiOrder()
				drawBoard()

				j = judgeWl()
	
				if j == 1:
					print("[cal result]")
					print("player win / ai lose")
					t.color("red")
					t.write("player win")

					checkReGame()
					
				elif j == 0:
					print("[cal result]")
					print("player lose / ai win")
					t.color("red")
					t.write("ai win")

					checkReGame()
					
				else:
					print("[cal result]")
					print("nothing")

BLANK = 0
AI = 1
PLAYER = 2

BLANK_ICON = "0"
AI_ICON = "a"
PLAYER_ICON = "p"

LENGTH = 18
SIZE = 30

AV = 2 #공격성
DV = 2.3 #방어성
ALPHA_V = -1 #차단 여부 가치
WEIGHT_V = 2 #bias 가치
INIT_COUNT = 1 #첫 돌의 가치

board = [[BLANK for j in range(LENGTH + 8)] for i in range(LENGTH + 8)]
past_board = [[BLANK for j in range(LENGTH + 8)] for i in range(LENGTH + 8)]

pos = []
for i in range(0, -1*SIZE*LENGTH, -1*SIZE):
	temp = []
	for j in range(0, SIZE*LENGTH, SIZE):
		temp.append(((j-(SIZE*(LENGTH//2)), i+(SIZE*LENGTH*0.6) - 50), (j+SIZE-(SIZE*(LENGTH//2)), i-SIZE+(SIZE*LENGTH*0.6) - 50)))
	pos.append(temp)

vpos = copy.deepcopy(pos)

showTitle()

#첫 돌이 AI돌 일때
board[4 + (LENGTH // 2) - 1 + 1][4 + (LENGTH // 2) - 1 + 1] = AI

drawInitBoard()
drawBoard()

t.onscreenclick(click)
t.mainloop()