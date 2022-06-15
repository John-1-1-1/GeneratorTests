import markdown
import random


class generator:

    def __init__(self):
        self.code = ""
        self.counter = 1
        self.list_questions = []


    def add_note(self, qestion, list_answers):
        self.list_questions.append([qestion, list_answers])
        self.code += "### "+ str(self.counter) +". " + qestion + "\n"
        for i in list_answers:
            self.code += " * [ ] " + i + " \n"
        self.code += " \n"
        self.counter += 1


    def add_report(self, countVariants,
                   convertQestions,
                   randomQestions,
                   convertAnswer,
                   count_q):

        rand_list_q = [list(range(count_q)) for i in range(countVariants)]
        if randomQestions:
            rand_list_q = self.random_list_questions(countVariants,
                                                 len(self.list_questions),
                                                 count_q)

        if convertQestions:
            rand_list_q = [self.converted(i) for i in rand_list_q]

        rand_list_q = [[[k, list(range(len(
            self.list_questions[k][1])))] for k in i] for i in rand_list_q]

        if convertAnswer:
            rand_list_q =[[[j[0], self.converted(j[1])]
                           for j in i] for i in rand_list_q]

        variants = 1
        for i in rand_list_q:
            coun = 1
            code = ""
            codeDefoult = ""
            for k in i:
                code += "### " + str(coun) + ". " + self.list_questions[k[0]][0] + "\n"
                codeDefoult += "### " + str(coun) + ". " + self.list_questions[k[0]][0] + "\n"
                answers = self.list_questions[k[0]][1]
                for j in k[1]:
                    if j == 0:
                        code += " * [x] " + answers[j] + " \n"
                    else:
                        code += " * [ ] " + answers[j] + " \n"
                    codeDefoult += " * [ ] " + answers[j] + " \n"
                    code += " \n"
                    codeDefoult  += " \n"
                coun += 1
            f = open("variant_"+str(variants)+".html", "w")
            f.write(" <meta charset=\"utf-8\">" +
                    markdown.markdown(code, extensions=['pymdownx.tasklist']))
            f.close()

            f = open("def_variant_" + str(variants) + ".html", "w")
            f.write(" <meta charset=\"utf-8\">" +
                    markdown.markdown(codeDefoult, extensions=['pymdownx.tasklist']))
            f.close()
            variants += 1




        f = open('all_list.html', 'w', encoding='utf-8')
        output = markdown.markdown(self.code, extensions=['pymdownx.tasklist'])
        f.write(" <meta charset=\"utf-8\">" + output)
        f.close()


    def random_list_questions(self, counts, count_questions,
                          count_questions_in_variant):
        list_id = []
        for i in range(counts):
            lis = list(range(count_questions))
            for k in range(count_questions-count_questions_in_variant):
                lis.pop(random.randint(0,len(lis)-1))
            list_id.append(lis)
        return list_id


    def converted(self, lis):
        for i in range(2*len(lis)):
            [i,j] = [random.randint(0,len(lis)-1) for _ in range(2)]
            lis[i], lis[j] = lis[j], lis[i]
        return lis