def print_board(board):
"""Функция для печати игрового поля."""
for row in board:
print(" | ".join(row))
print("-" * 5)

def check_winner(board):
"""Функция проверки завершенности игры."""
# Проверка строк
for row in board:
if row[0] == row[1] == row[2] and row[0] != " ":
return row[0]
# Проверка столбцов
for col in range(3):
if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
return board[0][col]
# Проверка диагоналей
if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
return board[0][0]
if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
return board[0][2]
# Проверка на ничью
for row in board:
if " " in row:
return None
return "Draw"

def is_valid_move(board, row, col):
"""Проверка корректности ввода."""
return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "

def main():
"""Основная функция игры."""
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

while True:
print_board(board)
print(f"Ход игрока {current_player}.")

try:
row, col = map(int, input("Введите номер строки и столбца (через пробел): ").split())
except ValueError:
print("Введите два числа через пробел!")
continue

if not is_valid_move(board, row, col):
print("Некорректный ход. Попробуйте снова.")
continue

board[row][col] = current_player
winner = check_winner(board)

if winner:
print_board(board)
if winner == "Draw":
print("Ничья!")
else:
print(f"Игрок {winner} победил!")
break

current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
main()