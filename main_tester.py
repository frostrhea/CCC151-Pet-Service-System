from appointment import Appointment, Service, Owner, Pet, Appointment_Service


def main():

    service = Service()
    owner = Owner()
    pet = Pet() 
    appointment = Appointment()
    appointment_service = Appointment_Service()

    #service.addService('','Trim','100')
    appointment.addAppointment('2023-07-04','12:05','Reservation','Pending','Rango','Dog', 'Aspin', 'Gel', '09978101451')
 
    
main()

#new