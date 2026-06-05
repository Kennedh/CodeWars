"""
Your task in this Kata is to emulate text justification in monospace font. You will be given a single-lined text and
the expected justification width. The longest word will never be greater than this width.

Here are the rules:

Use spaces to fill in the gaps between words.
Each line should contain as many words as possible.
Use '\n' to separate lines.
Last line should not terminate in '\n'
'\n' is not included in the length of a line.
Gaps between words can't differ by more than one space.
Lines should end with a word not a space.
Large gaps go first, then smaller ones ('Lorem--ipsum--dolor--sit-amet,' (2, 2, 2, 1 spaces)).
Last line should not be justified, use only one space between words.
Lines with one word do not need gaps ('somelongword\n').
Example with width=30:

Lorem  ipsum  dolor  sit amet,
consectetur  adipiscing  elit.
Vestibulum    sagittis   dolor
mauris,  at  elementum  ligula
tempor  eget.  In quis rhoncus
nunc,  at  aliquet orci. Fusce
at   dolor   sit   amet  felis
suscipit   tristique.   Nam  a
imperdiet   tellus.  Nulla  eu
vestibulum    urna.    Vivamus
tincidunt  suscipit  enim, nec
ultrices   nisi  volutpat  ac.
Maecenas   sit   amet  lacinia
arcu,  non dictum justo. Donec
sed  quam  vel  risus faucibus
euismod.  Suspendisse  rhoncus
rhoncus  felis  at  fermentum.
Donec lorem magna, ultricies a
nunc    sit    amet,   blandit
fringilla  nunc. In vestibulum
velit    ac    felis   rhoncus
pellentesque. Mauris at tellus
enim.  Aliquam eleifend tempus
dapibus. Pellentesque commodo,
nisi    sit   amet   hendrerit
fringilla,   ante  odio  porta
lacus,   ut   elementum  justo
nulla et dolor.
Also you can always take a look at how justification works in your text editor or directly in HTML
(css: text-align: justify).

Have fun :)
"""


def justify(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) <= width:
            current_line.append(word)
            current_length += len(word)
        else:
            if current_line:
                lines.append(current_line)

            current_line = [word]
            current_length = len(word)
    if current_line:
        lines.append(current_line)

    justified_lines = []
    for i, line_words in enumerate(lines):
        if i == len(lines) - 1:
            justified_lines.append(' '.join(line_words))
        elif len(line_words) == 1:
            justified_lines.append(line_words[0])
        else:
            total_spaces = width - sum(len(word) for word in line_words)
            gaps = len(line_words) - 1
            base_spaces = total_spaces // gaps
            extra_spaces = total_spaces % gaps
            justified_line = []

            for j, word in enumerate(line_words):
                justified_line.append(word)
                if j < gaps:
                    spaces = base_spaces + (1 if j < extra_spaces else 0)
                    justified_line.append(' ' * spaces)
            justified_lines.append(''.join(justified_line))
    return '\n'.join(justified_lines)

# Test

print(justify("G JUTcJwsYO WQlDTjtUA Pcvav vmJsYaPNYI R BPN ezFZOMDVM NZn ySx TxtRoy dPHN HFReBmeI WBT MQpJGCxyHw "
              "xVXTIiTne vxwqYvUtk CwgufMBwr DxDfA hcUnv RFzEzFlNC MdrueDyQ BMQk pJAY UZo pa V CRAqj jvolZTc L JbLrxTr "
              "aeMTu wlG ec EYPKMq CTnrfxL dMPQSncD YFAaaRU",width=23))