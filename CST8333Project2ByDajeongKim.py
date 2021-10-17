import pandas as pd

""""
* Use File-IO on startup to open and read the dataset, initializing one hundred record objects with data parsed
  from the first one hundred records in the csv file.
* The record objects should be stored ina simple data structure (9array or a list), use exception handling
  in case the file is missing or not available.
* Dajeong Kim(#040983172)
"""

pd.set_option('display.max_rows', 3029)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)
try:
    df = pd.read_csv('vaccination-coverage-byVaccineType.csv', index_col=None, na_values=['NA'], sep=',')
    dfNew = df.head(100)
    df100 = dfNew.iloc[:,[0,1,2,3,4,5,6,7]]
    df100.to_csv("new-vaccination-file.csv", index_col=None, na_values=['NA'], sep=',')
    print("student name: Dajeong Kim, student Number : 040983172")

except Exception as e:
    print("Can't read the file", e)


class Options:
    def displayF(self):
        """
        * 1
        * Select and display either one record, or display multiple records from the in-memory data
        * Dajeong Kim(#040983172)
        """
        print("##DISPLAY RECORDS")
        print("#Which data do you want to read by?")
        print("1. prename")
        print("2. product_name")
        readby = input(": ")
        if readby == '1':
            print("#Canada / Newfoundland and Labrador / Nova Scotia / Quebec / Manitoba / Saskatchewan / "
                  "British Columbia / Yukon / Northwest Territories / Nunavut / Prince Edward Island / "
                  "New Brunswick / Alberta / ")
            inputPrename = input("Enter prename: ")
            dfSt11 = df100[df100['prename'] == inputPrename]
            print(dfSt11)

        elif readby == '2':
            print("#Not reported / Pfizer-BioNTech / Moderna / Unknown")
            inputProduct = input("#Enter product_name: ")
            dfSt12 = df100[df100['product_name'] == inputProduct]
            print(dfSt12)
        else:
            print("Invalid option. Try again.")

    def addF(self):
        """
        * 2
        * Create a new record and store it in the simple data structure in memory
        * Dajeong Kim(#040983172)
        """
        print("##CREATE A NEW RECORD")
        print("#Enter 8 values you want to add")
        print("#pruid, prename, prfname, week-end, product_name, numtotal_atleast1does, numtotla-partially,numtotal_fully")
        addedList = []
        for i in range(8):
            addedList.append(input(": "))
        df100.loc[len(df100)] = addedList
        print(df100.loc[len(df100) - 1, :])
        df100.to_csv("new-vaccination-file.csv")
        print("The record is added successfully.")

    def editF(self):
        """
        * 3
        * Select and edit a record held in the simple data structure in memory.
        * Dajeong Kim(#040983172)
        """
        print("##EDIT A RECORD")
        print("#Which column do you want to edit?")
        print("#pruid, prename, prfname, week-end, product_name, numtotal_atleast1does, numtotla-partially,numtotal_fully")
        editWhat = input(": ")
        print("#Which data do you want to edit?")
        editBe = input(": ")
        print("#What do you want this to be?")
        editAf = input(": ")
        df100[editWhat].replace({editBe: editAf}, inplace=True)
        dfEdit = df100[df100[editWhat] == editAf]
        df100.to_csv("new-vaccination-file.csv")
        print(dfEdit)

    def deleteF(self):
        """
        * 4
        * Select and delete a record from the simple data structure in memory
        * Dajeong Kim(#040983172)
        """
        print("##DELETE A RECORD")
        print("#Enter an index number of the record you want to delete")
        inNum = input(":  ")
        df100.drop(index=int(inNum), axis=0, inplace=True)
        df100.to_csv("new-vaccination-file.csv")
        print("#The record is deleted successfully")

if __name__ == '__main__':
    project = Options()
    """
    * Options
    * Select and display either one record or display multiple records from the in-memory data
    * Create a new record and store it in the simple data structure in memory
    * Select and edit a record held in the simple data structure in memory
    * Select and delete a record from the simple data structure in memory
    * Dajeong Kim(#040983172)
    """
    while True:
        print("##Welcome to Dajeong Kim's Assignment2")
        print("#Select what you want to do")
        print("1. Display records")
        print("2. Create a new record")
        print("3. Edit a record")
        print("4. delete a record")
        print("5. End this program")
        selection = input(": ")


        if selection == '1':
            project.displayF()
        elif selection == '2':
            project.addF()

        elif selection == '3':
            project.editF()

        elif selection == '4':
            project.deleteF()

        elif selection == '5':
            print("##THANK YOU FOR USING DAJEONG'S PROGRAM")
            df100.to_csv("new-vaccination-file.csv")
            break
        else:
            print("invalid input")
