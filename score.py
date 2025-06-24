from Utils import SCORES_FILE_NAME

def add_score(difficulty):
    score_to_add = (difficulty * 3) + 5
    current_score = 0

    try:
        with open(SCORES_FILE_NAME, 'r') as file:
            content = file.read().strip()
            if content.isdigit():
                current_score = int(content)
    except FileNotFoundError:
        # No existing score file, start at 0
        pass
    except Exception as e:
        print(f"Error reading the score file: {e}")
        return None

    new_score = current_score + score_to_add

    try:
        with open(SCORES_FILE_NAME, 'w') as file:
            file.write(str(new_score))
    except Exception as e:
        print(f"Error writing to the score file: {e}")
        return None

    return new_score
