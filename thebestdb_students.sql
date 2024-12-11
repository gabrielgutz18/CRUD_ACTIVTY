-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: thebestdb
-- ------------------------------------------------------
-- Server version	8.0.40

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
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `program` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Gabriel Luigi M. Gutierrez',21,'BSCPE'),(2,'John Anthony U. Lontoc',21,'BSCPE'),(3,'Jeorge Assis A. Malabanan',23,'BSCPE'),(4,'James Kian I. Don',21,'BSCPE'),(5,'Ericka G. Villena',35,'BSCPE'),(6,'Amiela A. Artillaga',37,'BSCPE'),(7,'John Paul L. Vibal',30,'BSCPE'),(8,'Jay Ar M. Macalintal',29,'BSCPE'),(9,'Johndel Brian Matalog',69,'BSCPE'),(10,'Mark Jhon Aurinto',28,'BSCPE'),(11,'Gian Francis Hachachoco',60,'BSCPE'),(12,'David Marasigan',20,'BSCPE'),(13,'Dety Pagsinuhin',20,'BSCPE'),(14,'King Arthur Ragayday',21,'BSCPE'),(15,'Lennard Monteiro',23,'BSCPE'),(16,'Darren Ishi A. Doctora',30,'BSCPE'),(17,'Aira Loraine De Castro',20,'BSCPE'),(18,'Loraine Tarlac',21,'BSCPE'),(19,'Rhea Mendoza',21,'BSCPE'),(20,'Rafael Leyson',22,'BSCPE'),(22,'Josep Dimatibag',24,'BSIT'),(23,'Jeric Hernandez',22,'BSCPE');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-12  4:57:29
