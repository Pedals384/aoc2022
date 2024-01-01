
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


def set_priorities():
    """Creates a dictionary matching lower and upper case letters to 
    values so this can be used to calculate item priority scores in
    later functions.

    Returns:
        priorities [dictionary]: Dictionary matching upper and lower
        case letters to values.
    """
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
    Splits the string for each rucksack into equal halves, finds the 
    letter common to both halves and uses the priorities dictionary to
    add the value for that letter to a total score. 
    
    Args:
        rucksacks (list): List of strings containing a mix of lower and
        upper case letters representing items in rucksacks. Each string
        is made of 2 halves which require separating as part of the 
        function.

    Returns:
        priorities_sum (int): Sum of the values attached to each letter
        found in both halves of the string, with the value based on 
        the priorities dictionary. 
    """
    
    # call function for priorities dictionary
    priorities = set_priorities()

    priorities_sum = 0
    for rucksack in rucksacks:
        # ensure strings get split at halfway point regardless of length
        half = int(len(rucksack)//2)
        compartment_1 = rucksack[:half]
        compartment_2 = rucksack[half:]
        
        for letter in compartment_1:
            if letter in compartment_2:
                priorities_sum = priorities_sum + priorities[letter]
                # avoid adding priority values for duplicates
                break
        
    return priorities_sum



find_common_items(rucksacks)


def create_chunks(rucksacks):
    """ Splits the list of rucksacks into chunks of 3, avoiding the 
    same rucksack appearing in multiple chunks by passing on items in 
    the rucksacks list that are not a multiple of 3. 

    Args:
        rucksacks (list): List of strings representing rucksacks.

    Returns:
        chunks (list): List of lists, each containing three strings.
    """
    chunks = []
    chunk_size = 3
    for i in range(0, len(rucksacks)):
        if i % 3 !=0:
            pass
        else:
            # Ensures each value only appears in one chunk
            chunk = rucksacks[i:i+chunk_size]
            chunks.append(chunk)

    return chunks

chunks = create_chunks(rucksacks)
           
def find_item_in_chunk(chunks):
    """ Searches each chunk of three strings to find the letter common
    to all three. Finds the value for that letter based on the 
    priorities dictionary and sums the scores for all shared items 
    across the dataset.

    Args:
        chunks (list): List of lists, each containing three strings of 
        a mixture of lower and upper case letters.
    """
    
    priorities = set_priorities()
    
    shared_items = 0
    for chunk in chunks:
            for i in chunk[0]:
                if i in chunk[1] and i in chunk[2]:
                    shared_items += priorities[i]
                    break
    print(shared_items)
    
find_item_in_chunk(chunks)