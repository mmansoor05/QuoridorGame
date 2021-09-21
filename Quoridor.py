class Fence:
    """A class to represent a fence with direction (horizontal/vertical) and number of fences."""
    def __init__(self):
        """The constructor for Fence class. Takes no parameters. Initializes the required data members."""
        self._fence_horizontal = "-"
        self._fence_vertical = "|"
        self._fences_p1 = 10
        self._fences_p2 = 10

    def get_fence_horizontal(self):
        """Gets the horizontal fence. Used by QuordidorGame class to get horizontal fence to be placed at given
        position."""
        return self._fence_horizontal

    def get_fence_vertical(self):
        """Gets the vertical fence. Used by QuordidorGame class to get vertical fence to be placed at given position."""
        return self._fence_vertical

    def get_fences_p1(self):
        """Gets total number of fences for Player 1."""
        return self._fences_p1

    def get_fences_p2(self):
        """Gets total number of fences for Player 2."""
        return self._fences_p2


class QuoridorGame:
    """QuoridorGame class to represent Quoridor game, played by two players. Player 1 always starts first.
    Returns True if is a valid move, or a valid fence placement or if one of the player wins. Uses Fence class for fence
    to use those data members."""
    def __init__(self):
        """Constructor for QuoridorGame  class. Initializes the board with the fences and pawns (P1 and P2) placed in correct positions. """
        self._board = [
            [["|", "", "X"], ["-", "", "X"], ["-", "", "X"], ["-", "", "X"], ["-", "", "P1"], ["-", "", "X"],
             ["-", "", "X"],
             ["-", "", "X"], ["-", "", "X"], ["||"]],
            [["|", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"],
             ["", "", "X"], ["", "", "X"], ["||"]],
            [["|", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"],
             ["", "", "X"], ["", "", "X"], ["||"]],
            [["|", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"],
             ["", "", "X"], ["", "", "X"], ["||"]],
            [["|", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"],
             ["", "", "X"], ["", "", "X"], ["||"]],
            [["|", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"],
             ["", "", "X"], ["", "", "X"], ["||"]],
            [["|", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"],
             ["", "", "X"], ["", "", "X"], ["||"]],
            [["|", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"],
             ["", "", "X"], ["", "", "X"], ["||"]],
            [["|", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "X"], ["", "", "P2"], ["", "", "X"], ["", "", "X"],
             ["", "", "X"], ["", "", "X"], ["||"]],
            [["-", "", ""], ["-", "", ""], ["-", "", ""], ["-", "", ""], ["-", "", ""], ["-", "", ""], ["-", "", ""],
             ["-", "", ""], ["-", "", ""]]]
        self._fence = Fence()
        self._turn = 1
        self._current_state = "UNFINISHED"
        self._num_fence_p1 = self._fence.get_fences_p1()
        self._num_fence_p2 = self._fence.get_fences_p2()
        self._v_fence = self._fence.get_fence_vertical()
        self._h_fence = self._fence.get_fence_horizontal()

    def same_player_turn(self, player_number):
        """Ensures that same player can’t make more than one valid turn"""
        # if same player makes another turn, return False
        if self._turn != player_number:
            return False
        return True

    def switch_turns(self):
        """Takes no parameter. Switches the turns between both players"""
        # if move is valid, update turn to other player
        if self._turn == 1:
            self._turn = 2
        else:
            self._turn = 1
        return True

    def lock_borders(self, coordinate_tuple):
        """Checks if the move/fence is out of the board."""
        (y_coord, x_coord) = coordinate_tuple
        if y_coord < 0 or x_coord < 0:
            return False
        if y_coord > 8 or x_coord > 8:
            return False
        return True

    def validate_move_pawn1(self, player_number, x_dest, y_dest):
        """Checks validity of left, right, forward, backward movement of the pawn1 on board."""
        current = self._board[x_dest][y_dest]
        right = self._board[x_dest][y_dest + 1]
        if player_number == 1:
            # check validity for right movement
            if y_dest > 0:
                if self._board[x_dest][y_dest - 1][2] == "P1" and current[2] == "X" and current[1] != self._v_fence:
                    return True
            # check validity for forward movement
            if x_dest > 0:
                if self._board[x_dest - 1][y_dest][2] == "P1" and current[2] == "X" and current[0] != self._h_fence:
                    return True
            # check validity for backwards movement if x coordinate is equal to zero
            if x_dest == 0:
                if self._board[x_dest + 1][y_dest][2] == "P1" and current[2] == "X":
                    return True
            # check validity for backwards movement
            if x_dest < 8:
                if self._board[x_dest + 1][y_dest][2] == "P1" and current[2] == "X" and current[0] != self._h_fence:
                    return True
            # check validity for left movement
            if y_dest < 8:
                if self._board[x_dest][y_dest + 1][2] == "P1" and current[2] == "X" and right[1] != self._v_fence:
                    return True
        # if it is second player, then return True
        elif player_number == 2:
            return True
        return False

    def validate_move_pawn2(self, player_number, x_dest, y_dest):
        """Checks validity of left, right, forward, backward movement of the pawn2 on board."""
        current = self._board[x_dest][y_dest]
        right = self._board[x_dest][y_dest + 1]
        if player_number == 2:
            # check validity for right movement
            if y_dest > 0:
                if self._board[x_dest][y_dest - 1][2] == "P2" and current[2] == "X" and current[1] != self._v_fence:
                    return True
            # check validity for left movement
            if y_dest < 8:
                if right[2] == "P2" and current[2] == "X" and right[1] != self._v_fence:
                    return True
            # check validity for forward movement
            if x_dest > 0:
                if self._board[x_dest - 1][y_dest][2] == "P2" and current[2] == "X" and current[0] != self._h_fence:
                    return True
            # check validity for backwards movement if x coordinate is equal to zero
            if x_dest == 0:
                if self._board[x_dest + 1][y_dest][2] == "P2" and current[2] == "X":
                    return True
            # check validity for backwards movement
            if x_dest < 8:
                if self._board[x_dest + 1][y_dest][2] == "P2" and current[2] == "X" and current[0] != self._h_fence:
                    return True
        # if it is first player, then return True
        elif player_number == 1:
            return True
        return False

    def validate_jump_pawn1(self, player_number, x_dest, y_dest):
        """Validates the pawn1 jumping over pawn2 if both pawns are face to face and there is a fence at the back of pawn2.
    Checks validity of left, right, forward, backward movement of the pawn1 on board. Also checks for diagonal validity
    if fences are found at the back of pawn2."""
        current = self._board[x_dest][y_dest]
        diagonal_left = self._board[x_dest + 1][y_dest + 1]
        diagonal_right = self._board[x_dest + 1][y_dest - 1]
        right = self._board[x_dest][y_dest + 1]
        forward = self._board[x_dest + 1][y_dest]
        left = self._board[x_dest][y_dest - 1]
        if player_number == 1:
            # check for forward jump validity
            if x_dest >= 2:
                if self._board[x_dest - 2][y_dest][2] == "P1" and left[2] == "P2" and current[0] != self._h_fence:
                    return True
            # check for backwards jump validity
            if x_dest < 7:
                if self._board[x_dest + 2][y_dest][2] == "P1" and forward[2] == "P2" and forward[0] != self._h_fence:
                    return True
            # check diagonal validity if fence at back and moving forward
            if x_dest > 0 and y_dest < 8:
                # checking diagonal left
                if self._board[x_dest - 1][y_dest + 1][2] == "P1" and right[2] == "P2" and diagonal_left[0] == \
                        self._h_fence and right[1] != self._v_fence and current[0] != self._h_fence:
                    return True
            if x_dest > 0 and y_dest > 0:
                # checking diagonal right
                if self._board[x_dest - 1][y_dest - 1][2] == "P1" and left[2] == "P2" and diagonal_right[0] == \
                        self._h_fence and current[1] != self._v_fence and current[0] != self._h_fence:
                    return True
            # check diagonal validity if fence at back and moving backwards
            if x_dest < 8 and y_dest < 8:
                # checking diagonal left
                if diagonal_left[2] == "P1" and right[2] == "P2" and right[0] == self._h_fence and forward[0] \
                        != self._h_fence and right[1] != self._v_fence:
                    return True
            if x_dest < 8 and y_dest > 0:
                # checking diagonal right
                if diagonal_right[2] == "P1" and left[2] == "P2" and left[0] == self._h_fence and forward[0] \
                        != self._h_fence and current[1] != self._v_fence:
                    return True
        return False

    def validate_jump_pawn2(self, player_number, x_dest, y_dest):
        """Validates the pawn2 jumping over pawn1 if both pawns are face to face and there is a fence at the back of pawn1.
       Checks validity of left, right, forward, backward movement
        of the pawn2 on board. Also checks for diagonal validity if fences are found at the back of pawn1."""
        current = self._board[x_dest][y_dest]
        diagonal_left = self._board[x_dest + 1][y_dest + 1]
        diagonal_right = self._board[x_dest + 1][y_dest - 1]
        right = self._board[x_dest][y_dest + 1]
        forward = self._board[x_dest + 1][y_dest]
        left = self._board[x_dest][y_dest - 1]
        if player_number == 2:
            # check for forward jump validity
            if 2 <= x_dest < 8:
                if self._board[x_dest - 2][y_dest][2] == "P2" and self._board[x_dest - 1][y_dest][2] == "P1" and \
                        current[0] != self._h_fence:
                    return True
            # check for backwards jump validity
            if x_dest < 7:
                if self._board[x_dest + 2][y_dest][2] == "P2" and forward[2] == "P1" and forward[0] != self._h_fence:
                    return True
            # check diagonal validity if fence at back and moving forward
            if x_dest > 0 and y_dest < 8:
                # checking diagonal left
                if self._board[x_dest - 1][y_dest + 1][2] == "P2" and right[2] == "P1" and diagonal_left[0] == \
                        self._h_fence and right[1] != self._v_fence and current[0] != self._h_fence:
                    return True
            if x_dest > 0 and y_dest > 0:
                # checking diagonal right
                if self._board[x_dest - 1][y_dest - 1][2] == "P2" and left[2] == "P1" and diagonal_right[0] == \
                        self._h_fence and current[1] != self._v_fence and current[0] != self._h_fence:
                    return True
            # check diagonal validity if fence at back and moving backwards
            if x_dest < 8 and y_dest < 8:
                # checking diagonal left
                if diagonal_left[2] == "P2" and right[2] == "P1" and right[0] == self._h_fence and forward[0] != \
                        self._h_fence and right[1] != self._v_fence:
                    return True
            if x_dest < 8 and y_dest > 0:
                # checking diagonal right
                if diagonal_right[2] == "P2" and left[2] == "P1" and left[0] == self._h_fence and forward[0] != \
                        self._h_fence and current[1] != self._v_fence:
                    return True
        return False

    def jump_move_pawn1(self, player_number, x_dest, y_dest):
        """Actual move occurs here for pawn1 jumping over pawn2 if pawn1 and pawn2 are face to face and there is no fence
        at the back of pawn2. Jumps right, left, forward, backwards as per the requirements."""
        current = self._board[x_dest][y_dest]
        if player_number == 1:
            # if jumping forward, makes the move if it meets the criteria
            if x_dest > 1:
                if self._board[x_dest - 2][y_dest][2] == "P1" and self._board[x_dest - 1][y_dest][2] == "P2" and \
                        current[0] != self._h_fence:
                    current[2] = "P1"
                    self._board[x_dest - 2][y_dest][2] = "X"
            # if jumping backwards, makes the move if it meets the criteria
            if x_dest < 7:
                if self._board[x_dest + 2][y_dest][2] == "P1" and self._board[x_dest + 1][y_dest][2] == "P2" and \
                        self._board[x_dest + 1][y_dest][0] != self._h_fence:
                    current[2] = "P1"
                    self._board[x_dest + 2][y_dest][2] = "X"
        # if it is second player, then return True
        elif player_number == 2:
            return True
        return True

    def jump_move_pawn2(self, player_number, x_dest, y_dest):
        """Actual move occurs here for pawn2 jumping over pawn2 if pawn2 and pawn1 are face to face and there is no fence
        at the back of pawn1. Jumps right, left, forward, backwards as per the requirements"""
        current = self._board[x_dest][y_dest]
        if player_number == 2:
            # if jumping forward, makes the move if it meets the criteria
            if x_dest > 1:
                if self._board[x_dest - 2][y_dest][2] == "P2" and self._board[x_dest - 1][y_dest][2] == "P1" and \
                        current[0] != self._h_fence:
                    current[2] = "P2"
                    self._board[x_dest - 2][y_dest][2] = "X"
            # if jumping backwards, makes the move if it meets the criteria
            if x_dest < 7:
                if self._board[x_dest + 2][y_dest][2] == "P2" and self._board[x_dest + 1][y_dest][2] == "P1" and \
                        self._board[x_dest + 1][y_dest][0] != self._h_fence:
                    current[2] = "P2"
                    self._board[x_dest + 2][y_dest][2] = "X"
        # if it is first player, then return True
        elif player_number == 1:
            return True
        return True

    def move_diagonal_pawn1(self, player_number, x_dest, y_dest):
        """Pawn1 is moved diagonally if there is a fence at the back of pawn2.
       Moves diagonal right and left for both forward and backward jumps as per user input."""
        if player_number == 1 and 0 < x_dest < 8 and 8 > y_dest > 0:
            current = self._board[x_dest][y_dest]
            diagonal_right = self._board[x_dest + 1][y_dest + 1]
            diagonal_up_left = self._board[x_dest - 1][y_dest - 1]
            right = self._board[x_dest][y_dest + 1]
            left = self._board[x_dest][y_dest - 1]
            # move diagonal left - for forward jumping
            if self._board[x_dest - 1][y_dest + 1][2] == "P1" and right[2] == "P2" and diagonal_right[0] == self._h_fence:
                self._board[x_dest - 1][y_dest + 1][2] = "X"
                current[2] = "P1"
            # move diagonal right - for forward jumping
            if diagonal_up_left[2] == "P1" and left[2] == "P2" and self._board[x_dest + 1][y_dest - 1][0] == self._h_fence:
                diagonal_up_left[2] = "X"
                current[2] = "P1"
            # move diagonal left - for backward jumping
            if diagonal_right[2] == "P1" and right[2] == "P2" and right[0] == self._h_fence:
                diagonal_right[2] = "X"
                current[2] = "P1"
            # move diagonal right - for backward jumping
            if self._board[x_dest + 1][y_dest - 1][2] == "P2" and left[2] == "P2" and left[0] == self._h_fence:
                self._board[x_dest + 1][y_dest - 1][2] = "X"
                current[2] = "P1"

    def move_diagonal_pawn2(self, player_number, x_dest, y_dest):
        """Pawn2 is moved diagonally if there is a fence at the back of pawn1.
       Moves diagonal right and left for both forward and backward jumps as per user input"""
        if player_number == 2 and 0 < x_dest < 8 and 8 > y_dest > 0:
            current = self._board[x_dest][y_dest]
            diagonal_right = self._board[x_dest + 1][y_dest + 1]
            diagonal_left = self._board[x_dest - 1][y_dest - 1]
            right = self._board[x_dest][y_dest + 1]
            left = self._board[x_dest][y_dest - 1]
            # move diagonal left - for forward jumping
            if self._board[x_dest - 1][y_dest + 1][2] == "P2" and right[2] == "P1" and diagonal_right[0] == self._h_fence:
                    self._board[x_dest - 1][y_dest + 1][2] = "X"
                    current[2] = "P2"
            # move diagonal right - for forward jumping
            if diagonal_left[2] == "P2" and left[2] == "P1" and self._board[x_dest + 1][y_dest - 1][0] == self._h_fence:
                self._board[x_dest - 1][y_dest - 1][2] = "X"
                current[2] = "P2"
            # move diagonal left - for backward jumping
            if diagonal_right[2] == "P2" and right[2] == "P1" and right[0] == self._h_fence:
                diagonal_right[2] = "X"
                current[2] = "P2"
            # move diagonal right - for backward jumping
            if self._board[x_dest + 1][y_dest - 1][2] == "P2" and left[2] == "P1" and left[0] == self._h_fence:
                self._board[x_dest + 1][y_dest - 1][2] = "X"
                current[2] = "P2"

    def move_pawn_1(self, player_number, x_dest, y_dest):
        """Moves pawn1 according to given coordinates. Pawn can be moved to right, left, forward, backwards"""
        current = self._board[x_dest][y_dest]
        if player_number == 1:
            # checking and moving to right side
            if y_dest > 0:
                if self._board[x_dest][y_dest - 1][2] == "P1" and current[1] != self._v_fence:
                    self._board[x_dest][y_dest - 1][2] = "X"
                    current[2] = "P1"
            # checking and moving forward
            if x_dest > 0:
                if self._board[x_dest - 1][y_dest][2] == "P1" and current[0] != self._h_fence:
                    self._board[x_dest - 1][y_dest][2] = "X"
                    current[2] = "P1"
            if x_dest == 0:
                if self._board[x_dest + 1][y_dest][2] == "P1" and current[2] == "X":
                    self._board[x_dest + 1][y_dest][2] = "X"
                    current[2] = "P1"
            # checking and moving to left side
            if y_dest < 8:
                if self._board[x_dest][y_dest + 1][2] == "P1" and current[1] != self._v_fence:
                    self._board[x_dest][y_dest + 1][2] = "X"
                    current[2] = "P1"
            # checking and moving backwards
            if x_dest < 8:
                if self._board[x_dest + 1][y_dest][2] == "P1" and current[0] != self._h_fence:
                    self._board[x_dest + 1][y_dest][2] = "X"
                    current[2] = "P1"

    def move_pawn_2(self, player_number, x_dest, y_dest):
        """Moves pawn2 according to given coordinates. Pawn can be moved to right, left, forward, backwards"""
        current = self._board[x_dest][y_dest]
        if player_number == 2:
            # checking and moving to right side
            if y_dest > 0:
                if self._board[x_dest][y_dest - 1][2] == "P2" and current[1] != self._v_fence:
                    self._board[x_dest][y_dest - 1][2] = "X"
                    current[2] = "P2"
            # checking and moving to left side
            if y_dest < 8:
                if self._board[x_dest][y_dest + 1][2] == "P2" and current[1] != self._v_fence:
                    self._board[x_dest][y_dest + 1][2] = "X"
                    current[2] = "P2"
            # checking and moving forward
            if x_dest > 0:
                if self._board[x_dest - 1][y_dest][2] == "P2" and current[0] != self._h_fence:
                    self._board[x_dest - 1][y_dest][2] = "X"
                    current[2] = "P2"
            if x_dest == 0:
                if self._board[x_dest + 1][y_dest][2] == "P2" and current[2] == "X":
                    self._board[x_dest + 1][y_dest][2] = "X"
                    current[2] = "P2"
            # checking and moving backwards
            if x_dest < 8:
                if self._board[x_dest + 1][y_dest][2] == "P2" and current[0] != self._h_fence:
                    self._board[x_dest + 1][y_dest][2] = "X"
                    current[2] = "P2"
            if y_dest == 8:
                # move right
                if self._board[x_dest][y_dest - 2][2] == "P1" and self._board[x_dest][y_dest - 1][2] == "P2" and \
                        current[0] != self._h_fence:
                    current[2] = "P1"
                    self._board[x_dest][y_dest - 2][2] = "X"

    def place_fence_player1(self, player_number, direction, x_dest, y_dest):
        """Places fence for player1 depending on the direction of the fence. Subtracts 1 every time a fence is placed."""
        current = self._board[x_dest][y_dest]
        if player_number == 1:
            # checks if it is horizontal fence, if yes places a fence and subtracts one from total fences for player 1
            if direction == "h" and current[0] != self._h_fence:
                current[0] = self._h_fence
                self._num_fence_p1 -= 1
                return True
            # checks if number of fences is 0, if yes, returns False
            if self._num_fence_p2 < 1:
                return False
            # checks if it is vertical fence, if yes places a fence and subtracts one from total fences for player 1
            elif direction == "v" and current[1] != self._v_fence:
                current[1] = self._v_fence
                self._num_fence_p1 -= 1
                return True
            # checks if number of fences is 0, if yes, returns False
            if self._num_fence_p1 < 1:
                return False
        elif player_number == 2:
            return True
        return False

    def place_fence_player2(self, player_number, direction, x_dest, y_dest):
        """Places fence for player2 depending on the direction of the fence. Subtracts 1 every time a fence is placed."""
        current = self._board[x_dest][y_dest]
        if player_number == 2:
            # checks if it is horizontal fence, if yes places a fence and subtracts one from total fences for player 2
            if direction == "h" and player_number == 2 and current[0] != self._h_fence:
                current[0] = self._h_fence
                self._num_fence_p2 -= 1
                return True
            # checks if number of fences is 0, if yes, returns False
            if self._num_fence_p2 < 1:
                return False
            # checks if it is vertical fence, if yes places a fence and subtracts one from total fences for player 2
            elif direction == "v" and player_number == 2 and current[1] != self._v_fence:
                current[1] = self._v_fence
                self._num_fence_p2 -= 1
                return True
            # checks if number of fences is 0, if yes, returns False
            if self._num_fence_p2 < 1:
                return False
        elif player_number == 1:
            return True
        return False

    def move_pawn(self, player_number, coordinate_tuple):
        """Takes into account all the game rules of making a valid move and preventing an invalid one and returns True or
      False based on that."""
        (y_coord, x_coord) = coordinate_tuple
        if not self.same_player_turn(player_number):
            return False
        if not self.lock_borders(coordinate_tuple):
            return False
        if not self.validate_move_pawn1(player_number, x_coord, y_coord):
            if not self.validate_jump_pawn1(player_number, x_coord, y_coord):
                return False
        if not self.validate_move_pawn2(player_number, x_coord, y_coord):
            if not self.validate_jump_pawn2(player_number, x_coord, y_coord):
                return False
        if not self.jump_move_pawn1(player_number, x_coord, y_coord):
            return False
        if not self.jump_move_pawn2(player_number, x_coord, y_coord):
            return False
        self.move_diagonal_pawn1(player_number, x_coord, y_coord)
        self.move_diagonal_pawn2(player_number, x_coord, y_coord)
        self.move_pawn_1(player_number, x_coord, y_coord)
        self.move_pawn_2(player_number, x_coord, y_coord)
        if not self.switch_turns():
            return False
        if self._current_state != "UNFINISHED":
            return False
        self.win_logic(player_number, x_coord, y_coord)
        return True

    def place_fence(self, player_number, direction, coordinate_tuple):
        """Takes into account all the game rules of placing a fence, and then returns True or False based on that."""
        (y_coord, x_coord) = coordinate_tuple
        if not self.same_player_turn(player_number):
            return False
        if not self.lock_borders(coordinate_tuple):
            return False
        if not self.place_fence_player1(player_number, direction, x_coord, y_coord):
            return False
        if not self.place_fence_player2(player_number, direction, x_coord, y_coord):
            return False
        if not self.switch_turns():
            return False
        if self._current_state != "UNFINISHED":
            return False
        return True

    def win_logic(self, player_number, x_dest, y_dest):
        """Sets out how pawn1 or pawn2 can win. Sets the current game state to whoever wins."""
        if player_number == 1:
            for num in range(9):
                if y_dest == num and x_dest == 8:
                    self._current_state = "Player_1 won"
                    return True
        elif player_number == 2:
            for num in range(9):
                if y_dest == num and x_dest == 0:
                    self._current_state = "Player_2 won"
                    return True

    def is_winner(self, player_number):
        """Checks if player 1 or player 2 has won the game."""
        if player_number == 1:
            if self._current_state == "Player_1 won":
                return True
        if player_number == 2:
            if self._current_state == "Player_2 won":
                return True
        return False
