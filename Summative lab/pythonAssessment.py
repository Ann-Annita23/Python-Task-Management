import re
def count_specific_word(text,search_word):
    count=0

    words=text.split()

    for word in words:
        if word==search_word:
            count+=1
    return count

def identify_most_common_word(text):
    if not text.strip():
        return None

    highest_count=0
    most_common_word="" # It has the "" because it is a string and we want to return a string

    common_words=text.split()  
    unique_words=list(set(common_words)) # This will give us the unique words in the text, while set will give us the unique words in the text, while list will convert it back to a list so we can iterate through it
    
    for word in unique_words:
        current_count=common_words.count(word)# this will count the number of times the word appears in the text
        if current_count>highest_count: # This will check if the current count is greater than the highest count, if it is then it will update the highest count and the most common word
            highest_count=current_count # This will update the highest count to the current count
            most_common_word=word
        return most_common_word  

def calculate_average_word_length(text):
    total_length=0

    words=text.split()
    total_words=len(words)

    for word in words:
        total_length+=len(word) # This will add the length of each word to the total length
        if total_words==0: # This will check if the total words is 0, if it is then it will return 0 to avoid division by zero
            return 0

    average_length=total_length/total_words # This will calculate the average length of the words by dividing the total length by the total words
    return average_length

def calculate_average_word_length(text):
    if not text.strip():
        return 0.0

    cleaned_text=re.sub(r'[^\w\s]','',text) # This will remove any punctuation from the text, while re.sub will replace any character that is not a word character or whitespace with an empty string
    words=cleaned_text.split()
    if not words:
        return 0.0

    total_characters=0
    total_words=0

    for word in words:
        total_characters+=len(word)
        total_words+=1 # This will count the total number of words in the text
        average_length=total_characters/total_words # This will calculate the average length of the words by dividing the total characters by the total words
    return float(average_length)

def count_paragraphs(text):       
    if text.strip()=="":
        return 1
    paragraph_numbering= text.strip().split('\n\n')
    return len(paragraph_numbering)

def count_sentences(text):
    if text.strip()=="":
        return 1
    
    sentences= re.split(r'[.!?]+', text)
    actual_sentences=[sentence for sentence in sentences if sentence.strip()!=""]# This will split the text into sentences based on the punctuation marks (., !, ?) and then it will filter out any empty sentences that may be created due to multiple punctuation marks or leading/trailing punctuation. The list comprehension is used to create a new list of actual sentences that are not empty after stripping whitespace.
    return len(actual_sentences)

if __name__=="__main__":

    text="""ACME Inc. Unveils Revolutionary Apple Pie Machine, Transforming Baking with Automation

ACME Inc., a leading innovator in culinary technology, has launched a groundbreaking new device that promises to revolutionize the way apple pies are made. Dubbed the “Apple Pie Master,” this machine combines cutting-edge technology with traditional baking techniques to automate the entire pie-making process, ensuring perfect pies every time.

At a press conference held at ACME Inc.'s headquarters in Springfield, the company's CEO, Jane Doe, introduced the Apple Pie Master to an eager audience of journalists, culinary experts, and industry insiders. "Our goal has always been to make cooking and baking accessible and enjoyable for everyone, and with the Apple Pie Master, we are making a giant leap forward," Doe stated.

The Apple Pie Master is designed to simplify the baking process while maintaining the quality and taste of a homemade pie. The machine is equipped with AI-driven sensors that can analyze the quality of ingredients, adjust cooking times, and even replicate intricate baking techniques perfected by master chefs. “This isn't just about saving time; it's about enhancing the baking experience and ensuring consistent results,” Doe explained.

Unpacking the Technology

The heart of the Apple Pie Master lies in its advanced artificial intelligence system. This system is programmed to perform tasks such as peeling and slicing apples, mixing ingredients, and rolling out pie crusts. According to ACME Inc.'s head of product development, Dr. Emily Clark, “The AI not only replicates human actions but learns from each pie made, adjusting its techniques to improve the next one.”

Another innovative feature of the Apple Pie Master is its real-time monitoring capabilities. Cameras and sensors inside the machine provide continuous feedback during the pie-making process, allowing the AI to make micro-adjustments to the temperature and cooking times as needed. This ensures that each pie is baked to golden perfection.

User-Friendly Features

ACME Inc. has designed the Apple Pie Master with user experience in mind. The machine features a sleek, user-friendly interface with pre-programmed settings for different pie recipes. Users can select options for crust type, spice levels, and even the variety of apples they want to use. “We want to cater to all taste preferences, from the traditional to the adventurous,” said marketing director, Tom Nguyen.

The machine also includes a mobile app, allowing users to start the baking process from their smartphones. This app not only controls the machine but also provides users with tips, recipes, and the option to order ingredients directly through ACME Inc.'s partners.

Environmental and Economic Impact

ACME Inc. is also proud of the Apple Pie Master’s environmental credentials. The machine is built from recycled materials and designed to operate with minimal energy consumption. “Sustainability is at the core of all our product designs,” emphasized environmental consultant Lisa Green, who collaborated on the project.

Economically, the Apple Pie Master could have significant implications for both commercial and home bakers. By reducing the time and skill required to make high-quality pies, it opens up new business opportunities for small bakeries and restaurants, and it provides a cost-effective solution for busy consumers who crave homemade desserts without the fuss.

Market Response and Availability

The response to the Apple Pie Master has been overwhelmingly positive. Early adopters and reviewers have praised its ease of use and the quality of the pies it produces. Culinary blogger Mark Spencer commented, “It’s like having a professional baker in your kitchen. The pies are consistently excellent, with perfectly flaky crusts and rich, flavorful fillings.”

ACME Inc. plans to make the Apple Pie Master available online and in select retail stores starting next month. The company has set a competitive price point to make this innovative technology accessible to a broad audience.

The Future of Automated Baking

Looking ahead, ACME Inc. plans to expand its range of automated baking machines. “The Apple Pie Master is just the beginning,” said CEO Jane Doe. “We’re exploring machines for other types of desserts and complex dishes. Our vision is to automate parts of the cooking process without sacrificing the art of cooking.”

The Apple Pie Master from ACME Inc. represents a significant advancement in the field of culinary technology. By automating the process of baking apple pies, this machine not only makes baking more accessible but also sets a new standard for the integration of technology in traditional cooking practices. As more consumers and businesses adopt this technology, it could well redefine our cooking experiences and expectations.
"""    
keep_going=True
while keep_going:
    print("Please select an option:")
    print("1. Get number of times a specific word is used in the text")
    print("2. Identify the most common word in the text")
    print("3. Calculate the average word length in the text")
    print("4. Count the number of paragraphs in the text")
    print("5. Count the number of sentences in the text")
    print("6. Exit")
    choice=input("Enter your choice (1-6): ")

    if choice=="1":
        search_word=input("Enter the word you want to search for: ")
        count=count_specific_word(text,search_word)
        print(f"The word '{search_word}' is used {count} times in the text.")
        

    elif choice=="2":
        most_common_word=identify_most_common_word(text)
        print(f"The most common word in the text is: '{most_common_word}'")

    elif choice=="3":
        average_length=calculate_average_word_length(text)
        print(f"The average word length in the text is: {average_length:.2f} characters per word.")

    elif choice=="4":
        paragraph_count=count_paragraphs(text)
        print(f"The number of paragraphs in the text is {paragraph_count}.")

    elif choice=="5":
        sentence_count=count_sentences(text)
        print(f"The number of sentences in the text is {sentence_count}.")

    elif choice=="6":
        print("Exiting the program. Goodbye!")
        keep_going=False
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
