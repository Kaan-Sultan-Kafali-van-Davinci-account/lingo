import lingowords, random, sys, time
from termcolor import colored as c
from collections import Counter

langs = {
    "en": lingowords.english,
    "nl": lingowords.nederlands,
    "tr": lingowords.türkçe,
    "ar": lingowords.عربي,
    "jp": lingowords.日本語,
    "sy": lingowords.synaptsk,
}
l = {
    "en":
        {"A full game or a quick round? (1/2) ": "A full game or a quick round? (1/2) ",
        "Set Team Red name (leave blank for default): ": "Set Team Red name (leave blank for default): ",
        "Set Team Blue name (leave blank for default): ": "Set Team Blue name (leave blank for default): ",
        "Guess a word of 5 letters: ": "Guess a word of 5 letters: ",
        "The word has to be 5 letters.": "The word has to be 5 letters.",
        "This word doesn't exist.": "This word doesn't exist.",
        "Well done!": "Well done!",
        "Answer:": "Answer:",
        "Team ": "Team ",
        "'s turn:" : "'s turn:",
        " Wins!": " Wins!",
        ", Click ENTER to draw two balls ->": ", Click ENTER to draw two balls ->",
        "You drew a ": "You drew a ",
        "green ball": "green ball",
        "red ball": "red ball",
        "letters are correct.": "letters are correct.",
        "Green balls: ": "Green balls: ",
        "Red balls: ": "Red balls: ",
        "Press ENTER to continue -> ": "Press ENTER to continue -> ",},
    "nl":
        {"A full game or a quick round? (1/2) ": "Een vol spel of één snelle potje lingo? (1/2) ",
        "Set Team Red name (leave blank for default): ": "Stel Team Red naam in (laag leeg om zo te houden): ",
        "Set Team Blue name (leave blank for default): ": "Stel Team Blue naam in (laag leeg om zo te houden): ",
        "Guess a word of 5 letters: ": "Raad een woord van 5 letters: ",
        "The word has to be 5 letters.": "Het woord moet 5 letters lang zijn.",
        "This word doesn't exist.": "Dit woord bestaat niet.",
        "Well done!": "Goed geraden!",
        "Answer:": "Antwoord:",
        "Team ": "Team ",
        "'s turn:" : "'s beurt:",
        " Wins!": " Wint!",
        ", Click ENTER to draw two balls ->": ", Klik ENTER om twee ballen te trekken ->",
        "You drew a ": "Je trok een ",
        "green ball": "groene ball",
        "red ball": "rode ball",
        "letters are correct.": "letters zijn correct.",
        "Green balls: ": "Groene ballen: ",
        "Red balls: ": "Rode ballen: ",
        "Press ENTER to continue -> ": "Druk ENTER om door te gaan -> ",},
    "tr":
        {"A full game or a quick round? (1/2) ": "Tam oyun mu yoksa hızlı bir tur mu? (1/2) ",
        "Set Team Red name (leave blank for default): ": "Red Takımının ismi ayarla (varsayılanı boş bırak): ",
        "Set Team Blue name (leave blank for default): ": "Mavi Takımın ismi ayarla (varsayılanı boş bırak): ",
        "Guess a word of 5 letters: ": "5 harfli bir kelime tahmin et: ",
        "The word has to be 5 letters.": "Kelime 5 harfli olmalıdır.",
        "This word doesn't exist.": "Böyle bir kelime yok.",
        "Well done!": "Tebrikler!",
        "Answer:": "Cevap:",
        "Team ": "Takım ",
        "'s turn:" : "'nın sıra:",
        " Wins!": " Kazandı!",
        ", Click ENTER to draw two balls ->": ", İki top çekmek için ENTER tuşuna bas ->",
        "You drew a ": "Çektiğin top... ",
        "green ball": "Yeşil top",
        "red ball": "Kırmızı top",
        "letters are correct.": "harfler doğru.",
        "Green balls: ": "Yeşil toplar: ",
        "Red balls: ": "Kırmızı toplar: ",
        "Press ENTER to continue -> ": "Devam etmek için ENTER tuşuna bas -> ",},
    "ar":
        {"A full game or a quick round? (1/2) ": "هل تريد لعبة كاملة أم جولة سريعة؟ (1/2) ",
        "Set Team Red name (leave blank for default): ": "قم بتعيين اسم الفريق الأحمر (اتركه فارغًا للقيمة الافتراضية): ",
        "Set Team Blue name (leave blank for default): ": "قم بتعيين اسم الفريق الأزرق (اتركه فارغًا للقيمة الافتراضية): ",
        "Guess a word of 5 letters: ": "تخمين كلمة من 5 أحرف: ",
        "The word has to be 5 letters.": "يجب أن تكون الك",
        "This word doesn't exist.": "هذه الكلمة غير موج",
        "Well done!": "أحسنت!",
        "Answer:": "الجواب:",
        "Team ": "فريق ",
        "'s turn:" : "دوره: ",
        " Wins!": " فاز!",
        ", Click ENTER to draw two balls ->": ", انقر على ENTER لسحب كرتين ->",
        "You drew a ": "لقد رسمت ",
        "green ball": "كرة خضراء",
        "red ball": "كرة حمراء",
        "letters are correct.": "الحروف صحيحة.",
        "Green balls: ": "كرات خضراء: ",
        "Red balls: ": "كرات حمراء: ",
        "Press ENTER to continue -> ": "اضغط على ENTER للمتابعة -> ",},
    "jp":
        {"A full game or a quick round? (1/2) ": "フルゲームとかクイックラウンド？ (1/2) ",
        "Set Team Red name (leave blank for default): ": "チームRed名を設定する（デフォルトの場合は空白のままにしてください）： ",
        "Set Team Blue name (leave blank for default): ": "チームBlue名を設定する（デフォルトの場合は空白のままにしてください）： ",
        "Guess a word of 5 letters: ": "4かなの単語を当てて： ",
        "The word has to be 5 letters.": "単語は4かなでなければなりません。",
        "This word doesn't exist.": "この単語はいない。",
        "Well done!": "正解！",
        "Answer:": "正解は：",
        "Team ": "チーム ",
        "'s turn:" : "の番:",
        " Wins!": "の勝ち！",
        ", Click ENTER to draw two balls ->": ", ENTERをクリックして2つのボールを引く ->",
        "You drew a ": "あなたは引いたボールは… ",
        "green ball": "緑のボール",
        "red ball": "赤いボール",
        "letters are correct.": "文字が正しい。",
        "Green balls: ": "緑のボール: ",
        "Red balls: ": "赤いボール: ",
        "Press ENTER to continue -> ": "続行するにはENTERを押し -> ",},
    "sy":
        {"A full game or a quick round? (1/2) ": "Pleinling spële urd flert spële? (1/2) ",
        "Set Team Red name (leave blank for default): ": "İnset Team Red näm (trovk empt vor defalut): ",
        "Set Team Blue name (leave blank for default): ": "İnset Team Blue näm (trovk empt vor defalut): ",
        "Guess a word of 5 letters: ": "Devir e word ela 5 letere: ",
        "The word has to be 5 letters.": "De word mœt er 5 letere.",
        "This word doesn't exist.": "Dit word ikke beistäne.",
        "Well done!": "Well done!",
        "Answer:": "Answer:",
        "Team ": "Tïm ",
        "'s turn:" : " se skas:",
        " Wins!": " win！",
        ", Click ENTER to draw two balls ->": ", Naker ENTER mar trek dub curate ->",
        "You drew a ": "Du trek e ",
        "green ball": "gren curat",
        "red ball": "röd curat",
        "letters are correct.": "letere er corect.",
        "Green balls: ": "Gren curate: ",
        "Red balls: ": "Röd curate: ",
        "Press ENTER to continue -> ": "Naker ENTER mar reväme -> ",},
}
lang = ""
while not lang in langs:
    lang = input("Select language: (nl/tr/en/ar/jp/sy) ")



class Main:
    def __init__(self):
        self.word = langs[lang][random.randrange(0, len(langs[lang]))]
        self.correct_guess_letters = ["", "", "", "", ""]
        self.previous_guesses = [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]]
        self.colors = [["white", "white", "white", "white", "white"], ["white", "white", "white", "white", "white"], ["white", "white", "white", "white", "white"], ["white", "white", "white", "white", "white"], ["white", "white", "white", "white", "white"]]
        self.correct_guess_letters_jp = ["", "", "", ""]
        self.previous_guesses_jp = [[" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "]]
        self.colors_jp = [["white", "white", "white", "white"], ["white", "white", "white", "white"], ["white", "white", "white", "white"], ["white", "white", "white", "white"], ["white", "white", "white", "white"]]
        self.attempt = 0
        self.word_counts = Counter(self.word)
        self.guess = ""
        self.team_red = Team("Red")
        self.team_blue = Team("Blue")
        self.turn = self.team_red
        self.winner = None
        self.game_on = True

    def game(self):
        choice = "0"
        while choice != "1" and choice != "2":
            choice = input(l[lang]["A full game or a quick round? (1/2) "])
        if choice == "1":
            naam = input(l[lang]["Set Team Red name (leave blank for default): "])
            if naam: self.team_red.name = naam
            naam = input(l[lang]["Set Team Blue name (leave blank for default): "])
            if naam: self.team_blue.name = naam

        while self.game_on:
            self.round(quick_round=choice == "2")
            if choice == "2": break
            self.ballenbak()
            self.round_end()

            if self.team_red.greens >= 3 or self.team_blue.reds >= 3 or self.team_red.check_cart_win() or self.team_red.rounds_won_in_a_row >= 10 or self.team_blue.rounds_failed_in_a_row >= 3:
                self.winner = self.team_red
                self.game_on = False
            if self.team_blue.greens >= 3 or self.team_red.reds >= 3 or self.team_blue.check_cart_win() or self.team_blue.rounds_won_in_a_row >= 10 or self.team_red.rounds_failed_in_a_row >= 3:
                self.winner = self.team_blue
                self.game_on = False
        
        time.sleep(1)
        if choice == "1": print(l[lang]["Team "] + self.winner.__repr__() + l[lang][" Wins!"])

    def round(self, quick_round=False):
        while True:
            if not quick_round: print(l[lang]["Team "] + self.turn.__repr__() + l[lang]["'s turn:"])
            self.guess = input(l[lang]["Guess a word of 5 letters: "]).lower()
            if self.guess == "end":
                print("Game end.")
                sys.exit()
            elif len(self.guess) != 5 - int(lang == "jp"):
                print(l[lang]["The word has to be 5 letters."])
            elif not self.guess in langs[lang]:
                print(l[lang]["This word doesn't exist."])
            elif self.guess == self.word:
                print(l[lang]["Well done!"])
                self.check_words(False)
                break
            else:
                self.check_words()
                if self.turn == self.team_blue: self.turn = self.team_red
                elif self.turn == self.team_red: self.turn = self.team_blue

            if self.attempt >= 5 and self.guess != self.word: print("Game Over"); print(l[lang]["Answer:"], self.word.upper()); break

    def ballenbak(self):
        if self.guess == self.word:
            if self.turn == self.team_blue:
                self.team_blue.rounds_won_in_a_row += 1
                self.team_red.rounds_won_in_a_row = 0
                self.team_blue.rounds_won_in_a_row = 0
                self.team_red.rounds_failed_in_a_row -= 1
            elif self.turn == self.team_red:
                self.team_red.rounds_won_in_a_row += 1
                self.team_blue.rounds_won_in_a_row = 0
                self.team_red.rounds_won_in_a_row = 0
                self.team_blue.rounds_failed_in_a_row -= 1
            print(l[lang]["Team "] + self.turn.__repr__() + l[lang][" Wins!"])
            input(l[lang]["Team "] + self.turn.__repr__() + l[lang][", Click ENTER to draw two balls ->"])
            print("...")
            time.sleep(1.5)
            for _ in range(2):
                if random.randrange(0, 10) < 8:
                    num = 0
                    while num == 0 or num in self.turn.pulled_numbers:
                        num = random.randrange(1, 17)
                    print("Je trok " + str(num) + "!")
                    self.turn.mark(num)
                    self.turn.pulled_numbers.append(num)
                else:
                    if random.randrange(0, 2) == 1:
                        print(l[lang]["You drew a "] + c(l[lang]["green ball"], "green") + "!")
                        self.turn.greens += 1
                    else:
                        print(l[lang]["You drew a "] + c(l[lang]["red ball"], "red") + "...")
                        self.turn.reds += 1
                time.sleep(0.5)



    def check_words(self, print_total_letters_correct=True):
        if lang != "jp":
            correct = 0
            if lang != "ar":
                word = self.word
                guess = self.guess
            else:
                word = self.word[::-1]
                guess = self.guess[::-1]
            for i in range(5):
                if guess[i] == word[i]:
                    correct += 1
                    self.correct_guess_letters[i] = guess[i]
                    self.colors[self.attempt][i] = "green"
                    self.word_counts[guess[i]] -= 1
                if print_total_letters_correct:
                    if self.attempt < 4:
                        for i in range(5):
                            if self.correct_guess_letters[i] != "":
                                self.previous_guesses[self.attempt + 1][i] = self.correct_guess_letters[i]
                                self.colors[self.attempt + 1][i] = "grey"
            for i in range(5):
                if guess[i] != word[i]:
                    if self.word_counts[guess[i]] > 0:
                        self.colors[self.attempt][i] = "yellow"
                        self.word_counts[guess[i]] -= 1
                    else:
                        self.colors[self.attempt][i] = "red"
                self.previous_guesses[self.attempt][i] = guess[i]
            if print_total_letters_correct: print(correct, l[lang]["letters are correct."])
            self.word_counts = Counter(self.word)

            for index, guess_ in enumerate(self.previous_guesses):
                print(c(guess_[0], self.colors[index][0]) + " | " + c(guess_[1], self.colors[index][1]) + " | " + c(guess_[2], self.colors[index][2]) + " | " + c(guess_[3], self.colors[index][3]) + " | "  + c(guess_[4], self.colors[index][4]))
        
        else:
            correct = 0
            for i in range(4):
                if self.guess[i] == self.word[i]:
                    correct += 1
                    self.correct_guess_letters_jp[i] = self.guess[i]
                    self.colors_jp[self.attempt][i] = "green"
                    self.word_counts[self.guess[i]] -= 1
                    if print_total_letters_correct:
                        if self.attempt < 4:
                            for i in range(4):
                                if self.correct_guess_letters_jp[i] != "":
                                    self.previous_guesses_jp[self.attempt + 1][i] = self.correct_guess_letters_jp[i]
                                    self.colors_jp[self.attempt + 1][i] = "grey"
            for i in range(5):
                if self.guess[i] != self.word[i]:
                    if self.word_counts[self.guess[i]] > 0:
                        self.colors_jp[self.attempt][i] = "yellow"
                        self.word_counts[self.guess[i]] -= 1
                    else:
                        self.colors_jp[self.attempt][i] = "red"
                self.previous_guesses_jp[self.attempt][i] = self.guess[i]
            if print_total_letters_correct: print(correct, l[lang]["letters are correct."])
            self.word_counts = Counter(self.word)

            for index, guess in enumerate(self.previous_guesses_jp):
                print(c(guess[0], self.colors_jp[index][0]) + " | " + c(guess[1], self.colors_jp[index][1]) + " | " + c(guess[2], self.colors_jp[index][2]) + " | " + c(guess[3], self.colors_jp[index][3]))
        
        self.attempt += 1


    def round_end(self):
        self.word = langs[lang][random.randrange(0, len(langs[lang]))]
        self.correct_guess_letters = ["", "", "", "", ""]
        self.previous_guesses = [[" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "], [" ", " ", " ", " ", " "]]
        self.colors = [["white", "white", "white", "white", "white"], ["white", "white", "white", "white", "white"], ["white", "white", "white", "white", "white"], ["white", "white", "white", "white", "white"], ["white", "white", "white", "white", "white"]]
        self.correct_guess_letters_jp = ["", "", "", ""]
        self.previous_guesses_jp = [[" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "]]
        self.colors_jp = [["white", "white", "white", "white"], ["white", "white", "white", "white"], ["white", "white", "white", "white"], ["white", "white", "white", "white"], ["white", "white", "white", "white"]]
        self.attempt = 0
        self.word_counts = Counter(self.word)
        self.guess = ""

        time.sleep(0.5)
        print("\n" + l[lang]["Team "] + self.team_red.__repr__() + ":")
        for row in self.team_red.card:
            print(c("O", {False: "white", True: "green"}[row[0]]), c("O", {False: "white", True: "green"}[row[1]]), c("O", {False: "white", True: "green"}[row[2]]), c("O", {False: "white", True: "green"}[row[3]]))
        print(c("Green balls: " + str(self.team_red.greens), {False: "white", True: "green"}[self.team_red.greens >= 3]))
        print(c("Red balls: " + str(self.team_red.reds), {False: "white", True: "red"}[self.team_red.reds >= 3]))
        print("\n" + l[lang]["Team "] + self.team_blue.__repr__() + ":")
        for row in self.team_blue.card:
            print(c("O", {False: "white", True: "green"}[row[0]]), c("O", {False: "white", True: "green"}[row[1]]), c("O", {False: "white", True: "green"}[row[2]]), c("O", {False: "white", True: "green"}[row[3]]))
        print(c("Green balls: " + str(self.team_blue.greens), {False: "white", True: "green"}[self.team_blue.greens >= 3]))
        print(c("Red balls: " + str(self.team_blue.reds), {False: "white", True: "red"}[self.team_blue.reds >= 3]))
        input("\n" + l[lang]["Press ENTER to continue -> "])
        time.sleep(0.2)




class Team:
    def __init__(self, name):
        self.name = name
        self.card = [[False, False, False, False],
                     [False, False, False, False],
                     [False, False, False, False],
                     [False, False, False, False],]
        self.pulled_numbers = []
        self.greens = 0
        self.reds = 0
        self.rounds_won_in_a_row = 0
        self.rounds_failed_in_a_row = 0
    
    def mark(self, num):
        if 1 <= num <= 16: self.card[(num - 1) // 4][(num - 1) % 4] = True

    def check_cart_win(self):
        for row in self.card:
            if all(row): return True

        for col in range(4):
            if all(self.card[row][col] for row in range(4)): return True

        if all(self.card[i][i] for i in range(4)): return True

        if all(self.card[i][3 - i] for i in range(4)): return True

        return False
        
    def __repr__(self):
        return self.name








main = Main()
main.game()