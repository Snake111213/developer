import cvs 
import string

translator = str.maketrans('','', string.punctuation)

word_count = {}
text = open('declaracion.txt').read()

words = text.split()
for word in words:
    word = word.translate(translator).lower()
    count = word_count.get(word, 0)
    count += 1 
    word_count[word] = count
    
word_count_list = sorted(word_count, key=word_count.get, reverse=True)
for word in word_count[:10]:
    print(word, word_count[word])

output_file = open('words.csv','w')
writer = cvs.writer(output_file)
writer.writerow(['word','cout'])
for word in word_count_list:
    writer.writerow([word,word_count[word]])   