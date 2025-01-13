def play(self):
    while True:
        self.print_board()
        try:
            x = int(input("Enter x coordinate: "))
            y = int(input("Enter y coordinate: "))

            # Vérifier si les coordonnées sont valides
            if x < 0 or x >= self.width or y < 0 or y >= self.height:
                print("Coordinates out of bounds. Please try again.")
                continue

            if not self.reveal(x, y):
                self.print_board(reveal=True)
                print("Game Over! You hit a mine.")
                break

        except ValueError:
            print("Invalid input. Please enter numbers only.")
