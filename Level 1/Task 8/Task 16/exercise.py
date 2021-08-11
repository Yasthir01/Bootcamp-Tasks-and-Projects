# =========================
# Overview
# =========================

####################################################################################
# ========================
# Part 1: Vector and Complex Numbers
# ========================

# In this exercise you will use what you have learned to implement a Vector
# class and a complex number class.

# ========================
# The Vector class
# ========================

# Write definitions for a class called Vector.
# Your definition should include a constructor,  __str__, values for the x and y
# coordinates, and methods for addition and subtraction of vectors, scalar multiplication,
# length, and comparison.

import math

class Vector(object):
    
    def __init__(self, x, y):
        self.x = x  # x coordinate
        self.y = y  # y coodrinate

    def __add__(self, other):
        """Addition of vectors"""
        return Vector(self.x + other.x, self.y, other.y)


    def __sub__(self, other):
        """Subtraction of vectors"""
        return Vector(self.x - other.x, self.y - other.y)


    def __mul__(self, other):
        """Multiplication"""
        return self.x * other.x + self.y * other.y


    def __abs__(self):
        """Length"""
        return math.sqrt(self.x**2 + self.y**2)


    def __eq__(self, other):
        """Comparison"""
        return self.x == other.x and self.y == other.y


    def __str__(self):
        return f"{self.x}, {self.y}"






# =========================
# The derived Complex class
# =========================

# Write definitions for a class called MyComplex that is derived from your
# Vector class.  Your definition should include methods for multiplying two
# complex numbers and computing the complex conjugate as well as an updated
# definition of __str__.

class MyComplex(Vector):
    
    def __init__(self, real=0, imag=0):
        super().__init__(real, imag)

    def __str__(self):
        return f"{self.x} + {self.y}"





####################################################################################
# ========================
# Part 2: Tic-tac-toe
# ========================

# In this task you will be writing a simple game of tic-tac-toe.
# You should expect to find this exercise more challenging than Part 1.
# Please write docstrings for each class and method.
# As you walk through each element, think about how the game's objects are organized.
# Does it seem like the most efficient way to do things to you?
# A common criticism of object-oriented programming is that it can lead to
# excessive abstractions and overcomplication.

# ========================
# The Piece class
# ========================

# Write an abstract Piece class definition.
# Your definition should include:
board = [0, 1, 2, 3, 4 , 6, 7, 8]


class Piece(object):
    pass

# =======================
# The X and O classes
# =======================

# Write definitions of X and O piece classes.
# Your definitions should include:

class X(Piece):
    pass

class O(Piece):
    pass

# =========================
# The TicTacToeBoard class
# =========================

# Write a TicTacToeBoard class definition.
# Your definition should include:

class TicTacToeBoard(object):
    """Create the board"""
    print("--------")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("--------")


    def winner():
        """Determines the winner of the game"""

        if board[0] == 'O' and board[1]  == 'O'  and board[2] == 'O' :
            print("O Wins")
            break
        elif board[3]  == 'O' and board[4] == 'O' and board[5] == 'O' :
            print("O Wins")
            break
        elif board[6] == 'O'  and board[7] == 'O'  and board[8] == 'O' :
            print("O Wins")
            break
        elif board[0] == 'O'  and board[3] == 'O'  and board[6] == 'O' :
            print("O Wins")
            break
        elif board[1] == 'O'  and board[4] == 'O'  and board[7] == 'O' :
            print("O Wins")
            break
        elif board[2] == 'O'  and board[5] == 'O'  and board[8] == 'O' :
            print("O Wins")
            break
        elif board[0] == 'O'  and board[4] == 'O'  and board[8] == 'O' :
            print("O Wins")
            break
        elif board[2] == 'O'  and board[4] == 'O'  and board[6] == 'O' :
            print("O Wins")
            break
        elif board[0] == 'X' and board[1]  == 'X'  and board[2] == 'X' :
            print("X Wins")
            break
        elif board[3]  == 'X' and board[4] == 'X' and board[5] == 'X' :
            print("X Wins")
            break
        elif board[6] == 'X'  and board[7] == 'X'  and board[8] == 'X' :
            print("X Wins")
            break
        elif board[0] == 'X'  and board[3] == 'X'  and board[6] == 'X' :
            print("X Wins")
            break
        elif board[1] == 'X'  and board[4] == 'X'  and board[7] == 'X' :
            print("X Wins")
            break
        elif board[2] == 'X'  and board[5] == 'X'  and board[8] == 'X' :
            print("X Wins")
            break
        elif board[0] == 'X'  and board[4] == 'X'  and board[8] == 'X' :
            print("X Wins")
            break
        elif board[2] == 'X'  and board[4] == 'X'  and board[6] == 'X' :
            print("X Wins")
            break



