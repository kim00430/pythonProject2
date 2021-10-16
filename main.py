import csv

print("student name: Dajeong Kim, student Number : 040983172")

with open('vaccination-coverage-byVaccineType.csv', 'r') as openFile:
    openFile = csv.reader(openFile, delimiter=',')
    openFileList = list(openFile)
    reader = csv.DictReader(openFile)
    for row in reader:
        print(row)

    """
    * Persist the data from memory to the disk as a comma-separated file, writing a new file.
    * Dajeong Kim(#040983172)
    """
    reloadFile = open('new-file.csv', 'w', newline='')
    writer = csv.writer(reloadFile)
    writer.writerow(openFileList[0])
    """
    * Use File-IO on startup to open and read the dataset, initializing one hundred record objects with data parsed
      from the first one hundred records in the csv file.
    * The record objects should be stored ina simple data structure (9array or a list), use exception handling
      in case the file is missing or not available.
    * Dajeong Kim(#040983172)
    """
    try:
        for i in range(100):
            writer.writerow(openFileList[i + 1])  ## Skip over the column names

    except Exception as e:
        print("The file is missing or not available.", e)

    reloadFile.close()
    """
    * Options
    * Select and display either one record or display multiple records from the in-memory data
    * Create a new record and store it in the simple data structure in memory
    * Select and edit a record held in the simple data structure in memory
    * Select and delete a record from the simple data structure in memory
    * Dajeong Kim(#040983172)
    """
    while True:
        print("Welcome to Dajeong Kim's Assignment2")
        print("Select what you want to do")
        print("1. Display records")
        print("2. Create a new record")
        print("3. Edit a record")
        print("4. delete a record")
        print("5. End this program")
        selection = input(": ")

        """
        * 1
        * Select and display either one record, or display multiple records from the in-memory data
        * Dajeong Kim(#040983172)
        """
        savedFile = open('new-file.csv', 'r')
        savedFileList = list(savedFile)
        savedReader = csv.DictReader(savedFile)
        if selection == '1':
            print("DISPLAY RECORDS")
            print("Which data do you want to read? ")
            print("1. Pick by data number")
            print("2. Pick by prename")
            option = input(":  ")
            if option == '1':
                print("You can pick 1 to 100 or more")
                try:
                    display = input(": ")
                    cvDisplay = int(display)
                    print(openFileList[0])
                    for line in savedReader:
                        print(line)
                    savedFile.close()
                except Exception as e:
                    print("The data is not exist. Try again", e )
            elif option == '2':
                print("You can pick by prename")
                try:
                    inputPrename = input(":  ")
                    for line in savedReader:
                        if line[2] == inputPrename:
                            print(line)

                except Exception as e:
                    print("The data is not exist. Try agian", e)


            """
            * 2
            * Create a new record and store it in the simple data structure in memory
            * Dajeong Kim(#040983172)
            """
        elif selection == '2':
            addRecord = open('new-file.csv', 'a')
            pruidNew = input("Enter pruid: ")
            prenameNew = input("Enter prename: ")
            prfnameNew = input("Enter prfname: ")
            week_endNew = input("Enter week-end: ")
            product_nameNew = input("Enter product_name: ")
            numtotal_atleast1doseNew = input("Enter numtotal_atleast1dose: ")
            numtotal_partiallyNew = input("Enter numtotal_partially: ")
            numtotal_fullyNew = input("Enter numtotal_fully: ")
            prop_atleast1doseNew = input("Enter_atleast1dose: ")
            prop_partiallyNew = input("Enter prop_partially: ")
            prop_fullyNew = input("Enter prop_fully: ")

            addRecord.write(pruidNew)
            addRecord.write(',')
            addRecord.write(prenameNew)
            addRecord.write(',')
            addRecord.write(prfnameNew)
            addRecord.write(',')
            addRecord.write(week_endNew)
            addRecord.write(',')
            addRecord.write(product_nameNew)
            addRecord.write(',')
            addRecord.write(numtotal_atleast1doseNew)
            addRecord.write(',')
            addRecord.write(numtotal_partiallyNew)
            addRecord.write(',')
            addRecord.write(numtotal_fullyNew)
            addRecord.write(',')
            addRecord.write(prop_atleast1doseNew)
            addRecord.write(',')
            addRecord.write(prop_partiallyNew)
            addRecord.write(',')
            addRecord.write(prop_fullyNew)
            addRecord.close()
            print("The new record is saved successfully.")

            addRecord.close()

            """
            * 3
            * Select and edit a record held in the simple data structure in memory.
            * Dajeong Kim(#040983172)
            """
        elif selection == 3:
            editRecord = open('new-file.csv', 'r')
            editRecordList = list(editRecord)
            print("Which number of record do you want to edit?")
            editNum = input(": ")
            num = int(editNum)
            print("Which data of the record do you want to edit?")
            editData = input(": ")
            data = int(editData)
            print("What do you want to edit to?")
            editText = input(": ")

            """
            * 4
            * Select and delete a record from the simple data structure in memory
            * Dajeong Kim(#040983172)
            """
        elif selection == '4':
            print("delete")

            """
            * 5
            * End Program
            * Dajeong Kim(#040983172)
            """
        elif selection == '5':
            break

        else:
            print("Invalid input")




