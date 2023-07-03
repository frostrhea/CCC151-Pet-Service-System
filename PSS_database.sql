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
  KEY `petID_idx` (`petID`),
  KEY `ownerIDforeign_idx` (`ownerID`),
  CONSTRAINT `ownerIDforeign` FOREIGN KEY (`ownerID`) REFERENCES `tblowner` (`ownerID`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `petIDforeign` FOREIGN KEY (`petID`) REFERENCES `tblpet` (`petID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblappointment_history`
--

LOCK TABLES `tblappointment_history` WRITE;
/*!40000 ALTER TABLE `tblappointment_history` DISABLE KEYS */;
INSERT INTO `tblappointment_history` VALUES (4875,'2000-01-01','00:00:00','Reservation','Pending',1150,4344);
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
  `serviceID` varchar(12) NOT NULL,
  PRIMARY KEY (`appointmentID`,`serviceID`),
  KEY `servforeignID_idx` (`serviceID`),
  CONSTRAINT `appforeignID` FOREIGN KEY (`appointmentID`) REFERENCES `tblappointment_history` (`appointmentID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `servforeignID` FOREIGN KEY (`serviceID`) REFERENCES `tblservice` (`serviceID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblappointment_service`
--

LOCK TABLES `tblappointment_service` WRITE;
/*!40000 ALTER TABLE `tblappointment_service` DISABLE KEYS */;
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
  `phoneNumber` char(11) DEFAULT NULL,
  UNIQUE KEY `idtblOwner_UNIQUE` (`ownerID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblowner`
--

LOCK TABLES `tblowner` WRITE;
/*!40000 ALTER TABLE `tblowner` DISABLE KEYS */;
INSERT INTO `tblowner` VALUES (1842,'',''),(2182,'d','d'),(3641,'',''),(4226,'c','c'),(4344,'',''),(6236,'Rey','09278672460');
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
  KEY `ownerIDForeign_idx` (`ownerID`),
  CONSTRAINT `ownIDforeign` FOREIGN KEY (`ownerID`) REFERENCES `tblowner` (`ownerID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblpet`
--

LOCK TABLES `tblpet` WRITE;
/*!40000 ALTER TABLE `tblpet` DISABLE KEYS */;
INSERT INTO `tblpet` VALUES (1150,'','','',4344),(2497,'','','',1842),(2586,'da','dd','dd',2182),(2974,'c','c','c',4226),(3291,'Perry','Dog','Belgian',6236),(4625,'','','',3641);
/*!40000 ALTER TABLE `tblpet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tblservice`
--

DROP TABLE IF EXISTS `tblservice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tblservice` (
  `serviceID` varchar(12) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `cost` double DEFAULT NULL,
  PRIMARY KEY (`serviceID`),
  UNIQUE KEY `serviceID_UNIQUE` (`serviceID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tblservice`
--

LOCK TABLES `tblservice` WRITE;
/*!40000 ALTER TABLE `tblservice` DISABLE KEYS */;
INSERT INTO `tblservice` VALUES ('1435','Cat Trimming',100);
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

-- Dump completed on 2023-07-04  4:54:26
