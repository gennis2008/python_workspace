inputstr = input("请输入您下棋的坐标，应以x,y的格式：\n")
while inputstr != None:
    try:
        x_str,y_str = inputstr.split(sep = ",")
        if board[int(y_str)] - 1][int(x_str)-1] != "+":
            inputstr = input("您输入的坐标点已有棋子了，请重新输入\n")
            continue
        board[int(y_str)-1][int(x_str)-1] = "."
    except Exception:
        inputstr = input("您输入的坐标不合法，请重新输入，下棋坐标应以x,y的格式\n")
        continue
