import json


def is_blank(string):
    name = string.strip()
    if name == "":
        return True
    else:
        return False


conversation_list = []


def conversation():
    text = None
    while text is None or text != "quit":
        text = input("> ")

        if text.lower() == "quit":
            with open("notes.json", "w") as f:
                json.dump(conversation_list, f)

            break

        if not is_blank(text):
            conversation_list.append(text)


conversation()
