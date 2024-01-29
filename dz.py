# 1 задание
word = input()
reverse_word = word.split()
reverse_word = reverse_word[1] + " " + reverse_word[0]
print(reverse_word)
# 2 задание
how_many_words = word.count(" ")
print(how_many_words + 1)
# 3 задание
text = "В 2020 году я буду все делать вовремя!"
text = text.replace("2020", "2021")
print(text)
# 4 задание
numbers = input()
numbers = numbers.split()
numbers = [int(i) for i in numbers]
print(numbers)
sum_of_sqrt = 0
for n in numbers:
    sum_of_sqrt += n ** 2

print(sum_of_sqrt)
# 5 задание
grades = input()
grades = grades.split()
print(grades.count("5"), grades.count("4"),
      grades.count("3"), grades.count("2"))
print(grades)

# мы меняем тип данных в нашем списке grades  str в int
grades = [int(i) for i in grades]
avg_grades = sum(grades) / len(grades)
print(avg_grades)
# 6 задание
grade = input()
print(grade)
grade = grade.replace("2", "3")
print(grade)
