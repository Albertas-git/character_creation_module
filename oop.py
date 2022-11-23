class Human:
    def __init__(self, name):
        self.name = name

    # ответ по умолчанию для всех одинаковый, можно 
    # доверить его родительскому классу
    def answer_question(self, question):
        self.question = question
        print('Очень интересный вопрос! Не знаю.')

    def __str__(self):
        return (f'{self.name}')

class Student(Human):
    
    #def __init__(self, name, someone, question):
        #super().__init__(name)
        #self.someone = someone
        #self.question = question


    def ask_question(self, someone, question):
        self.someone = someone
        self.question = question
        print(f'{self.someone}, {self.question}')
          # этот print выводит разделительную пустую строку	
        self.someone.answer_question(self.question)
        print()


class Curator(Human):
    def answer_question(self, question):
        if question == ('мне грустненько, что делать?'):
            print('Держись, всё получится. Хочешь видео с котиками?')
        else:
            super().answer_question(question)

    def __str__(self):
        return (f'{self.name}')

class CodeReviewer(Human):
    def answer_question(self, question):
        if question == ('что не так с моим проектом?'):
            print('О, вопрос про проект, это я люблю.')
        else:
            super().answer_question(question)

    def __str__(self):
        return (f'{self.name}')

class Mentor(Human):
    def answer_question(self, question):
        if question == ('мне грустненько, что делать?'):
            print('Отдохни и возвращайся с вопросами по теории.')
        elif question == ('как устроиться работать питонистом?'):
            print('Сейчас расскажу.')
        else:
            super().answer_question(question)

    def __str__(self):
        return (f'{self.name}')
    
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса

# объявите и реализуйте классы CodeReviewer и Mentor


# следующий код менять не нужно, он работает, мы проверяли
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')






#def __init__(self, name, someone):
     #   super().__init__(name)
     #   self.name = name
      #  self.someonoe = someone
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос; 
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question

