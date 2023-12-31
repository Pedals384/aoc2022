
def read_text_file(path: str) -> list[str]:
    """Read text file.

    Reads an input text file into a list of strings. Removes trailing
    new line characters.

    Parameters
    ----------
    path : str
        path to input text file.

    Returns
    -------
    list: [str]
        text file content in a list of strings

    """
    with open(path, "r") as f:
        return [line.strip("\n") for line in f.readlines()]


DATAPATH = "test_input.txt"
my_scores = []
opponent_scores = []
matches = read_text_file(DATAPATH)

for match in matches:
    opponent_play, my_play = match.split(" ")
    #print(opponent_play)
    #print(my_play)


my_scores_dict = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

opponent_scores_dict = {
    "A": 1,
    "B": 2,
    "C": 3,
}

# loop through each line, if dictionary key in line, append item to each score
# sum the scores

for opponent_play, my_play in zip(opponent_play, my_play):
    for key, value in opponent_scores_dict.items():
        if key in opponent_play:
            opponent_scores.append(value)
    for key, value in my_scores_dict.items():
        if key in my_play:
            my_scores.append(value)
    if opponent_play.value > my_play.value:
        opponent_scores.append(6)
    if opponent_play.value == my_play.value:
        opponent_scores.append(3)
        my_scores.append(3)

print(my_scores)
print(opponent_scores)
print(opponent_play,my_play)