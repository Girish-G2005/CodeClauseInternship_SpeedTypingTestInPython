import time


def speed_typing_test():
    text_to_type = "I am going to the park."
    print("Type the following text:")
    print(text_to_type)
    input("Press Enter when you are ready to start...")

    start_time = time.time()

    user_input = input("Start typing here: ")

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Counting the number of words in the text
    word_count = len(text_to_type.split())

    # Counting the number of correctly typed words
    correct_words = sum(1 for word1, word2 in zip(text_to_type.split(), user_input.split()) if word1 == word2)

    # Calculating words per minute (WPM) and accuracy
    wpm = (correct_words / elapsed_time) * 60
    accuracy = (correct_words / word_count) * 100

    print("\nTyping speed: {:.2f} WPM".format(wpm))
    print("Accuracy: {:.2f}%".format(accuracy))


if __name__ == "__main__":
    speed_typing_test()
