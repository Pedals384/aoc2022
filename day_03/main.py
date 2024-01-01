
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

rucksacks = read_text_file(DATAPATH)

#print(rucksacks)

def set_priorities():
    
    priorities = {
        "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, 
        "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16,
        "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24,
        "y": 25, "z": 26, "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F": 32, 
        "G": 33, "H": 34, "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40, 
        "O": 41, "P": 42, "Q": 43, "R": 44, "S": 45, "T": 46, "U": 47, "V": 48, 
        "W": 49, "X": 50, "Y": 51, "Z": 52
        }
    
    return priorities

def find_common_items(rucksacks):
    """

    Args:
        rucksacks (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    priorities = set_priorities()

    priorities_sum = 0
    for rucksack in rucksacks:
        half = int(len(rucksack)//2)
        compartment_1 = rucksack[:half]
        compartment_2 = rucksack[half:]
        
        for letter in compartment_1:
            if letter in compartment_2:
                priorities_sum = priorities_sum + priorities[letter]
                break
        
    return priorities_sum


find_common_items(rucksacks)


def create_chunks(rucksacks):
    chunks = []
    chunk_size = 3
    for i in range(0, len(rucksacks)):
        if i % 3 !=0:
            pass
        else:
            chunk = rucksacks[i:i+chunk_size]
            chunks.append(chunk)

    return chunks

chunks = create_chunks(rucksacks)
           
def find_item_in_chunk(chunks):
    priorities = set_priorities()
    shared_items = 0
    for chunk in chunks:
            for i in chunk[0]:
                if i in chunk[1] and chunk[2]:
                    shared_items = shared_items + priorities[i]
                    break
    print(shared_items)
    
find_item_in_chunk(chunks)