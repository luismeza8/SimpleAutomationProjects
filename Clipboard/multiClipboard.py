import sys
import clipboard
import json

savedData = "clipboard.json"


def saveData(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def loadData(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1]
    data = loadData(savedData)

    if command == "save":
        key = input("Enter a key: ")

        data[key] = clipboard.paste()
        saveData(savedData, data)

    elif command == "load":
        key = input("Enter a key: ")

        if key in data:
            clipboard.copy(data[key])
            print("Data copied to clipboard")
        else:
            print("Key does not exist")

    elif command == "list":
        print(data)

    elif command == "delete":
        key = input("Enter a key to delete it: ")

        if key in data:
            del data[key]
            saveData(savedData, data)
            print(f"Key: {key} deleted")

    else:
        print("Unknown command")
else:
    print("Please pass only one command")
