print("== task1 ==")


def find_and_print(messages):

    for key, value in messages.items():

        if "18" in value:
            print(key)
        elif "college student" in value:
            print(key)
        elif "legal age" in value:
            print(key)
        elif "vote" in value:
            print(key)


find_and_print({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
})

print("== task2 ==")


def calculate_sum_of_bonus(data):
    employees = data["employees"]
    sum_of_bonus = 0

    for staff in employees:
        salary = staff["salary"]
        performance = staff["performance"]
        role = staff["role"]

        # isinstance() 内建函數，用來建查對象是否為指定的類型
        if isinstance(salary, str) and salary.find("USD") > -1:
            salary = int(salary.replace("USD", ""))*30
        elif isinstance(salary, str) and salary.find(",") > -1:
            salary = int(salary.replace(",", ""))
        elif isinstance(salary, int):
            salary = int(salary)

        if performance == "above average":
            bonus = salary*0.09
        elif performance == "below average":
            bonus = salary*0.05
        elif performance == "average":
            bonus = salary*0.07
        else:
            bonus = 0

        if role == "CEO":
            bonus *= 1.1

        sum_of_bonus += bonus

    print(sum_of_bonus)


calculate_sum_of_bonus({
    "employees": [
        {
            "name": "John",
            "salary": "1000USD",
            "performance": "above average",
            "role": "Engineer"
        },
        {
            "name": "Bob",
            "salary": 60000,
            "performance": "average",
            "role": "CEO"
        },
        {
            "name": "Jenny",
            "salary": "50,000",
            "performance": "below average",
            "role": "Sales"
        }
    ]
})  # call calculate_sum_of_bonus function

print("== task3 ==")


def func(*data):

    for i in data:
        middle_char = i[1]
        middle = 0
        for a in data:
            middle += a[1].count(middle_char)
        if (middle == 1):  # 計算中間值不重複的所以等於1
            print(i)
            return  # 不要讓值再繼續跳脫function
    print("沒有")


func("彭⼤牆", "王明雅", "吳明")  # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有

print("== task4 ==")


def get_number(index):
    result = 0
    for i in range(index):  # range要放參數讓他計算
        if i % 2 == 0:
            result += 4
        else:
            result -= 1
    print(result)


get_number(1)  # print 4
get_number(5)  # print 10
get_number(10)  # print 15
