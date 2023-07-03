import mysql.connector
import random
import datetime

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="0927867Frosty",
        database="dbpetservice"
    )
    if connection.is_connected():
        print("Connected to MySQL database.")
except mysql.connector.Error as error:
    print("Error connecting to MySQL database:", error)



class Appointment:

    def __init__(self):
        self.columns = ['ID', 'Date', 'Time', 'Avail Type', 'Status', 'Pet ID', 'Owner ID'] #Pet ID and Service ID are foreign keys
        self.cursor = connection.cursor(buffered=True)

    # generate Random Unique ID
    def generateID (self):
        query = "SELECT appointmentID FROM tblappointment_history"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        id = random.randint(1000, 9999)
        for x in result:
            if id == x[0]:
                id = random.randint(1000, 9999)
        return id

    
    #add (add information then add to appHistory) 
    def addAppointment (self, date, time, availType, status, petName, petSpecies, petBreed, ownerName, phoneNum):
        #generate appointmentID
        id = self.generateID() #?

        ownerID =ownerObject.addOwner(ownerName, phoneNum)
        petID = petObject.addPet(petName, petSpecies, petBreed, ownerID)
        
        
        date_obj = datetime.datetime.strptime(date, '%d/%m/%Y')
        date = date_obj.strftime('%Y-%m-%d')
        time_obj = datetime.datetime.strptime(time, '%I:%M %p')
        time = time_obj.strftime('%H:%M:%S')
        
        query = "INSERT INTO tblappointment_history (appointmentID, date, time, availType, status, petID, ownerID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (id, date, time, availType, status, petID, ownerID)
        self.cursor.execute(query, values)
        connection.commit()
        print("Appointment added.")
        
    def deleteAppointment (self, id):  
        query = "DELETE FROM tblappointment_history WHERE appointmentID = %s"
        values = (id,)
        self.cursor.execute(query, values)
        connection.commit()
        print("Appointment deleted.")
    
    #need changes
    def searchAppointment (self, value):
        value = str(value).lower() + '%'
        self.cursor.execute("SELECT * FROM tblappointment_history WHERE LOWER(`ID`) LIKE %s OR LOWER(`name`) LIKE %s OR LOWER(`cost`) LIKE %s", 
                    (f"%{value}", f"%{value}", f"%{value}", f"%{value}", f"%{value}", f"%{value}", f"%{value}"))
        searchResults = self.cursor.fetchall()
        
        for x in searchResults:
            print(x)
        return searchResults
    
    #return History (return all appointments)
    def returnAppointmentData (self):
        self.cursor.execute("SELECT * FROM tblappointment_history")
        result = self.cursor.fetchall()
        return result
        
    availType = ["Reservation", "Walk-in"]
    status = ["Pending", "Canceled", "Completed"]


# -------------------------------------------------------------------------------------------------------
class Owner:

    def __init__(self):
        self.columns = ['ID', 'Name', 'Phone Number']
        self.cursor = connection.cursor(buffered=True)

    # generate Random Unique ID
    def generateID (self):
        query = "SELECT ownerID FROM tblowner"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        id = random.randint(1000, 9999)
        for x in result:
            if id == x[0]:
                id = random.randint(1000, 9999)
        return id
    
    # check if OwnerID already exists in tblowner
    def checkOwnerID (self, ownerID):
        query = "SELECT ownerID FROM tblowner"
        self.cursor.execute(query)
        if self.cursor.fetchone:
                return True
        return False
    
    #add 
    def addOwner (self, name, phoneNum):
        id = self.generateID() #?
  
        query = "INSERT INTO tblowner (ownerID, name, phoneNumber) VALUES (%s, %s, %s)"
        values = (id, name, phoneNum)
        self.cursor.execute(query, values)
        connection.commit()
        print("Owner added.")

        return id
    

    #delete
    def deleteOwner (self, id):
        query = "DELETE FROM tblowner WHERE ownerID = %s"
        values = (id)
        self.cursor.execute(query, values)
        connection.commit()
        print("Owner deleted.")

    #update
    def updateOwner (self, id, name, phoneNum):
        query = "UPDATE tblowner SET name = %s, phoneNum = %s WHERE ownerID = %s"
        values = (name, phoneNum, id)
        self.cursor.execute(query, values)
        connection.commit()
        print("Owner updated.")

    #display
    def displayOwner (self):
        self.cursor.execute("SELECT * FROM tblowner")
        result = self.cursor.fetchall()
        return result

    #search
    def searchOwner (self, id):
        query = "SELECT * FROM tblowner WHERE ownerID = %s"
        values = (id)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result

    #return Owner name
    def returnOwnerName (self, id):
        query = "SELECT name FROM tblowner WHERE ownerID = %s"
        values = (id)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result
    
    def returnOwnerData (self):
        self.cursor.execute("SELECT * FROM tblowner")
        result = self.cursor.fetchall()
        return result 
    
  
class Pet:

    def __init__(self):
        self.columns = ['ID', 'Name', 'Species', 'Breed', 'Owner ID'] #Owner ID is foreign key
        self.cursor = connection.cursor(buffered=True)

    # generate Random Unique ID   
    def generateID (self):
        query = "SELECT petID FROM tblpet"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        id = random.randint(1000, 9999)
        for x in result:
            if id == x[0]:
                id = random.randint(1000, 9999)
        return id
    
    # check if PetID already exists in tblpet
    def checkPetID (self, petID):
        query = "SELECT petID FROM tblpet"
        self.cursor.execute(query)
        if self.cursor.fetchone:
                return True
        return False


    #add
    def addPet (self, name, species, breed, ownerID):
        id = self.generateID() #?
    
        query = "INSERT INTO tblpet (petID, name, species, breed, ownerID) VALUES (%s, %s, %s, %s, %s)"
        values = (id, name, species, breed, ownerID)
        self.cursor.execute(query, values)
        connection.commit()
        print("Pet added.")

        return id

    #delete
    def deletePet (self, id):
        query = "DELETE FROM tblpet WHERE petID = %s"
        values = (id)
        self.cursor.execute(query, values)
        connection.commit()
        print("Pet deleted.")

    #update
    def updatePet (self, id, name, species, breed):
        query = "UPDATE tblpet SET name = %s, species = %s, breed = %s WHERE petID = %s"
        values = (name, species, breed, id)
        self.cursor.execute(query, values)
        connection.commit()
        print("Pet updated.")

    #display
    def displayPet (self):
        self.cursor.execute("SELECT * FROM tblpet")
        result = self.cursor.fetchall()
        return result

    #search
    def searchPet (self, id):
        query = "SELECT * FROM tblpet WHERE petID = %s"
        values = (id)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result

    #return pet name
    def returnPetName (self, id):
        query = "SELECT name FROM tblpet WHERE petID = %s"
        values = (id)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result
    
    def returnPetData (self):
        self.cursor.execute("SELECT * FROM tblpet")
        result = self.cursor.fetchall()
        return result 
    
#----------------------------------------------------------------------------------------------
class Service:

    def __init__(self):
        self.columns = ['ID', 'Name', 'Cost']
        self.cursor = connection.cursor(buffered=True)

    #generate Random Unique ID
    def generateID (self):
        query = "SELECT serviceID FROM tblservice"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        id = random.randint(1000, 9999)
        for x in result:
            if id == x[0]:
                id = random.randint(1000, 9999)
        return id
    
    #check if ID exists
    def checkServiceID (self, serviceID):
        query = "SELECT serviceID FROM tblservice"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if self.cursor.fetchone():
                return True
        return False
    
    #add
    def addService (self, id, name, cost): 
        query = "INSERT INTO tblservice (serviceID, name, cost) VALUES (%s, %s, %s)"
        values = (id, name, cost)
        self.cursor.execute(query, values)
        connection.commit()
        print("Service added.")

    #delete
    def deleteService (self, id):
        query = "DELETE FROM tblservice WHERE serviceID = %s"
        values = (id,)
        self.cursor.execute(query, values)
        connection.commit()
        print("Service deleted.")

    #update
    def updateService (self, unique_key, column, new_value):
        update_query = f"UPDATE tblservice SET `{column}`= %s where `serviceID` = %s"
        print (column)
        self.cursor.execute(update_query, (new_value, unique_key))
        connection.commit()
        print(f"Row updated successfully: {unique_key} with new change: {new_value}")
    
    #search
    def searchService (self, value):
        value = str(value).lower() + '%'
        self.cursor.execute("SELECT * FROM tblservice WHERE LOWER(`serviceID`) LIKE %s OR LOWER(`name`) LIKE %s OR LOWER(`cost`) LIKE %s", 
                    (f"%{value}", f"%{value}", f"%{value}"))
        searchResults = self.cursor.fetchall()
        
        for x in searchResults:
            print(x)
        return searchResults

    #return service data
    def returnServiceData (self):
        self.cursor.execute("SELECT * FROM tblservice")
        result = self.cursor.fetchall()
        return result 
    
    #return names in name column
    def returnServiceNames (self):
        self.cursor.execute("SELECT `name` FROM tblservice")
        result = self.cursor.fetchall()
        service_names = [str(name[0]) for name in result]
        return service_names
    
    
ownerObject = Owner()
petObject = Pet()
servObject = Service()
appObject = Appointment()
