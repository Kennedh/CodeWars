"""
In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice and
digital data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−,
letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital
letters are used. When the message is written in Morse code, a single space is used to separate the character codes and
3 spaces are used to separate words. For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.

In addition to letters, digits and some punctuation, there are some special service codes, the most notorious of those
is the international distress signal SOS (that was first issued by Titanic), that is coded as ···−−−···. These special
codes are treated as single special characters, and usually are transmitted as separate words.

Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

For example:

decode_morse('.... . -.--   .--- ..- -.. .')
#should return "HEY JUDE"
NOTE: For coding purposes you have to use ASCII characters . and -, not Unicode characters.

The Morse code table is preloaded for you as a dictionary, feel free to use it:

C: provides parallel arrays, i.e. morse[2] == "-.-" for ascii[2] == "C"
Coffeescript/C++/Go/JavaScript/Julia/PHP/Python/Ruby/TypeScript/Groovy: MORSE_CODE['.--']
C#: MorseCode.Get(".--") (returns string)
Elixir: @morse_codes variable (from use MorseCode.Constants). Ignore the unused variable warning for morse_codes because
it's no longer used and kept only for old solutions.
Elm: MorseCodes.get : Dict String String
F#: MorseCode.get ".--" (returns string)
Haskell: morseCodes ! ".--" (Codes are in a Map String String)
Java: MorseCode.get(".--")
Kotlin: MorseCode[".--"] ?: "" or MorseCode.getOrDefault(".--", "")
NASM: a table of pointers to the morsecodes, and a corresponding list of ascii symbols
Racket: morse-code (a hash table)
Rust: MORSE_CODE
Scala: morseCodes(".--")
Swift: MorseCode[".--"] ?? "" or MorseCode[".--", default: ""]
All the test strings would contain valid Morse code, so you may skip checking for errors and exceptions. In C#, tests
will fail if the solution code throws an exception, please keep that in mind. This is mostly because otherwise the
ngine would simply ignore the tests, resulting in a "valid" solution.

Good luck!
"""

MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '...---...': 'SOS'  # Exemplo para o teste '... --- ...' se for tratado como uma palavra
}


def decode_morse(morse_code, morse_map=MORSE_CODE):
    morse_code = morse_code.strip()
    morse_words = morse_code.split('   ')
    decoded_words = []

    for word in morse_words:
        if not word:
            continue

        morse_letters = word.split(' ')
        decoded_letters = []

        for letter_code in morse_letters:
            if letter_code in morse_map:
                decoded_letters.append(morse_map[letter_code])

        decoded_word = "".join(decoded_letters)
        decoded_words.append(decoded_word)

    return " ".join(decoded_words)

# Teste

print(decode_morse('----- .---- ..--- ---.. ----.'))
print(decode_morse('... --- ...'))
print(decode_morse('...   ---   ...'))
print(decode_morse('----- .---- ..--- ---.. ----.'))