import mysql.connector
import random

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

#
#
# galibog pa ko unsaon pagbutang sa Services Availed
# unsaon pagkabako sa connection sa service na nakuha sa Pet 
# sa appointment_service?
# tas checkan pd niya ang appointmentID sa appointment_service to
# retrieve yung petID at ownerID?
# if mag match kay ibutang sa list?
# pero unsaon add 
#
#

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
    def returnOwner (self, id):
        query = "SELECT name FROM tblowner WHERE ownerID = %s"
        values = (id)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result
    
# -----------------------------------------------------------------------------------------   
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
    def returnPet (self, id):
        query = "SELECT name FROM tblpet WHERE petID = %s"
        values = (id)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result
 
# -----------------------------------------------------------------------------------------   
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
        id = self.generateID() #?
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
    def returnService (self):
        self.cursor.execute("SELECT * FROM tblservice")
        result = self.cursor.fetchall()
        return result
    
# -----------------------------------------------------------------------------------------   
class Appointment:

    def __init__(self):
        self.columns = ['ID', 'Date', 'Time', 'Avail Type', 'Status', 'Pet ID', 'Service ID'] #Pet ID and Service ID are foreign keys
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
    def addAppointment (self, id, date, time, availType, status, petID, serviceID):
        #generate appointmentID
        id = self.generateID() #?

        #if serviceID and petID does not exists
        if Pet.checkPetID(petID) == False & Service.checkServiceID(serviceID) == False:
            # generate petID
            idPet = Pet.generateID()
            petID = idPet
            # insert idPet to tblpet petID
            query = "INSERT INTO tblpet (petID) VALUES (%s)"
            values = (idPet)
            self.cursor.execute(query, values)
            connection.commit()

            # generate serviceID
            idService = Service.generateID()
            serviceID = idService
            # insert idService to tblservice serviceID
            query = "INSERT INTO tblservice (serviceID) VALUES (%s)"
            values = (idService)
            self.cursor.execute(query, values)
            connection.commit()

        #if serviceID exists but petID does not exists
        elif self.checkPetID(petID) == False & self.checkServiceID(serviceID):
            # generate petID
            idPet = Pet.generateID()
            petID = idPet
            # insert idPet to tblpet petID
            query = "INSERT INTO tblpet (petID) VALUES (%s)"
            values = (idPet)
            self.cursor.execute(query, values)
            connection.commit()
        
        #if serviceID does not exists but petID exists
        elif self.checkPetID(petID) & self.checkServiceID(serviceID) == False:
            # generate serviceID
            idService = Service.generateID()
            serviceID = idService
            # insert idService to tblservice serviceID
            query = "INSERT INTO tblservice (serviceID) VALUES (%s)"
            values = (idService)
            self.cursor.execute(query, values)
            connection.commit()

        #if serviceID and petID exists
        else:
            pass

        query = "INSERT INTO tblappointment_history (appointmentID, date, time, availType, status, petID, serviceID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (id, date, time, availType, status, petID, serviceID)
        self.cursor.execute(query, values)
        connection.commit()
        print("Appointment added.")

    #delete (delete information then delete from appHistory)
    def deleteAppointment (self, id):  
        query = "DELETE FROM tblappointment_history WHERE appointmentID = %s"
        values = (id)
        self.cursor.execute(query, values)
        connection.commit()
        print("Appointment deleted.")

    #delete when Status:Pending
    def deletePendingAppointment (self, id):
        query = "DELETE FROM tblappointment_history WHERE appointmentID = %s AND status = 'Pending'"
        values = (id)
        self.cursor.execute(query, values)
        connection.commit()
        print("Appointment deleted.")
    
    #delete when Status:Cancelled
    def deleteCancelledAppointment (self, id):
        query = "DELETE FROM tblappointment_history WHERE appointmentID = %s AND status = 'Cancelled'"
        values = (id)
        self.cursor.execute(query, values)
        connection.commit()
        print("Appointment deleted.")

    #update (update information then update appHistory)
    def updateAppointment (self, id, date, time, availType, status):  
        query = "UPDATE tblappointment_history SET date = %s, time = %s, availType = %s, status = %s WHERE appointmentID = %s"
        values = (date, time, availType, status, id)
        self.cursor.execute(query, values)
        connection.commit()
        print("Appointment updated.")

    #display (display all appointments)
    def displayAppointment (self):
        self.cursor.execute("SELECT * FROM tblappointment_history")
        result = self.cursor.fetchall()
        return result

    #search
    def searchAppointment (self, id):
        query = "SELECT * FROM tblappointment_history WHERE appointmentID = %s"
        values = (id)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result

    #return History (return all appointments)
    def returnAppointment (self):
        self.cursor.execute("SELECT * FROM tblappointment_history")
        result = self.cursor.fetchall()
        return result
    
    #return all data from tblappointment_history, tblowner, tblservice (excluding IDs that are already in the appointment history)
    def returnAppointmentData (self):
        query = "SELECT tblappointment_history.appointmentID, tblappointment_history.date, tblappointment_history.time, tblappointment_history.availType, tblappointment_history.status, tblpet.name, tblpet.species, tblpet.breed, tblowner.name, tblowner.phoneNumber, tblservice.name FROM tblappointment_history INNER JOIN tblpet ON tblappointment_history.petID = tblpet.petID INNER JOIN tblowner ON tblpet.ownerID = tblowner.ownerID INNER JOIN tblservice ON tblappointment_history.serviceID = tblservice.serviceID"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    
    #return status
    def returnStatus (self, id):
        query = "SELECT status FROM tblappointment_history WHERE id = %s"
        values = (id)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result
    
    #return Status:Pending appointment
    def returnPendingAppointment (self):
        query = "SELECT * FROM tblappointment_history WHERE status = 'Pending'"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

# -----------------------------------------------------------------------------------------   
class Appointment_Service:
    def __init__(self):
        self.columns = ['Appointment ID','Service ID'] #Appointment ID and Service ID are foreign keys
        self.cursor = connection.cursor(buffered=True)

    #add foreign IDs from tblAppointment (for Appointment ID) and tblService (for Service ID)
    def addAppointment_Service (self, appointmentID, serviceID):
        query = "INSERT INTO tblappointment_service (appointmentID, serviceID) VALUES (%s, %s)"
        values = (appointmentID, serviceID)
        self.cursor.execute(query, values)
        connection.commit()
        print("Appointment Service added.")


appObject = Appointment()
servObject = Service()
