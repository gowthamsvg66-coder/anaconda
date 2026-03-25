
input_file = "E:\MCA\input.txt"
output_file = "long_words.txt"

line_count = 0
word_count = 0
long_words = []

with open(input_file, "r") as f:
    for line in f:
        line_count += 1

        words = line.strip().split()
        word_count += len(words)

        for word in words:
            if len(word) > 5:
                long_words.append(word)

with open(output_file, "w") as f:
    for word in long_words:
        f.write(word + "\n")


print("Total lines:", line_count)
print("Total words:", word_count)
print("Long words saved to", output_file)
