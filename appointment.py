import mysql.connector
import random

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="gag0p1n4s",
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
    
    # check if all owner details exists in tblowner by owner name
    def checkOwner (self, name, phoneNum):
        query = "SELECT * FROM tblowner WHERE name = %s AND phoneNumber = %s"
        values = (name, phoneNum)
        self.cursor.execute(query, values)
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
    def returnOwner (self, id):
        query = "SELECT name FROM tblowner WHERE ownerID = %s"
        values = (id)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result
    
    #return owner ID by name and phone number
    def returnOwnerID (self, name, phoneNum):
        query = "SELECT ownerID FROM tblowner WHERE name = %s AND phoneNumber = %s"
        values = (name, phoneNum)
        self.cursor.execute(query, values)
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
        

    # check if all pet details exists in tblpet by pet name
    def checkPet (self, name, species, breed):
        query = "SELECT * FROM tblpet WHERE name = %s AND species = %s AND breed = %s"
        values = (name, species, breed)
        self.cursor.execute(query, values)
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
    def returnPet (self, id):
        query = "SELECT name FROM tblpet WHERE petID = %s"
        values = (id)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result
    
    #return pet ID by pet name and pet breed and species
    def returnPetID (self, name, species, breed):
        query = "SELECT petID FROM tblpet WHERE name = %s AND species = %s AND breed = %s"
        values = (name, species, breed)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result
    
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
        id = self.generateID() #?
        query = "INSERT INTO tblservice (serviceID, name, cost) VALUES (%s, %s, %s)"
        values = (id, name, cost)
        self.cursor.execute(query, values)
        connection.commit()
        print("Service added.")
        return id


    #delete
    def deleteService (self, id):
        query = "DELETE FROM tblservice WHERE serviceID = %s"
        values = (id)
        self.cursor.execute(query, values)
        connection.commit()
        print("Service deleted.")

    #update
    def updateService (self, id, name, cost):
        query = "UPDATE tblservice SET name = %s, cost = %s WHERE serviceID = %s"
        values = (name, cost, id)
        self.cursor.execute(query, values)
        connection.commit()
        print("Service updated.")

    #display  
    def displayService (self):    
        self.cursor.execute("SELECT * FROM tblservice")
        result = self.cursor.fetchall()
        for x in result:
            print(x)  

    #search
    def searchService (self, id):
        query = "SELECT * FROM tblservice WHERE serviceID = %s"
        values = (id)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        for x in result:
            print(x)

    #return service data
    def returnService (self):
        self.cursor.execute("SELECT * FROM tblservice")
        result = self.cursor.fetchall()
        return result
    
    #return service cost
    def returnCost (self, id):
        query = "SELECT cost FROM tblservice WHERE serviceID = %s"
        values = (id)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result
    
    #return service id when given service name
    def returnID(self, names):
        query = "SELECT serviceID FROM tblservice WHERE name = %s"
        results = []

        for name in names:
            self.cursor.execute(query, (name,))
            result = self.cursor.fetchall()
            results.extend(result)

        return results
 

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
    def addAppointment (self, date, time, availType, status, petName, petSpecies, petBreed, ownerName, phoneNum, serviceName):
        #generate appointmentID
        id = self.generateID() #?
        
        # check if owner and pet exists
        if ownerObject.checkOwner(ownerName, phoneNum) & petObject.checkPet(petName, petSpecies, petBreed):
            ownerID = ownerObject.returnOwnerID(ownerName, phoneNum) 
            petID = petObject.returnPetID(petName, petSpecies, petBreed)

        # check if owner exists but pet does not
        elif ownerObject.checkOwner(ownerName, phoneNum) & (not petObject.checkPet(petName, petSpecies, petBreed)):
            ownerID = ownerObject.returnOwnerID(ownerName, phoneNum)
            petID = petObject.addPet(petName, petSpecies, petBreed, ownerID)
        
        #check if pet exists but owner does not
        elif (not ownerObject.checkOwner(ownerName, phoneNum)) & petObject.checkPet(petName, petSpecies, petBreed):
            ownerID = ownerObject.addOwner(ownerName, phoneNum)
            petID = petObject.returnPetID(petName, petSpecies, petBreed)
        
        #check if neither owner nor pet exists
        else:
            ownerID = ownerObject.addOwner(ownerName, phoneNum)
            petID = petObject.addPet(petName, petSpecies, petBreed, ownerID)

        #get serviceID
        serviceIDs = []
        for serviceName in serviceName:
            serviceID = serviceObject.returnID(serviceName)
            serviceIDs.extend(serviceID) 

        #insert into tblappointment_history
        query = "INSERT INTO tblappointment_history (appointmentID, date, time, availType, status, petID, ownerID) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (id, date, time, availType, status, petID, ownerID)
        self.cursor.execute(query, values)
        connection.commit()
        print("Appointment added.")

        #add to tblappointment_service
        serviceIDs = [x[0] for x in serviceIDs]

        query = "INSERT INTO tblappointment_service (appointmentID, serviceID) VALUES (%s, %s)"
        values = [(id, x) for x in serviceIDs]
     
        self.cursor.executemany(query, values)
        connection.commit()
        
        print("Appointment_Service added.")

    #delete (delete information then delete from appHistory)
    def deleteAppointment (self, id):  
        query = "DELETE FROM tblappointment_history WHERE appointmentID = %s"
        values = (id)
        self.cursor.execute(query, values)
        connection.commit()
        print("Appointment deleted.")
        servappObject.deleteAppointment_Service(id)

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
    
    #return Status:Cancelled appointment
    def returnCancelledAppointment (self):
        query = "SELECT * FROM tblappointment_history WHERE status = 'Cancelled'"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    
    #return Status:Completed appointment
    def returnCompletedAppointment (self):
        query = "SELECT * FROM tblappointment_history WHERE status = 'Completed'"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result


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

    #loop display service name by appointmentID
    def displayServiceByAppointment (self, appointmentID):
        query = "SELECT tblservice.name FROM tblservice INNER JOIN tblappointment_service ON tblservice.serviceID = tblappointment_service.serviceID WHERE tblappointment_service.appointmentID = %s"
        values = (appointmentID)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result
    
    #delete row by appointment ID
    def deleteAppointment_Service (self, appointmentID):
        query = "DELETE FROM tblappointment_service WHERE appointmentID = %s"
        values = (appointmentID)
        self.cursor.execute(query, values)
        connection.commit()
        print("Appointment Service deleted.")

ownerObject = Owner()
petObject = Pet()
serviceObject = Service()
servappObject = Appointment_Service()