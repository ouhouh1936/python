from db import Person

class Program :
    def view_people(people):
            for p in people:
                print(f"NAME  : {p.name}")
                print(f"AGE   : {p.age}")
                print(f"GENDER: {p.gender}")
                print("------------------------------------------------")
    def create_people(people):

        prev_length = len(people)
        new_person = Person()
        name = input("이름을 입력하세요. >>")
        age = int(input("나이를 입력하세요. >>"))
        gender = input("성별을 입력하세요. >>")

        new_person.data_setter(name, age, gender)
        people.append(new_person)

        next_length = len(people)

        if prev_length < next_length:
            return True
        else:
            return False

    def delete_people(people):
        prev_length = len(people)
        print("=============================")
        for p in enumerate(people):
            print(f"{(p[0] + 1)} - {p[1].name}")
        print("=============================")

        answer = int(input("삭제할 사람의 번호를 적어주세요. >>"))

        people.pop(answer - 1)

        next_length = len(people)

        if prev_length > next_length:
            return True
        else:
            return False