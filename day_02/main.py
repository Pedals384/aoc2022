
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


DATAPATH = "input.txt"

matches = read_text_file(DATAPATH)

#print(matches)

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

def find_scores(matches):
    my_scores = []
    opponent_scores = []
    for match in matches:
        opponent_play, my_play = match.split(" ")
        opponent_scores.append(opponent_scores_dict[opponent_play])
        my_scores.append(my_scores_dict[my_play])
    
    #print(opponent_scores, my_scores)                
    return opponent_scores, my_scores

#find_scores(matches)

def score_wins():
    my_wins = []
    opponent_wins = []
    opponent_scores, my_scores = find_scores(matches)

    for opponent_score, my_score in zip(opponent_scores, my_scores):
        #print(opponent_scores)
        #print(my_scores)
        if opponent_score == 1:
            if my_score == 1:
                my_wins.append(3)
                opponent_wins.append(3)
            elif my_score == 2:
                my_wins.append(6)
            else:
                opponent_wins.append(6)
        elif opponent_score == 2:
            if my_score == 1:
                opponent_wins.append(6)
            elif my_score == 2:
                my_wins.append(3)
                opponent_wins.append(3)
            else:
                my_wins.append(6)
        else:
            if my_score == 1:
                my_wins.append(6)
            elif my_score == 2:
                opponent_wins.append(6)
            else:
                my_wins.append(3)
                opponent_wins.append(3)
            
        # if opponent_score > my_score:
        #     opponent_wins.append(6)
        # elif opponent_score == my_score:
        #     opponent_wins.append(3)
        #     my_wins.append(3)
        # elif my_score == 1 and opponent_score ==3:
        #     my_wins.append(6)
        # elif opponent_score == 1 and my_score == 3:
        #     opponent_wins.append(6)
        # elif my_score > opponent_score:
        #     my_wins.append(6)
        #    # print(my_wins)
    return sum(my_scores) + sum(my_wins)

score_wins()

