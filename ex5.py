file = open(input("Δώσε ένα αρχείο κειμένου: "), "r")
text = file.read()
x = text.replace(".", "")
x = x.replace(",", "")
x = x.replace("!", "")
x = x.replace("*", "")
x = x.replace(")", "")
x = x.replace("(", "")
print(x)
x = x.split()
str1 = " "
for word in x:
    if len(word) > 3:
        l = list(word)
        g = l[0]
        del(l[0])
        word = str1.join(l)
        word = word.replace(" ", "")
        new_word = word + g + "ay"
        print(new_word)


