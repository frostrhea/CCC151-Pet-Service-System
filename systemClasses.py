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
        self.columns = ['App ID', 'Date', 'Time', 'Avail Type', 'Status', 'Pet Name', 'Owner Name', 'App ID', 'Service Availed'] #Pet ID and Service ID are foreign keys
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
    def addAppointment(self, petName, petSpecies, petBreed, ownerName, phoneNum, date, time, availType, status, serviceNames):
        # generate appointmentID
        id = self.generateID()  # ?

        owner = ownerObject.checkOwner(ownerName, phoneNum)
        pet = petObject.checkPet(petName, petSpecies, petBreed)

        # check if owner and pet exists
        if owner and pet:
            ownerID = ownerObject.returnOwnerID(ownerName, phoneNum) 
            petID = petObject.returnPetID(petName, petSpecies, petBreed)

        # check if owner exists but pet does not
        if owner and not pet:
            ownerID = ownerObject.returnOwnerID(ownerName, phoneNum)
            petID = petObject.addPet(petName, petSpecies, petBreed, ownerID)
        
        #check if neither owner nor pet exists
        if not owner and not pet:
            ownerID = ownerObject.addOwner(ownerName, phoneNum)
            petID = petObject.addPet(petName, petSpecies, petBreed, ownerID)


        date_obj = datetime.datetime.strptime(date, '%d/%m/%Y')
        date = date_obj.strftime('%Y-%m-%d')
        time_obj = datetime.datetime.strptime(time, '%I:%M %p')
        time = time_obj.strftime('%H:%M')

        # Get service IDs
        serviceIDs = []
        for serviceName in serviceNames:
            serviceID = servObject.returnID(serviceName)
            if serviceID:
                serviceIDs.append(serviceID[0])
            else:
                print(f"Service ID not found for service name: {serviceName}")

        # insert into tblappointment_history
        query = "INSERT INTO tblappointment_history (appointmentID, date, time, availType, status, petID, ownerID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        value = (id, date, time, availType, status, petID, ownerID)
        print(value)
        self.cursor.execute(query, value)
        connection.commit()
        print("Appointment added.")

        # add to tblappointment_service
        serviceIDs = [x[0] for x in serviceIDs]
        query = "INSERT INTO tblappointment_service (appointmentID, serviceID) VALUES (%s, %s)"
        values = [(id, x) for x in serviceIDs]
        self.cursor.executemany(query, values)
        connection.commit()
        print("Appointment_Service added.")
        
        
    def deleteAppointment (self, id):  
        query = "DELETE FROM tblappointment_history WHERE appointmentID = %s"
        values = (id,)
        self.cursor.execute(query, values)
        connection.commit()
        print("Appointment deleted.")
    
    #done
    def searchAppointment (self, value):
        value = '%' + str(value).lower() + '%'
        self.cursor.execute("""
                    SELECT ah.appointmentID, ah.date, ah.time, ah.availType, ah.status, p.name, o.name, a.appointmentID, s.name
                    FROM tblappointment_history ah
                    INNER JOIN tblappointment_service a ON ah.appointmentID = a.appointmentID
                    INNER JOIN tblpet p ON ah.petID = p.petID
                    INNER JOIN tblservice s ON a.serviceID = s.serviceID
                    INNER JOIN tblowner o ON ah.ownerID = o.ownerID
                    WHERE LOWER(ah.appointmentID) LIKE %s
                    OR LOWER(ah.date) LIKE %s
                    OR LOWER(ah.time) LIKE %s
                    OR LOWER(ah.availType) LIKE %s
                    OR LOWER(ah.status) LIKE %s
                    OR LOWER(p.name) LIKE %s
                    OR LOWER(o.name) LIKE %s
                    OR LOWER(s.name) LIKE %s
                """, 
                    (f"{value}", f"{value}", f"{value}", f"{value}", f"{value}", f"{value}", f"{value}", f"{value}"))
        searchResults = self.cursor.fetchall()
        
        for x in searchResults:
            print(x)
        return searchResults
    
    #update
    def updateAppointment(self, unique_key, column, new_value):
        update_query = ""
        
        if column == "Service ID":
            update_query = f"UPDATE `tblappointment_service` SET `serviceID` = %s WHERE `appointmentID` = %s"
        else: 
            update_query = f"UPDATE `tblappointment_history` SET `{column.lower()}` = %s WHERE `appointmentID` = %s"

        self.cursor.execute(update_query, (new_value, unique_key))
        connection.commit()
        print(f"Row updated successfully: {unique_key} with new change: {new_value}")
    
    #return History (return all appointments)
    def returnAppointmentData (self):
        #self.cursor.execute("SELECT * FROM tblappointment_history ah INNER JOIN tblappointment_service s ON ah.appointmentID = s.appointmentID")
        self.cursor.execute("""
                    SELECT ah.appointmentID, ah.date, ah.time, ah.availType, ah.status, p.name, o.name, a.appointmentID, s.name
                    FROM tblappointment_history ah
                    INNER JOIN tblappointment_service a ON ah.appointmentID = a.appointmentID
                    INNER JOIN tblpet p ON ah.petID= p.petID
                    INNER JOIN tblservice s ON a.serviceID = s.serviceID
                    INNER JOIN tblowner o ON ah.ownerID = o.ownerID
                    ORDER BY ah.date DESC, ah.time DESC
                """)
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
        values = (id, )
        self.cursor.execute(query, values)
        connection.commit()
        print("Owner deleted.")

    #update
    def updateOwner (self, unique_key, column, new_value):
        update_query = f"UPDATE tblowner SET `{column}`= %s where `ownerID` = %s"
        #print (column)
        self.cursor.execute(update_query, (new_value, unique_key))
        connection.commit()
        print(f"Row updated successfully: {unique_key} with new change: {new_value}")

    #display
    def displayOwner (self):
        self.cursor.execute("SELECT * FROM tblowner")
        result = self.cursor.fetchall()
        return result

    #search
    def searchOwner(self, value):
        value = str(value).lower() + '%'
        self.cursor.execute("SELECT * FROM tblowner WHERE LOWER(`ownerID`) LIKE %s OR LOWER(`name`) LIKE %s OR LOWER(`phoneNumber`) LIKE %s", 
                    (f"%{value}", f"%{value}", f"%{value}"))
        searchResults = self.cursor.fetchall()
        
        for x in searchResults:
            print(x)
        return searchResults 

    #return Owner name
    def returnOwnerName (self, id):
        query = "SELECT name FROM tblowner WHERE ownerID = %s"
        values = (id)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result
    
    def checkOwnerExists (self, name):
        query = "SELECT name FROM tblowner WHERE name = %s"
        value = (name,)
        self.cursor.execute(query, value)
        if self.cursor.fetchone():
            return True 
        else:
            return False
        
    
    def returnOwnerData (self):
        self.cursor.execute("SELECT * FROM tblowner")
        result = self.cursor.fetchall()
        return result 
    
    #return owner ID by name and phone number
    def returnOwnerID (self, name, phoneNum):
        query = "SELECT ownerID FROM tblowner WHERE name = %s AND phoneNumber = %s"
        values = (name, phoneNum)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()
        if result:
            ownerID = result[0]
            return ownerID
        else:
            return None 
    
    # check if all owner details exists in tblowner by owner name and number
    def checkOwner (self, name, phoneNum):
        query = "SELECT * FROM tblowner WHERE name = %s AND phoneNumber = %s"
        values = (name, phoneNum)
        self.cursor.execute(query, values)
        if self.cursor.fetchone():
                return True
        return False
    
    
  
class Pet:

    def __init__(self):
        self.columns = [ 'ID', 'Name', 'Species', 'Breed', 'Owner Name'] #Owner ID is foreign key
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
        values = (id, )
        self.cursor.execute(query, values)
        connection.commit()
        print("Pet deleted.")

    #update
    def updatePet(self, unique_key, column, new_value):
        if column == "Owner Name":
            update_query = f"UPDATE `tblpet` SET `ownerID` = (SELECT `ownerID` FROM `tblowner` WHERE `name` = %s) WHERE `petID` = %s"
        else:
            update_query = f"UPDATE `tblpet` SET `{column}` = %s WHERE `petID` = %s"
            
        self.cursor.execute(update_query, (new_value, unique_key))
        connection.commit()
        print(f"Row updated successfully: {unique_key} with new change: {new_value}")



    #display
    def displayPet (self):
        self.cursor.execute("SELECT * FROM tblpet")
        result = self.cursor.fetchall()
        return result

    #search
    def searchPet(self, value):
        value = str(value).lower() + '%'
        self.cursor.execute("""
            SELECT p.petID, p.name, p.species, p.breed, o.name 
            FROM tblpet p 
            INNER JOIN tblowner o ON p.ownerID = o.ownerID
            WHERE LOWER(p.petID) LIKE %s
            oR LOWER(p.name) LIKE %s 
            OR LOWER(p.species) LIKE %s 
            OR LOWER(p.breed) LIKE %s 
            OR LOWER(o.name) LIKE %s
        """, (f"%{value}", f"%{value}", f"%{value}", f"%{value}", f"%{value}"))
        searchResults = self.cursor.fetchall()
        
        for x in searchResults:
            print(x)
        return searchResults


    #return pet name
    def returnPetName (self):
        self.cursor.execute("SELECT name FROM tblpet")
        result = self.cursor.fetchall()
        pet_names = [str(name[0]) for name in result]
        return pet_names
    
    def returnPetData (self):
        self.cursor.execute("SELECT p.petID, p.name, p.species, p.breed, COALESCE(o.name, NULL) FROM tblpet p LEFT JOIN tblowner o ON p.ownerID = o.ownerID")
        #self.cursor.execute("SELECT p.petID, p.name, p.species, p.breed, o.name FROM tblpet p INNER JOIN tblowner o ON p.ownerID = o.ownerID")
        result = self.cursor.fetchall()
        return result 
    
    # Get the ownerID corresponding to the petID
    def getOwnerID(self, petID):
        self.cursor.execute("SELECT ownerID FROM tblpet WHERE petID = %s", (petID,))
        result = self.cursor.fetchone()
        if result is not None:
            owner_id = result[0]
        return owner_id
    
    #return pet ID by pet name and pet breed and species
    def returnPetID(self, name, species, breed):
        query = "SELECT petID FROM tblpet WHERE name = %s AND species = %s AND breed = %s"
        values = (name, species, breed)
        self.cursor.execute(query, values)
        result = self.cursor.fetchone()  # Use fetchone() to retrieve a single row
        if result:
            return result[0]  # Access the first element of the tuple
        return None  # Handle case when no petID is found
        

    # check if all pet details exists in tblpet by pet name
    def checkPet (self, name, species, breed):
        query = "SELECT * FROM tblpet WHERE name = %s AND species = %s AND breed = %s"
        values = (name, species, breed)
        self.cursor.execute(query, values)
        if self.cursor.fetchone():
                return True
        return False
    
    def checkPetExists(self, name):
        query = "SELECT name FROM tblpet WHERE name = %s"
        value = (name,)
        self.cursor.execute(query, value)
        if self.cursor.fetchone():
            return True 
        else:
            return False
        
    def getPetDataFromSelectedPet(self, selected_pet):
        query = '''
            SELECT p.name, p.species, p.breed, o.name, o.phoneNumber
            FROM tblpet p
            INNER JOIN tblowner o ON p.ownerID = o.ownerID
            WHERE p.name = %s
        '''
        self.cursor.execute(query, (selected_pet,))
        result = self.cursor.fetchone()
        print(result)
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
    def addService (self, name, cost): 
        id = self.generateID()
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
        #print (column)
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
        self.cursor.execute("SELECT * FROM tblservice ORDER BY `name` ASC")
        result = self.cursor.fetchall()
        return result 
    
    #return names in name column
    def returnServiceNames (self):
        self.cursor.execute("SELECT `name` FROM tblservice ORDER BY `name` ASC")
        result = self.cursor.fetchall()
        service_names = [str(name[0]) for name in result]
        return service_names
    
    #return service id when given service name
    def returnID(self, names):
        query = "SELECT serviceID FROM tblservice WHERE name = %s"
        results = []

        if isinstance(names, str):
            # Handle a single name
            self.cursor.execute(query, (names,))
            results = self.cursor.fetchall()
        elif isinstance(names, list):
            # Handle a list of names
            self.cursor.executemany(query, [(name,) for name in names])
            results = self.cursor.fetchall()

        return results



    
ownerObject = Owner()
petObject = Pet()
servObject = Service()
appObject = Appointment()
