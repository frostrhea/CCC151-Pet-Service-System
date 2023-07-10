CREATE DATABASE  IF NOT EXISTS `dbpetservice` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `dbpetservice`;
-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: dbpetservice
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `tblappointment_history`
--

DROP TABLE IF EXISTS `tblappointment_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblappointment_history` (
  `appointmentID` int NOT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `availType` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `petID` int DEFAULT NULL,
  `ownerID` int DEFAULT NULL,
  PRIMARY KEY (`appointmentID`),
  UNIQUE KEY `appointmentID_UNIQUE` (`appointmentID`),
  KEY `petIDforeign_idx` (`petID`),
  KEY `ownerIDforeign_idx` (`ownerID`),
  CONSTRAINT `ownerIDforeign` FOREIGN KEY (`ownerID`) REFERENCES `tblowner` (`ownerID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `petIDforeign` FOREIGN KEY (`petID`) REFERENCES `tblpet` (`petID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblappointment_history`
--

LOCK TABLES `tblappointment_history` WRITE;
/*!40000 ALTER TABLE `tblappointment_history` DISABLE KEYS */;
INSERT INTO `tblappointment_history` VALUES (1090,'2002-01-01','09:00:00','Walk-in','Canceled',3027,9233),(1205,'2023-04-01','14:00:00','Walk-in','Canceled',8118,6375),(1431,'2023-07-10','15:00:00','Walk-in','Completed',3027,9233),(1486,'2004-01-04','13:00:00','Reservation','Pending',8157,6020),(1664,'2023-07-04','12:05:00','Reservation','Pending',6019,2167),(1899,'2023-07-01','09:00:00','Walk-in','Completed',2288,6375),(1921,'2023-01-01','12:00:00','Reservation','Pending',6376,6375),(2139,'2006-01-01','12:00:00','Reservation','Pending',2392,6020),(2260,'2023-07-04','12:05:00','Reservation','Pending',6019,2167),(2580,'2023-07-09','10:00:00','Walk-in','Completed',2118,9826),(3176,'2021-01-01','12:00:00','Reservation','Pending',8455,7159),(3996,'2005-01-01','12:00:00','Walk-in','Pending',2392,6020),(4081,'2023-07-06','09:00:00','Reservation','Canceled',2288,6375),(4084,'2002-01-01','15:00:00','Walk-in','Completed',1795,9233),(4499,'2000-01-03','02:00:00','Reservation','Pending',2392,6020),(4559,'2023-07-10','09:00:00','Reservation','Pending',6746,8295),(4732,'2008-01-01','12:00:00','Reservation','Pending',2561,6020),(4980,'2023-07-07','10:00:00','Reservation','Completed',6019,2167),(5002,'2007-01-01','14:00:00','Reservation','Pending',2392,6020),(6237,'2000-01-02','01:00:00','Reservation','Pending',2392,6020),(6590,'2021-01-01','13:00:00','Reservation','Canceled',7107,7159),(6618,'2023-07-04','12:05:00','Reservation','Pending',6019,2167),(7246,'2005-01-02','12:00:00','Reservation','Completed',2392,6020),(7674,'2000-01-04','12:00:00','Reservation','Pending',2392,6020),(8368,'2004-01-01','14:00:00','Walk-in','Canceled',3604,6020),(8405,'2005-01-03','13:00:00','Walk-in','Completed',2392,6020),(8600,'2023-07-10','14:00:00','Reservation','Completed',7636,6274),(8648,'2000-01-04','15:00:00','Reservation','Pending',2392,6020),(8774,'2005-01-05','13:04:00','Walk-in','Completed',2561,6020),(9079,'2000-01-03','02:00:00','Reservation','Pending',2392,6020);
/*!40000 ALTER TABLE `tblappointment_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblappointment_service`
--

DROP TABLE IF EXISTS `tblappointment_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblappointment_service` (
  `appointmentID` int NOT NULL,
  `serviceID` int NOT NULL,
  PRIMARY KEY (`appointmentID`,`serviceID`),
  KEY `servforeignID_idx` (`serviceID`),
  CONSTRAINT `appforeignID` FOREIGN KEY (`appointmentID`) REFERENCES `tblappointment_history` (`appointmentID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `servforeignID` FOREIGN KEY (`serviceID`) REFERENCES `tblservice` (`serviceID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblappointment_service`
--

LOCK TABLES `tblappointment_service` WRITE;
/*!40000 ALTER TABLE `tblappointment_service` DISABLE KEYS */;
INSERT INTO `tblappointment_service` VALUES (1431,1178),(2580,2988),(1090,3767),(3176,3767),(4980,3767),(6590,3767),(8600,3767),(1431,4166),(4559,4166),(4559,4247),(4559,4354),(1090,5449),(3176,5449),(4732,5449),(4980,5449),(8600,5449),(8774,5449),(1205,7344),(1921,7344),(3996,7344),(2580,8342),(1205,9615),(1899,9615),(1921,9615),(3996,9615),(4081,9615),(1899,9998);
/*!40000 ALTER TABLE `tblappointment_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblowner`
--

DROP TABLE IF EXISTS `tblowner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblowner` (
  `ownerID` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `phoneNumber` char(11) NOT NULL,
  PRIMARY KEY (`ownerID`),
  UNIQUE KEY `ownerID_UNIQUE` (`ownerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblowner`
--

LOCK TABLES `tblowner` WRITE;
/*!40000 ALTER TABLE `tblowner` DISABLE KEYS */;
INSERT INTO `tblowner` VALUES (2167,'Gel','09978101451'),(4846,'dsad','dasd'),(6020,'Rhea','09278672460'),(6274,'Venus','09473658734'),(6375,'Lizer','0949326747'),(7159,'daaa','dsad'),(8295,'Mao','09876543211'),(9233,'Abe','093281632'),(9826,'Keena','09123456781');
/*!40000 ALTER TABLE `tblowner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblpet`
--

DROP TABLE IF EXISTS `tblpet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblpet` (
  `petID` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `species` varchar(45) NOT NULL,
  `breed` varchar(45) NOT NULL,
  `ownerID` int DEFAULT NULL,
  PRIMARY KEY (`petID`),
  UNIQUE KEY `petID_UNIQUE` (`petID`),
  KEY `ownIDforeign_idx` (`ownerID`),
  CONSTRAINT `ownIDforeign` FOREIGN KEY (`ownerID`) REFERENCES `tblowner` (`ownerID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblpet`
--

LOCK TABLES `tblpet` WRITE;
/*!40000 ALTER TABLE `tblpet` DISABLE KEYS */;
INSERT INTO `tblpet` VALUES (1795,'Matte','Cat','Puspin',9233),(2118,'Techala','Cat','Domestic Shorthair',9826),(2288,'Bing1','Cat','Puspin',6375),(2392,'Ginger','Cat','Puspin',2167),(2561,'Perry','Dog','Aspin',6020),(3027,'Queenie','Dog','Aspin',9233),(3604,'Memowk','Cat','Puspin',6020),(6019,'Rango','Dog','Aspin',6020),(6376,'Bing','Cat','Puspin',6375),(6746,'Groot','Dog','German Shepherd',8295),(7107,'Blacky','Dog','Doberman',7159),(7636,'Likey','Dog','Chihuahua',6274),(8118,'Mengzz','Cat','Puspin',6375),(8157,'Ginger','Cat ','Puspin',6020),(8455,'Whitey','Dog','Aspin',7159);
/*!40000 ALTER TABLE `tblpet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblservice`
--

DROP TABLE IF EXISTS `tblservice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblservice` (
  `serviceID` int NOT NULL,
  `name` varchar(45) NOT NULL,
  `cost` double NOT NULL,
  PRIMARY KEY (`serviceID`),
  UNIQUE KEY `serviceID_UNIQUE` (`serviceID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblservice`
--

LOCK TABLES `tblservice` WRITE;
/*!40000 ALTER TABLE `tblservice` DISABLE KEYS */;
INSERT INTO `tblservice` VALUES (1178,'Pet Heartworm Test',800),(2988,'Cat Deworming',250),(3767,'Dog Nail Trimming',100),(4166,'Dog Deworming',250),(4247,'Dog Rabies Vaccination',250),(4354,'Dog Ear Cleaning',120),(5449,'Dog Fur Trimming',120),(7344,'Cat Fur Trimming',120),(8342,'Cat Ear Cleaning',120),(9615,'Cat Nail Trimming',100),(9998,'Dog Blah',1200);
/*!40000 ALTER TABLE `tblservice` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-10  9:02:54
