
if __name__ == "__main__":
    import os




    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    backup_path = os.path.join(desktop_path, "Backup")


    if not os.path.exists(backup_path):
        os.mkdir(backup_path)
    os.chdir(backup_path)



    if "notes.txt" not in os.listdir() and "notes_old.txt" not in os.listdir():
        with open(os.path.join(backup_path, "notes.txt"), "w") as file:
            file.write("Backup Initialized")
    else:
        print("Notes file already exists")

    notesFilePath = os.path.join(backup_path, "notes.txt")


    print("File path is " + os.path.abspath(notesFilePath))
    if os.path.isfile(notesFilePath):
        print("Its a file")
    else:
        print("Is a directory")

    input("Press Enter to continue...")

    if "notes_old.txt" not in os.listdir():
        os.rename(notesFilePath, "notes_old.txt")
    if "notes_old.txt" in os.listdir():
        notesFilePath = os.path.join(backup_path, "notes_old.txt")
    else:
        print("It's already renamed")
    print("Parent path is: " + os.path.dirname(notesFilePath))
    for file in os.listdir(backup_path):
        print(file)

    answer = input("Do you want to delete these files? (y/n): ")
    if answer == "y":
        os.remove(notesFilePath)
        if os.listdir(backup_path) == []:
            os.chdir(desktop_path)
            os.rmdir(backup_path)
        else:
            print("Directory is not empty")
    else:
        exit()



