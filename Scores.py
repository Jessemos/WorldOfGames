from Utils import *


def add_score(difficulty):
    points_of_winning = (difficulty * 3) + 5
    file_info = FILES_PATH + SCORES_FILE_NAME
    f = open(file_info, "a+")
    f.seek(0)
    first_line: str = f.readline()
    if (first_line == '') or (first_line == '\n'):
        data_to_update = "Updated at: " + str(time_stamp()) + " | " + "Score: " + str(points_of_winning)
    else:
        old_total_str = first_line[first_line.rfind("Score:")+7:-1]
        if old_total_str.isnumeric():
                new_total = int(old_total_str) + points_of_winning
                data_to_update = "Updated at: " + str(time_stamp()) + " | Previous Score: " + old_total_str + "| New Score: " + str(new_total)
                f.truncate(0)
        else:
            data_to_update = ''
    if (data_to_update != ''):
        print("will update to file: %s" % data_to_update)
        f.write(str(data_to_update) + "\n")
    else:
        print("Nothing to update to file...")
    f.close()



