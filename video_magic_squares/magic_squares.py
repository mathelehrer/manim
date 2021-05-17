from abc import ABC
from colour import Color
from numpy.random import random

from manim import *

import numpy as np


class MagicSquare(VGroup, ABC):
    def __init__(self, size=3, **kwargs):
        VGroup.__init__(self, **kwargs)
        self.shifts = []
        self.numbers = []
        self.values = []
        self.squares = []
        self.sums = []
        self.size = size
        self.colors = []
        for row in range(0, self.size):
            for col in range(0, self.size):
                square = Square()
                square.scale(0.5)
                square.move_to((col - int(self.size / 2)) * RIGHT + (row - int(self.size / 2)) * DOWN)
                self.add(square)
                self.squares.append(square)

    def shift(self, *vectors: np.ndarray) -> "Mobject":
        """
        Override methode to shift the numbers of the square as well
        The amount of shifting is saved for numbers that are added later
        Parameters
        ----------
        vectors

        Returns
        -------

        """
        super().shift(*vectors)
        # for n in range(0, len(self.numbers)):
        #     self.numbers[n].shift(*vectors)
        # self.shifts = vectors

    def set_numbers(self, numbers):
        self.values = numbers
        for n in range(0, len(numbers)):
            row = int(n / self.size)
            col = int(n % self.size)
            number = MathTex(numbers[n])
            number.move_to((col - int(self.size / 2)) * RIGHT + (row - int(self.size / 2)) * DOWN)
            if len(self.shifts) > 0:
                number.shift(*self.shifts)
            self.numbers.append(number)

    def add_colors(self, colors):
        self.colors = colors
        for n in range(0, len(colors)):
            self.numbers[n].set_color(colors[n])

    def add_numbers(self, numbers):
        self.values = numbers
        if len(self.numbers) > 0:
            self.remove(*self.numbers)
            self.numbers.clear()
        for n in range(0, len(numbers)):
            row = int(n / self.size)
            col = int(n % self.size)
            number = MathTex(numbers[n])
            number.move_to((col - int(self.size / 2)) * RIGHT + (row - int(self.size / 2)) * DOWN)
            if len(self.shifts) > 0:
                number.shift(*self.shifts)
            self.numbers.append(number)
            self.add(number)

    def append_numbers(self, *numbers, run_time=1):
        """
        append numbers to existing numbers of the magic square
        Parameters
        ----------
        numbers
        run_time

        Returns
        -------

        """
        m = len(self.numbers)
        self.values.extend([*numbers])
        print(m)

        trafos = []
        count = 0
        for n in numbers:
            number = MathTex(n)
            row = int((count + m) / self.size)
            col = int((count + m) % self.size)
            number.move_to((col - int(self.size / 2)) * RIGHT + (row - int(self.size / 2)) * DOWN)
            if len(self.shifts) > 0:
                number.shift(*self.shifts)
            self.numbers.append(number)
            trafos.append(Write(number))
            count = count + 1

        return AnimationGroup(*trafos, lag_ratio=run_time / len(numbers))

    def update_number(self, value, index):
        """
        Update the value of a number in the magic square
        Parameters
        ----------
        value
        index

        Returns
        -------

        """
        self.values[index] = value
        number = MathTex(value)
        number.shift(self.numbers[index].get_center())
        if len(self.colors) > index:
            number.set_color(color[index])
        return Transform(self.numbers[index], number)

    def write_numbers(self, run_time=1):
        writing = []
        for n in range(0, len(self.numbers)):
            writing.append(Create(self.numbers[n]))
        return AnimationGroup(*writing, lag_ratio=run_time / self.size / self.size)

    def reduce_numbers_to(self, length):
        """
        reduce to a certain amount of numbers that are shown in the magic square
        Parameters
        ----------
        length amount of numbers that remain in the square

        Returns
        -------

        """
        deletes = []
        for n in range(length, len(self.numbers)):
            deletes.append(self.numbers[n])
        values = []
        numbers = []
        for v in range(0, length):
            values.append(self.values[v])
            numbers.append(self.numbers[v])
        self.values = values
        self.numbers = numbers
        return deletes

    def get_numbers(self):
        return self.numbers

    def get_row(self, row):
        row_group = VGroup()
        for col in range(0, self.size):
            row_group.add(self.squares[row * self.size + col])
        return row_group

    def get_subsquare(self, offx, offy):
        row_group = VGroup()
        for col in range(0, 2):
            for row in range(0, 2):
                row_group.add(self.squares[(row + offy) * self.size + (col + offx)])
        return row_group

    def get_row_sum(self, row):
        s = 0
        for col in range(0, self.size):
            s = s + self.values[row * self.size + col]
        s_object = Tex(s)
        if self.size % 2 == 0:
            shift = 1
        else:
            shift = 0
        s_object.move_to((self.size - int(self.size / 2 - shift)) * RIGHT + (row - int(self.size / 2)) * DOWN)
        return s_object

    def get_col(self, col):
        col_group = VGroup()
        for row in range(0, self.size):
            col_group.add(self.squares[row * self.size + col])
        return col_group

    def get_col_sum(self, col):
        s = 0
        for row in range(0, self.size):
            s = s + self.values[row * self.size + col]
        s_object = Tex(s)
        s_object.move_to((col - int(self.size / 2)) * RIGHT + (self.size - int(self.size / 2)) * DOWN)
        return s_object

    def get_diagonal_sum(self, diagonal=0):
        s = 0
        if diagonal == 0:
            for row in range(0, self.size):
                s = s + self.values[row * self.size + row]
            s_object = Tex(s)
            s_object.move_to((self.size - int(self.size / 2)) * RIGHT + (self.size - int(self.size / 2)) * DOWN)
        else:
            for row in range(0, self.size):
                s = s + self.values[row * self.size + self.size - row - 1]
            s_object = Tex(s)
            s_object.move_to((-1 - int(self.size / 2)) * RIGHT + (self.size - int(self.size / 2)) * DOWN)
        return s_object

    def get_dim(self):
        return self.size

    def apply_permutation(self, permutation):
        transformations = []
        values = [0] * self.size * self.size
        placeholders = [0] * self.size * self.size
        for i in range(0, self.size * self.size):
            values[i] = self.values[i]
        for i in range(0, len(permutation) - 1):
            values[permutation[i + 1] - 1] = self.values[permutation[i] - 1]
            transformations.append(ApplyMethod(self.numbers[permutation[i] - 1].move_to,
                                               self.numbers[permutation[i + 1] - 1].get_center()))
            placeholders[permutation[i + 1] - 1] = self.numbers[permutation[i] - 1]
        # copy numbers back into the array with the correct ordering

        for i in range(0, self.size * self.size):
            if not placeholders[i] == 0:
                self.numbers[i] = placeholders[i]

        self.values = values
        return AnimationGroup(*transformations)

    def swap(self, a, b):
        tmp = self.values[a]
        self.values[a] = self.values[b]
        self.values[b] = tmp

    def get_values(self):
        return self.values

    def update_sums(self):
        self.sums.clear()
        for i in range(0, self.size):
            rs = self.get_row_sum(i)
            self.sums.append(rs)
            cs = self.get_col_sum(i)
            self.sums.append(cs)
        self.sums.append(self.get_diagonal_sum(0))
        self.sums.append(self.get_diagonal_sum(1))

    def show_sums(self, run_time=1):
        self.update_sums()
        return AnimationGroup(*[Write(self.sums[n]) for n in range(0, len(self.sums))],
                              lag_ratio=run_time / (2 * self.size + 2))

    def get_sums(self):
        return self.sums

    def is_magic(self):
        s = 0
        for col in range(0, self.size):
            s = s + self.values[col]
        first_row = s

        # check remaining rows
        for row in range(1, self.size):
            s = 0
            for col in range(0, self.size):
                s = s + self.values[col + row * self.size]
            if s != first_row:
                return False

        # check cols
        for col in range(0, self.size):
            s = 0
            for row in range(0, self.size):
                s = s + self.values[col + row * self.size]
            if s != first_row:
                return False
        # check diagonal
        s = 0
        for row in range(0, self.size):
            s = s + self.values[row + row * self.size]
        if s != first_row:
            return False
        s = 0
        for row in range(0, self.size):
            s = s + self.values[self.size - row - 1 + row * self.size]
        if s != first_row:
            return False
        # all checks passed successfully
        return True


class Intro(Scene):
    def construct(self):
        title = Tex("Magic Squares")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))
        self.wait()

        magic_square = MagicSquare(size=3)
        self.play(GrowFromCenter(magic_square))
        self.wait()

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        magic_square.add_numbers(numbers)
        self.play(magic_square.write_numbers(run_time=3))
        self.wait()

        sums = self.calculate_sums(magic_square)
        self.remove(*sums)

        self.play(magic_square.apply_permutation([1, 8, 7, 6, 9, 2, 3, 4, 1]), run_time=5)
        self.wait()

        sums = self.calculate_sums(magic_square)
        self.wait(10)

    def calculate_sums(self, magic_square):
        sums = []
        # determine row sums
        rect = SurroundingRectangle(magic_square.get_row(0))
        rect.set_color(BLUE)
        self.play(GrowFromEdge(rect, LEFT))
        self.wait()

        row_sum = magic_square.get_row_sum(0)
        row_sum.set_color(BLUE)
        sums.append(row_sum)
        self.play(Create(row_sum))
        self.wait()

        for row in range(1, magic_square.get_dim()):
            rect.generate_target()
            rect.target = SurroundingRectangle(magic_square.get_row(row))
            rect.target.set_color(BLUE)

            self.play(MoveToTarget(rect))
            row_sum = magic_square.get_row_sum(row)
            row_sum.set_color(BLUE)
            sums.append(row_sum)
            self.play(Create(row_sum))
            self.wait()

        self.play(FadeOut(rect))

        # determine col sums
        rect = SurroundingRectangle(magic_square.get_col(0))
        rect.set_color(RED)
        self.play(GrowFromEdge(rect, LEFT))
        self.wait()

        col_sum = magic_square.get_col_sum(0)
        col_sum.set_color(RED)
        sums.append(col_sum)
        self.play(Create(col_sum))
        self.wait()

        for col in range(1, magic_square.get_dim()):
            rect.generate_target()
            rect.target = SurroundingRectangle(magic_square.get_col(col))
            rect.target.set_color(RED)

            self.play(MoveToTarget(rect))
            col_sum = magic_square.get_col_sum(col)
            col_sum.set_color(RED)
            sums.append(col_sum)
            self.play(Create(col_sum))
            self.wait()

        self.play(FadeOut(rect))

        # diagonals

        rect = SurroundingRectangle(magic_square.get_row(0))
        pivot = magic_square.get_row(0)[0].get_center()
        rect.stretch_about_point(1.4, 0, pivot)
        rect.stretch(0.7, 1)
        rect.rotate(-45 * DEGREES, OUT, pivot)
        rect.set_color(GREEN)
        self.play(GrowFromCenter(rect))
        self.wait()

        diag_sum = magic_square.get_diagonal_sum(0)
        diag_sum.set_color(GREEN)
        sums.append(diag_sum)
        self.play(Create(diag_sum))
        self.wait()

        self.play(ApplyMethod(rect.rotate, 90 * DEGREES), run_time=3)
        self.wait()

        diag_sum = magic_square.get_diagonal_sum(1)
        diag_sum.set_color(GREEN)
        sums.append(diag_sum)
        self.play(Create(diag_sum))
        self.wait()

        self.play(FadeOut(rect))
        self.wait()

        return sums


class Plan(Scene):
    def construct(self):
        title = Tex("Outline")
        title.to_edge(UP)
        title.set_color(YELLOW)
        self.play(Write(title))
        self.wait()

        approaches = BulletedList("Random approach", "Systematic approach", "Challenges", "Other strategies")
        approaches[0].set_color(BLUE)
        self.play(Write(approaches[0]))
        self.wait(3)
        approaches[1].set_color(GREEN)
        self.play(Write(approaches[1]))
        self.wait(3)
        approaches[2].set_color(RED)
        self.play(Write(approaches[2]))
        self.wait(3)
        approaches[3].set_color(WHITE)
        self.play(Write(approaches[3]))
        self.wait(3)
        self.wait(10)


class RandomApproach(Scene):
    def construct(self):
        title = Tex("Random approach")
        title.to_edge(UP)
        title.set_color(BLUE)
        self.play(Write(title))
        self.wait()

        items = [Tex("There are 362880 possibilities"),
                 MathTex(r"9\cdot 8 \cdot 7\cdot 6\cdot 5\cdot 4\cdot 3\cdot 2\cdot 1 = 9! = 362880"),
                 Tex("Only eight of the are magic"), Tex("Only a one in 45360 chance to find a magic square")]

        items[0].next_to(title, DOWN)
        items[0].to_edge(LEFT, buff=LARGE_BUFF)
        for i in range(1, len(items)):
            items[i].next_to(items[i - 1], DOWN)
            items[i].align_to(items[i - 1], LEFT)
            self.play(Write(items[i - 1]))
            self.wait()

        last = len(items) - 1
        magic1 = MagicSquare(3)
        magic1.add_numbers([4, 9, 2, 3, 5, 7, 8, 1, 6])
        blue = Color("yellow")
        red = Color("cyan")
        colors = list(blue.range_to(red, 9))
        magic1.add_colors(colors)
        magic1.scale(0.5)

        magic1.next_to(items[last - 1], DOWN)
        magic1.to_edge(LEFT, buff=LARGE_BUFF)

        self.play(Create(magic1))

        squares = [magic1]
        for i in range(0, 3):
            magic = MagicSquare(3)
            magic.add_numbers(squares[0].get_values())
            magic.add_colors(colors)
            magic.scale(0.5)
            magic.next_to(squares[i], RIGHT)
            self.play(TransformFromCopy(squares[0], magic))
            for j in range(0, i + 1):
                self.play(magic.apply_permutation([1, 3, 9, 7, 1]), magic.apply_permutation([2, 6, 8, 4, 2]))
            squares.append(magic)
            self.wait()

        for i in range(0, 4):
            magic = MagicSquare(3)
            magic.add_numbers(squares[0].get_values())
            magic.add_colors(colors)
            magic.scale(0.5)
            magic.next_to(squares[i], DOWN)
            self.play(TransformFromCopy(squares[0], magic))
            for j in range(0, i):
                self.play(magic.apply_permutation([1, 3, 9, 7, 1]), magic.apply_permutation([2, 6, 8, 4, 2]))
            self.play(magic.apply_permutation([1, 7, 1]), magic.apply_permutation([2, 8, 2]),
                      magic.apply_permutation([3, 9, 3]))
            squares.append(magic)
            self.wait()

        last = len(items) - 1
        items[last].to_edge(DOWN)
        self.play(Write(items[last]))
        self.wait()

        self.wait(10)


class RandomApproach2(Scene):
    def construct(self):
        title = Tex("Random approach 3x3")
        title.to_edge(UP)
        title.set_color(BLUE)
        self.play(Write(title))
        self.wait()

        random_permutations = []
        for i in range(0, 30):
            a = int(np.random.random() * 9) + 1
            b = int(np.random.random() * 9) + 1
            random_permutations.append([a, b, a])

        print(random_permutations)
        # solved magic square
        values = [4, 9, 2, 3, 5, 7, 8, 1, 6]
        print(values)
        blue = Color("yellow")
        red = Color("cyan")
        colors = list(blue.range_to(red, 9))

        # apply permutations backward to shuffle the values
        for p in reversed(random_permutations):
            v = [0] * 9
            c = [0] * 9
            for i in range(0, 9):
                v[i] = values[i]
                c[i] = colors[i]
            for i in range(0, len(p) - 1):
                v[p[i + 1] - 1] = values[p[i] - 1]
                c[p[i + 1] - 1] = colors[p[i] - 1]
            values = v
            colors = c
            print(values)

        magic = MagicSquare(3)
        magic.set_numbers(values)
        magic.add_colors(colors)

        self.play(Create(magic))
        self.play(magic.write_numbers())
        self.wait()
        self.play(magic.show_sums())

        counter = 0
        for p in random_permutations:
            counter = counter + 1
            self.play(magic.apply_permutation(p), run_time=2 / counter)
            print(magic.get_values())
            self.remove(*magic.get_sums())
            magic.update_sums()
            self.add(*magic.get_sums())

        self.wait(10)


class RandomApproach3(Scene):
    def construct(self):
        title = Tex("Random approach 4x4")
        title.to_edge(UP)
        title.set_color(BLUE)
        self.play(Write(title))
        self.wait()

        items = [Tex("There are 20 922 789 888 000 possibilities"),
                 Tex("Only 7040 of the are magic"),
                 Tex("Only a one in 2 971 987 200 chance to find a magic square")]

        last = len(items) - 1
        magic1 = MagicSquare(4)
        magic1.add_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
        blue = Color("yellow")
        red = Color("cyan")
        colors = list(blue.range_to(red, 16))
        magic1.add_colors(colors)

        items[0].to_edge(LEFT, buff=LARGE_BUFF)
        items[0].shift(2 * DOWN)

        self.play(Create(magic1))

        for i in range(1, len(items)):
            items[i].next_to(items[i - 1], DOWN)
            items[i].align_to(items[i - 1], LEFT)
            self.play(Write(items[i - 1]))
            self.wait()

        self.play(Write(items[last]))
        self.wait(10)


class SystematicApproach(Scene):
    def construct(self):
        title = Tex("Systematic approach")
        title.to_edge(UP)
        title.set_color(GREEN)
        self.play(Write(title))
        self.wait()

        magic = MagicSquare(4)
        magic.set_numbers([1, 2, 3, 4])
        magic.shift(0.5 * RIGHT)
        self.play(Create(magic))
        self.wait()

        self.play(magic.write_numbers(run_time=3))
        self.wait()

        rect = SurroundingRectangle(magic.get_row(0))
        rect.set_color(BLUE)
        self.play(GrowFromEdge(rect, LEFT))
        self.wait()

        row_sum = magic.get_row_sum(0)
        row_sum.set_color(BLUE)
        self.play(Create(row_sum))
        self.wait()

        deletes = []

        for i in range(5, 17):
            self.play(magic.update_number(i, 3), run_time=5 / i)
            self.remove(row_sum)
            row_sum = magic.get_row_sum(0)
            row_sum.set_color(BLUE)
            self.add(row_sum)

        for j in range(3, 15):  # change to 15 again
            for i in range(3, 17):
                replacements = []
                if i == 3:
                    replacements.append(magic.update_number(j + 1, 2))
                    replacements.append(magic.update_number(i, 3))
                    self.play(*replacements, run_time=8 / (i + j))
                elif i != j + 1:
                    replacements.append(magic.update_number(i, 3))
                    self.play(*replacements, run_time=8 / (i + j))
                self.remove(row_sum)
                row_sum = magic.get_row_sum(0)
                row_sum.set_color(BLUE)
                self.add(row_sum)
        deletes.append(row_sum)
        self.wait()

        rect2 = SurroundingRectangle(magic.get_row(1))
        rect2.set_color(GREEN)
        rect.generate_target()
        rect.target = rect2
        self.play(magic.append_numbers(3, 4, 5, 6, run_time=3))
        self.play(MoveToTarget(rect))
        row_sum = magic.get_row_sum(1)
        row_sum.set_color(GREEN)
        self.play(Write(row_sum))

        for i in range(7, 15):
            self.play(magic.update_number(i, 7), run_time=3 / i)
            self.remove(row_sum)
            row_sum = magic.get_row_sum(1)
            row_sum.set_color(GREEN)
            self.add(row_sum)

        for j in range(5, 13):  # change to 13 again
            for i in range(5, 15):
                replacements = []
                if i == 5:
                    replacements.append(magic.update_number(j + 1, 6))
                    replacements.append(magic.update_number(i, 7))
                    self.play(*replacements, run_time=4 / (i + j))
                elif i != j + 1:
                    replacements.append(magic.update_number(i, 7))
                    self.play(*replacements, run_time=4 / (i + j))
                self.remove(row_sum)
                row_sum = magic.get_row_sum(1)
                row_sum.set_color(GREEN)
                self.add(row_sum)
        deletes.append(row_sum)
        self.wait()

        rect2 = SurroundingRectangle(magic.get_row(2))
        rect2.set_color(RED)
        rect.generate_target()
        rect.target = rect2
        self.play(magic.append_numbers(5, 6, 7, 8, run_time=3))
        self.play(MoveToTarget(rect))
        row_sum = magic.get_row_sum(2)
        row_sum.set_color(RED)
        self.play(Write(row_sum))

        for i in range(9, 13):
            self.play(magic.update_number(i, 11), run_time=2 / i)
            self.remove(row_sum)
            row_sum = magic.get_row_sum(2)
            row_sum.set_color(RED)
            self.add(row_sum)

        for j in range(7, 11):  # change to 11 again
            for i in range(7, 13):
                replacements = []
                if i == 7:
                    replacements.append(magic.update_number(j + 1, 10))
                    replacements.append(magic.update_number(i, 11))
                    self.play(*replacements, run_time=2 / (i + j))
                elif i != j + 1:
                    replacements.append(magic.update_number(i, 11))
                    self.play(*replacements, run_time=2 / (i + j))
                self.remove(row_sum)
                row_sum = magic.get_row_sum(2)
                row_sum.set_color(RED)
                self.add(row_sum)
        deletes.append(row_sum)
        self.wait()

        rect.generate_target()
        rect2 = SurroundingRectangle(magic.get_row(0))
        pivot = magic.get_row(0)[3].get_center()
        rect2.stretch_about_point(1.4, 0, pivot)
        rect2.stretch(0.7, 1)
        rect2.rotate(45 * DEGREES, OUT, pivot)
        rect2.set_color(YELLOW)
        rect.target = rect2
        self.play(magic.append_numbers(7))
        self.play(MoveToTarget(rect), run_time=3)
        self.wait()

        dia_sum = magic.get_diagonal_sum(1)
        dia_sum.set_color(YELLOW)
        self.play(Write(dia_sum))
        self.wait()
        deletes.append(dia_sum)

        rect2 = SurroundingRectangle(magic.get_row(0))
        rect2.set_color(BLUE)
        rect.generate_target()
        rect.target = rect2
        self.play(MoveToTarget(rect))
        self.remove(*deletes)
        self.remove(*magic.reduce_numbers_to(4))
        self.wait()

        self.play(magic.update_number(16, 2), magic.update_number(15, 3))
        row_sum = magic.get_row_sum(0)
        row_sum.set_color(BLUE)
        self.play(Write(row_sum), run_time=0.1)
        self.wait()
        self.play(magic.append_numbers(3, 4, 5, 6, run_time=1))
        self.wait()

        func1 = Tex("shrink")
        func2 = Tex("increment")
        func3 = Tex("expand")

        func1.next_to(title, DOWN, buff=LARGE_BUFF)
        func1.to_edge(LEFT)
        func1.set_color(YELLOW)

        func2.next_to(title, DOWN, buff=LARGE_BUFF)
        func2.set_color(YELLOW)

        func3.next_to(func2, RIGHT, buff=2 * LARGE_BUFF)
        func3.set_color(YELLOW)

        numbers = magic.get_numbers()
        targets = []
        for n in range(0, len(numbers)):
            numbers[n].generate_target()
            target = numbers[n].copy()
            targets.append(target)
            if n == 0:
                target.next_to(func1, DOWN)
                target.to_edge(LEFT)
            else:
                target.next_to(targets[n - 1], RIGHT)
            numbers[n].target = target
            self.play(MoveToTarget(numbers[n]))

        self.remove(magic, rect, row_sum)
        self.play(Write(func1))
        for row in range(0, 4):
            next_numbers = []
            for col in range(0, 7 - row):
                next_number = numbers[col].copy()
                next_number.next_to(numbers[col], DOWN)
                next_numbers.append(next_number)
                self.play(Write(next_number), run_time=0.1)
            self.wait(0.5)
            numbers = next_numbers

        self.play(Write(func2))
        next_numbers = []
        for n in range(0, len(numbers)):
            numbers[n].generate_target()
            if n == 0:
                numbers[n].target.next_to(func2, DOWN)
                numbers[n].target.align_to(func2, LEFT)
            else:
                numbers[n].target.next_to(numbers[n - 1].target, RIGHT)

            next_number = numbers[n].copy()
            next_numbers.append(next_number)
            self.play(MoveToTarget(next_number), run_time=0.1)

        new_numbers = [1, 3, 2, 4, 1, 3, 2, 5, 1, 3, 2, 6, 1, 3, 2, 7]
        numbers = next_numbers
        for row in range(0, 4):
            next_numbers = []
            for col in range(0, 4):
                next_number = Tex(new_numbers[row * 4 + col])
                next_number.next_to(numbers[col], DOWN)
                if row == 0 and col > 0:
                    next_number.set_color(YELLOW)
                elif col > 2:
                    next_number.set_color(YELLOW)
                next_numbers.append(next_number)
                self.play(Write(next_number), run_time=0.1)
            numbers = next_numbers
            self.wait(0.5)

        self.play(Write(func3))
        next_numbers = []
        for n in range(0, len(numbers)):
            numbers[n].generate_target()
            if n == 0:
                numbers[n].target.next_to(func3, DOWN)
                numbers[n].target.align_to(func3, LEFT)
            else:
                numbers[n].target.next_to(numbers[n - 1].target, RIGHT)
            numbers[n].target.set_color(WHITE)
            next_number = numbers[n].copy()
            next_numbers.append(next_number)
            self.play(MoveToTarget(next_number), run_time=0.1)

        new_numbers = [4, 5, 6, 8]
        numbers = next_numbers
        for row in range(0, 4):
            next_numbers = []
            max = 4 + row + 1
            for col in range(0, max):
                if col < max - 1:
                    next_number = numbers[col].copy()
                    next_number.set_color(WHITE)
                    next_number.next_to(numbers[col], DOWN)
                else:
                    next_number = Tex(new_numbers[row])
                    next_number.set_color(YELLOW)
                    next_number.next_to(next_numbers[len(next_numbers) - 1], RIGHT)
                next_numbers.append(next_number)
                self.play(Write(next_number), run_time=0.1)
            numbers = next_numbers
            self.wait(0.5)

        self.wait(10)


class Challenges(Scene):
    def construct(self):
        title = Tex("Challenges")
        title.to_edge(UP)
        title.set_color(RED)
        self.play(Write(title))
        self.wait()

        approaches = BulletedList("Next solutions", "Perfect magic squares")
        approaches.next_to(title, DOWN)
        approaches[0].set_color(BLUE)
        approaches[1].shift(2.5 * DOWN)
        self.play(Write(approaches[0]))
        self.wait(3)

        magic_square = MagicSquare(size=4)
        magic_square.add_numbers([1, 2, 15, 16, 13, 14, 3, 4, 12, 7, 10, 5, 8, 11, 6, 9])
        magic_square.scale(0.5)
        magic_square.shift(3 * LEFT + 0.5 * UP)
        self.play(Create(magic_square))
        self.wait()

        magic_square = MagicSquare(size=4)
        magic_square.add_numbers([1, 2, 16, 15, 13, 14, 4, 3, 12, 7, 9, 6, 8, 11, 5, 10])
        magic_square.scale(0.5)
        magic_square.shift(0.5 * UP)
        self.play(Create(magic_square))
        self.wait()

        magic_square = MagicSquare(size=4)
        magic_square.add_numbers([1, 3, 14, 16, 10, 13, 4, 7, 15, 6, 11, 2, 8, 12, 5, 9])
        magic_square.scale(0.5)
        magic_square.shift(3 * RIGHT + 0.5 * UP)
        self.play(Create(magic_square))
        self.wait()

        approaches[1].set_color(GREEN)
        self.play(Write(approaches[1]))
        self.wait(3)

        magic_square = MagicSquare(size=4)
        magic_square.add_numbers([6, 3, 16, 9, 15, 10, 5, 4, 1, 8, 11, 14, 12, 13, 2, 7])
        magic_square.scale(0.7)
        magic_square.shift(3 * DOWN)
        self.play(Write(magic_square))
        self.wait()

        rect = SurroundingRectangle(magic_square.get_subsquare(0, 0))
        rect.set_color(BLUE)
        self.play(GrowFromCenter(rect))
        self.wait()

        rect.generate_target()
        rect.target = SurroundingRectangle(magic_square.get_subsquare(0, 1))
        rect.target.set_color(BLUE)
        self.play(MoveToTarget(rect))
        self.wait()

        rect.generate_target()
        rect.target = SurroundingRectangle(magic_square.get_subsquare(0, 2))
        rect.target.set_color(BLUE)
        self.play(MoveToTarget(rect))
        self.wait()

        rect.generate_target()
        rect.target = SurroundingRectangle(magic_square.get_subsquare(1, 2))
        rect.target.set_color(BLUE)
        self.play(MoveToTarget(rect))
        self.wait()

        rect.generate_target()
        rect.target = SurroundingRectangle(magic_square.get_subsquare(1, 1))
        rect.target.set_color(BLUE)
        self.play(MoveToTarget(rect))
        self.wait()

        rect.generate_target()
        rect.target = SurroundingRectangle(magic_square.get_subsquare(1, 0))
        rect.target.set_color(BLUE)
        self.play(MoveToTarget(rect))
        self.wait()

        rect.generate_target()
        rect.target = SurroundingRectangle(magic_square.get_subsquare(2, 0))
        rect.target.set_color(BLUE)
        self.play(MoveToTarget(rect))
        self.wait()

        rect.generate_target()
        rect.target = SurroundingRectangle(magic_square.get_subsquare(2, 1))
        rect.target.set_color(BLUE)
        self.play(MoveToTarget(rect))
        self.wait()

        rect.generate_target()
        rect.target = SurroundingRectangle(magic_square.get_subsquare(2, 2))
        rect.target.set_color(BLUE)
        self.play(MoveToTarget(rect))
        self.wait()

        self.wait(10)


def mapping(x, y, length):
    off_y = -0.05
    off_x = 3.445

    delta_x = (14 - 2 * off_x) / length / 2
    delta_y = (7 - 2 * off_y) / length / 2

    return [x * delta_x, y * delta_y]


class History(Scene):
    def construct(self):
        title = Tex("Other strategies")
        title.to_edge(UP)
        title.set_color(WHITE)
        self.play(Write(title))
        self.wait()

        image = ImageMobject("history")
        image.scale(0.25)
        image.shift(0.5 * DOWN)

        self.add(image)
        self.wait(3)

        pixels = image.get_pixel_array()

        sub_pixels = []
        for p in range(0, len(pixels)):
            sub_pixels.append(pixels[p][336:2276])  # horizontal range
        sub_image = ImageMobject(sub_pixels[1124:3060])  # vertical range

        sub_image.scale(0.25)

        self.play(FadeOut(image), FadeIn(sub_image), FadeOut(title))

        self.wait(3)

        size = 17

        initial_coordinates = []
        count = 1
        initial_x = 0

        for s in range(size - 1, -size, -2):
            for i in range(0, size):
                initial_coordinates.append([count, initial_x + i, s - initial_x - i])
                count = count + 1
            initial_x = initial_x - 1

        magic_square = []

        # grid
        grid = []
        for x in range(-size, size + 1):
            line = Line(mapping(x - 0.5, -size - 0.5, size)[1] * UP,
                        mapping(x - 0.5, size - 0.5, size)[1] * UP)
            line.shift(mapping(x - 0.5, size, size)[0] * RIGHT)
            line.set_stroke(width=0.5, opacity=0.5)
            grid.append(line)
            self.play(Create(line), run_time=0.01)

        for y in range(-size, size + 1):
            line = Line(mapping(-size - 0.5, y - 0.5, size)[0] * RIGHT,
                        mapping(size - 0.5, y - 0.5, size)[0] * RIGHT)
            line.shift(mapping(size, y - 0.5, size)[1] * UP)
            line.set_stroke(width=0.5, opacity=0.5)
            grid.append(line)
            self.play(Create(line), run_time=0.01)

        numbers = []
        test = size * size
        for i in range(0, test):
            x = initial_coordinates[i][1]
            y = initial_coordinates[i][2]
            v = initial_coordinates[i][0]
            number = MathTex(initial_coordinates[i][0])

            if v != 9 and v != 25 and v != 26 and v != 27 and v != 111:

                pos = mapping(x, y, 17)

                if np.abs(x) > size / 2 or np.abs(y) > size / 2:
                    number.set_color(WHITE)
                else:
                    number.set_color(BLACK)
                    magic_square.append(number)

                number.set_stroke(width=1.5)
                if v < 100:
                    number.scale(0.33)
                else:
                    number.scale(0.22)
                number.shift(pos[0] * RIGHT + pos[1] * UP)

                self.play(Write(number), run_time=0.01)

            numbers.append(number)

        self.wait(3)

        for i in range(0, test):
            x = initial_coordinates[i][1]
            y = initial_coordinates[i][2]
            v = initial_coordinates[i][0]

            number = numbers[i]
            if y > size / 2:
                self.play(ApplyMethod(number.set_color, RED), run_time=0.1)
                self.play(ApplyMethod(number.shift, mapping(size, size, size)[1] * DOWN), run_time=0.5)
                if v <= 34:
                    self.play(FadeOut(number))
                else:
                    magic_square.append(number)
            if x > size / 2:
                self.play(ApplyMethod(number.set_color, GREEN), run_time=0.1)
                self.play(ApplyMethod(number.shift, mapping(size, size, size)[0] * LEFT), run_time=0.25)
                if v <= 34:
                    self.play(FadeOut(number))
                else:
                    magic_square.append(number)
            if y < -size / 2:
                self.play(ApplyMethod(number.set_color, BLUE), run_time=0.1)
                self.play(ApplyMethod(number.shift, mapping(size, size, size)[1] * UP), run_time=0.1)
                magic_square.append(number)
            if x < -size / 2:
                self.play(ApplyMethod(number.set_color, PURPLE), run_time=0.1)
                self.play(ApplyMethod(number.shift, mapping(size, size, size)[0] * RIGHT), run_time=0.05)
                magic_square.append(number)

        self.wait(3)

        magic_square_group = VGroup(*magic_square)
        grid_group = VGroup(*grid)
        self.play(FadeOut(grid_group), ApplyMethod(magic_square_group.scale, 2), ApplyMethod(sub_image.scale, 2))

        self.wait(10)


class Counting(Scene):
    def construct(self):
        approaches = BulletedList("3x3 square: one magic configuration","4x4 square: 880 magic configurations","5x5 square: 275 305 224 magic configurations","6x6 square: ?")
        for i in range(0,4):
            self.play(Write(approaches[i]))
            self.wait(3)

