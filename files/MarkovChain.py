class MarkovChain:

    def process_file(file_name):
        for each line
            words = file split on white space
            delete common words
            words.delete("a")
            words.delete("an")
            words.delete("and")
            words.delete("by")
            words.delete("for")
            words.delete("from")
            words.delete("in")
            words.delete("of")
            words.delete("on")
            words.delete("or")
            words.delete("out")
            words.delete("the")
            words.delete("to")
            words.delete("with")
            put words into bigram
                if the occurence doesn't exist yet, set it to 1
                if the occurence exists, increment
        return words

    def most_common_word(words):
        if key doesn't exist
            return null
        else if key exists
            return largest key

    def largest_key(words):
        return largest largest key

    def cleanup(title):
        remove special characters and such

    def create_title(word):
        first words
        title
        length
        while the length is < #
            word = most_common_word(word)
            if word = null and length is 1
                return first_word
            else if word is null
                break
            end
            break of title includes word
            title = title + word
            length ++
        end
        return title

    
