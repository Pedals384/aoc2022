import re


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

assignments = read_text_file(DATAPATH)
# set to zero for later
total_combinations = 0


for line in assignments:
    job_1, job_2 = line.split(",")
    pattern = r"(\d+)"
    # start and end positions to identify range
    assignment_1_start, assignment_1_end = re.findall(pattern, job_1)
    assignment_2_start, assignment_2_end = re.findall(pattern, job_2)

    # convert start and end points to range
    assignment_1_range = (int(assignment_1_start)), int(assignment_1_end)
    assignment_2_range = ((int(assignment_2_start)), int(assignment_2_end))

    for assignment in assignments:
        if assignment_1_range[0] <= assignment_2_range[0] and assignment_1_range[1] >= assignment_2_range[1]:
            total_combinations += 1
            break
        elif assignment_2_range[0] <= assignment_1_range[0] and assignment_2_range[1] >= assignment_1_range[1]:
            total_combinations += 1
            break
        else:
            break


    print(total_combinations)
