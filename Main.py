import ChessEngine as ce
import chess as ch

class Main:

    def __init__(self, board=ch.Board):
        self.board=board

    
    def playHumanMove(self):
        try:
            print("\n")
            print(self.board.legal_moves)
            print("""\nĐể quay lại, nhấn "undo".""")
            print("""Để bắt đầu lại ván mới, nhấn "reset".""")
            play = input("\nLượt của bạn: ")
            print("\n")
            if (play=="undo"):
                self.board.pop()
                self.board.pop()
                print(self.board) 
                self.playHumanMove()
                return
            elif (play=="reset"):
                print("Bắt đầu ván mới")
                self.board.reset_board()
                self.startGame()
                return
            self.board.push_san(play)
        except:
            self.playHumanMove()

    def playEngineMove(self, maxDepth, color):
        engine = ce.Engine(self.board, maxDepth, color)
        self.board.push(engine.getBestMove())

    def startGame(self):
        color=None
        while(color!="đen" and color!="trắng"):
            color = input("""\nChọn màu quân cờ ("đen" hoặc "trắng"): """) 
        maxDepth=None
        while(isinstance(maxDepth, int)==False):
            maxDepth =  int(input("""Chọn độ sâu của bàn cờ: """))
        print("\n") 
        if color=="đen":
            while (self.board.is_checkmate()==False):
                print("\nLượt của máy...\n")
                self.playEngineMove(maxDepth, ch.WHITE)
                print(self.board)
                self.playHumanMove()
                print(self.board)
            print(self.board)
            print(self.board.outcome())  
            print("Màu trắng thắng!")  
        elif color=="trắng":
            while (self.board.is_checkmate()==False):
                print(self.board)
                self.playHumanMove()
                print(self.board)
                print("\nLượt của máy...\n")
                self.playEngineMove(maxDepth, ch.BLACK)
            print(self.board)
            print(self.board.outcome())
            print("Màu đen thắng!")
        self.board.reset
        self.startGame()
#
newBoard= ch.Board()
game = Main(newBoard)
bruh = game.startGame()