CREATE DATABASE  IF NOT EXISTS `bug_system_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `bug_system_db`;
-- MySQL dump 10.13  Distrib 8.0.33, for macos13 (arm64)
--
-- Host: localhost    Database: bug_system_db
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
-- Table structure for table `Bug`
--

DROP TABLE IF EXISTS `Bug`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Bug` (
  `bugId` int NOT NULL AUTO_INCREMENT,
  `bugPostingDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `custLoginId` varchar(10) NOT NULL,
  `bugStatus` varchar(20) DEFAULT 'New Bug',
  `productName` varchar(45) NOT NULL,
  `bugDesc` text NOT NULL,
  `expertAssignedDate` datetime DEFAULT NULL,
  `expertLoginId` varchar(10) DEFAULT NULL,
  `bugSolvedDate` datetime DEFAULT NULL,
  `solution` text,
  PRIMARY KEY (`bugId`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Bug`
--

LOCK TABLES `Bug` WRITE;
/*!40000 ALTER TABLE `Bug` DISABLE KEYS */;
INSERT INTO `Bug` VALUES (1,'2023-07-06 14:39:38','CU2001','New Bug','Laptop','Screen is flickring','2023-07-06 16:17:29','2',NULL,NULL),(2,'2023-07-06 14:39:43','CU2001','New Bug','Mobile','Keyboard not working.',NULL,NULL,NULL,NULL),(3,'2023-07-06 14:40:24','CU2002','New Bug','Laptop','Wifi connection issues','2023-07-06 21:56:58','2',NULL,NULL),(4,'2023-07-13 14:22:44','CU3004','New Bug','Trackpad not Working','Track pad is not showing the mouse on the screen.',NULL,NULL,NULL,NULL),(5,'2023-07-15 09:30:12','CU4005','New Bug','Mobile','Battery draining too quickly.',NULL,NULL,NULL,NULL),(6,'2023-07-15 10:15:28','CU2001','New Bug','Laptop','Random system crashes.','2023-07-16 14:20:45','2','2023-07-18 11:35:19','Performed system update.'),(7,'2023-07-15 11:05:37','CU3003','New Bug','Mobile','App freezing on launch.',NULL,NULL,NULL,NULL),(8,'2023-07-15 12:20:56','CU2002','New Bug','Laptop','Files not syncing to cloud storage.','2023-07-17 09:45:23','1','2023-07-19 16:10:32','Reconfigured cloud storage settings.'),(9,'2023-07-16 13:50:19','CU4001','New Bug','Mobile','Camera not focusing properly.','2023-07-17 10:55:42','3','2023-07-20 08:25:14','Calibrated camera module.'),(10,'2023-07-16 14:30:28','CU3002','New Bug','Laptop','Slow performance when running multiple applications.','2023-07-17 16:40:55','2','2023-07-19 09:55:31','Performed system cleanup and optimization.'),(11,'2023-07-17 09:10:43','CU2004','New Bug','Mobile','Screen not responding to touch.',NULL,NULL,NULL,NULL),(12,'2023-07-17 10:25:59','CU4002','New Bug','Laptop','Bluetooth connectivity issues.','2023-07-18 13:15:24','1','2023-07-20 10:30:18','Reset Bluetooth settings.'),(13,'2023-07-18 11:40:15','CU3001','New Bug','Mobile','Network signal drops frequently.','2023-07-19 14:05:37','3','2023-07-21 09:20:46','Reconfigured network settings.'),(14,'2023-07-19 13:15:22','CU2003','New Bug','Laptop','External monitor not detected.','2023-07-20 15:30:41','2','2023-07-22 12:40:55','Updated display drivers.'),(15,'2023-07-20 10:35:29','CU3005','New Bug','Mobile','Apps crashing randomly.',NULL,NULL,NULL,NULL),(16,'2023-07-21 09:55:38','CU4003','New Bug','Laptop','Battery not charging.','2023-07-22 11:45:59','1','2023-07-24 10:20:12','Replaced faulty charging cable.'),(17,'2023-07-23 14:30:12','CU2001','New Bug','Laptop','Random system freezes.','2023-07-24 10:15:28','2','2023-07-25 09:05:37','Performed system diagnostics.'),(18,'2023-07-24 09:40:28','CU3003','New Bug','Mobile','App crashes when opening notifications.',NULL,NULL,NULL,NULL),(19,'2023-07-25 12:50:24','CU2002','New Bug','Laptop','Audio not working after software update.','2023-07-26 11:30:44','1','2023-07-28 08:45:21','Reinstalled audio drivers.'),(20,'2023-07-26 11:22:44','CU3004','New Bug','Mobile','Touchscreen unresponsive in certain areas.',NULL,NULL,NULL,NULL),(21,'2023-07-27 15:10:29','CU4005','New Bug','Laptop','Overheating and shutdown during heavy usage.','2023-07-29 09:55:18','2','2023-07-30 14:20:33','Cleaned internal cooling system.'),(22,'2023-07-28 10:35:17','CU2003','New Bug','Mobile','Unable to send/receive text messages.','2023-07-29 12:25:41','3','2023-07-31 10:10:29','Reconfigured network settings.'),(23,'2023-07-29 12:40:55','CU3001','New Bug','Laptop','USB ports not recognizing devices.','2023-07-31 08:15:29','1','2023-08-01 10:30:42','Updated USB drivers.'),(24,'2023-07-30 11:55:42','CU4002','New Bug','Mobile','Battery draining rapidly after software update.',NULL,NULL,NULL,NULL),(25,'2023-07-31 14:20:35','CU2004','New Bug','Laptop','Graphics glitches on external monitor.','2023-08-02 09:35:18','2','2023-08-03 11:50:25','Updated graphics drivers.'),(26,'2023-08-01 16:45:29','CU3002','New Bug','Mobile','Speaker not producing sound.',NULL,NULL,NULL,NULL),(27,'2023-08-02 09:50:15','CU4001','New Bug','Laptop','Apps freezing when using external monitor.','2023-08-04 11:30:29','1','2023-08-05 09:15:37','Resolved compatibility issue.'),(28,'2023-08-03 10:15:22','CU2005','New Bug','Mobile','Mobile data not working.','2023-08-05 14:20:38','3','2023-08-07 10:30:46','Reconfigured APN settings.'),(29,'2023-08-04 11:40:18','CU3003','New Bug','Laptop','Keyboard keys not registering.',NULL,NULL,NULL,NULL),(30,'2023-08-05 13:55:27','CU2002','New Bug','Mobile','Camera app crashing when taking photos.','2023-08-06 10:30:44','2','2023-08-07 09:20:35','Reinstalled camera app.'),(31,'2023-08-06 15:20:29','CU4004','New Bug','Laptop','Random system reboots.','2023-08-08 09:45:18','1','2023-08-09 11:30:22','Performed hardware diagnostics.'),(32,'2023-08-07 10:10:38','CU3001','New Bug','Mobile','GPS not working properly.',NULL,NULL,NULL,NULL),(33,'2023-08-08 14:45:21','CU2005','New Bug','Laptop','Slow performance and lagging.','2023-08-10 09:35:28','2','2023-08-11 10:25:35','Optimized system settings.'),(34,'2023-08-09 11:55:18','CU3004','New Bug','Mobile','Apps not updating properly.','2023-08-10 13:40:29','3','2023-08-12 09:15:37','Cleared app cache and data.'),(35,'2023-08-10 13:30:23','CU4002','New Bug','Laptop','File corruption when transferring via USB.','2023-08-12 08:15:29','1','2023-08-13 10:30:42','Updated USB drivers.'),(36,'2023-08-11 10:45:29','CU2003','New Bug','Mobile','Battery draining even when not in use.',NULL,NULL,NULL,NULL),(37,'2023-08-12 14:20:35','CU3002','New Bug','Laptop','Display flickering intermittently.','2023-08-14 09:35:18','2','2023-08-15 11:50:25','Updated display drivers.'),(38,'2023-08-13 16:45:29','CU2001','New Bug','Mobile','Apps crashing after software update.',NULL,NULL,NULL,NULL),(39,'2023-08-14 09:50:15','CU3005','New Bug','Laptop','Unexpected shutdown during gaming.','2023-08-16 11:30:29','1','2023-08-17 09:15:37','Performed stress tests.'),(40,'2023-08-15 10:15:22','CU2004','New Bug','Mobile','Screen unresponsive to touch input.','2023-08-17 14:20:38','3','2023-08-19 10:30:46','Calibrated touchscreen.');
/*!40000 ALTER TABLE `Bug` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `custLoginId` varchar(10) NOT NULL,
  `custPassword` varchar(20) DEFAULT NULL,
  `custName` varchar(45) DEFAULT NULL,
  `custAge` int DEFAULT NULL,
  `custPhone` varchar(10) DEFAULT NULL,
  `custEmail` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`custLoginId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('CU2001','password','Priya',21,'9998887776','priya@demo.com'),('CU2002','password','Anjali',22,'9998887776','priya@demo.com'),('CU2003','password','Aman',25,'9998887776','aman@demo.com'),('CU2004','password','Rahul',28,'9998887776','rahul@demo.com'),('CU2005','password','Pooja',32,'9998887776','pooja@demo.com'),('CU2006','password','Sneha',27,'9998887776','sneha@demo.com'),('CU2007','password','Vikas',35,'9998887776','vikas@demo.com'),('CU2008','password','Kiran',31,'9998887776','kiran@demo.com'),('CU2009','password','Neha',29,'9998887776','neha@demo.com'),('CU2010','password','Ajay',34,'9998887776','ajay@demo.com'),('CU2011','password','Rima',26,'9998887776','rima@demo.com'),('CU2012','password','Rajesh',33,'9998887776','rajesh@demo.com'),('CU2013','password','Deepak',30,'9998887776','deepak@demo.com'),('CU2014','password','Anita',27,'9998887776','anita@demo.com'),('CU2015','password','Ravi',31,'9998887776','ravi@demo.com'),('CU2016','password','Kavita',28,'9998887776','kavita@demo.com'),('CU2017','password','Manish',32,'9998887776','manish@demo.com'),('CU2018','password','Shalini',29,'9998887776','shalini@demo.com'),('CU2019','password','Sanjay',33,'9998887776','sanjay@demo.com'),('CU2020','password','Kirti',30,'9998887776','kirti@demo.com'),('CU2021','password','Asha',34,'9998887776','asha@demo.com'),('CU2022','password','Saurabh',31,'9998887776','saurabh@demo.com'),('CU3003','password',NULL,NULL,NULL,NULL),('CU3004','password',NULL,NULL,NULL,NULL),('CU3005','password','Aarav',25,'9998887776','aarav@demo.com'),('CU3006','password','Aanya',28,'9998887776','aanya@demo.com'),('CU3007','password','Vihaan',32,'9998887776','vihaan@demo.com'),('CU3008','password','Ishaan',27,'9998887776','ishaan@demo.com'),('CU3009','password','Aaradhya',35,'9998887776','aaradhya@demo.com'),('CU3010','password','Myra',31,'9998887776','myra@demo.com'),('CU3011','password','Advait',29,'9998887776','advait@demo.com'),('CU3012','password','Anika',34,'9998887776','anika@demo.com'),('CU3013','password','Arjun',26,'9998887776','arjun@demo.com'),('CU3014','password','Shreya',33,'9998887776','shreya@demo.com'),('CU3015','password','Aryan',30,'9998887776','aryan@demo.com'),('CU3016','password','Sia',27,'9998887776','sia@demo.com'),('CU3017','password','Kabir',31,'9998887776','kabir@demo.com'),('CU3018','password','Mythri',28,'9998887776','mythri@demo.com'),('CU3019','password','Atharv',32,'9998887776','atharv@demo.com'),('CU3020','password','Anaya',29,'9998887776','anaya@demo.com'),('CU3021','password','Shaurya',33,'9998887776','shaurya@demo.com'),('CU3022','password','Zara',30,'9998887776','zara@demo.com'),('CU3023','password','Mohammad',34,'9998887776','mohammad@demo.com');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `empLoginId` varchar(10) NOT NULL,
  `empPassword` varchar(20) DEFAULT NULL,
  `empType` varchar(20) DEFAULT NULL,
  `empName` varchar(45) DEFAULT NULL,
  `empPhone` varchar(10) DEFAULT NULL,
  `empEmail` varchar(45) DEFAULT NULL,
  `empStatus` varchar(20) DEFAULT 'ACTIVE',
  PRIMARY KEY (`empLoginId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES ('AD1001','password','ADMIN','Priti Singh','9998887776','help@admin.com','ACTIVE'),('AD1002','password','ADMIN','John Doe','9998887775','john@example.com','ACTIVE'),('AD1003','password','ADMIN','Emily Davis','6665554443','emily@example.com','ACTIVE'),('AD1004','password','ADMIN','Sarah Wilson','4443332221','sarah@example.com','ACTIVE'),('AD1005','password','ADMIN','Olivia Thompson','2221110009','olivia@example.com','ACTIVE'),('AD1006','password','ADMIN','Sophia Anderson','0009998887','sophia@example.com','ACTIVE'),('AD1007','password','ADMIN','Mohini Gupta','9876543210','mohini@example.com','ACTIVE'),('AD1008','password','ADMIN','Sneha Kapoor','7654321098','sneha@example.com','ACTIVE'),('AD1009','password','ADMIN','Rajeev Kumar','5432109876','rajeev@example.com','ACTIVE'),('AD1010','password','ADMIN','Alok Verma','3210987654','alok@example.com','ACTIVE'),('AD1011','password','ADMIN','Smita Gupta','1098765432','smita@example.com','ACTIVE'),('AD1012','password','ADMIN','Nikhil Kapoor','9876543210','nikhil@example.com','ACTIVE'),('AD1013','password','ADMIN','Anand Sharma','7654321098','anand@example.com','ACTIVE'),('AD1014','password','ADMIN','Sachin Kumar','5432109876','sachin@example.com','ACTIVE'),('AD1015','password','ADMIN','Ravi Verma','3210987654','ravi.verma@example.com','ACTIVE'),('AD1016','password','ADMIN','Amita Sharma','1098765432','amita@example.com','ACTIVE'),('AD1017','password','ADMIN','Priyanka Kapoor','9876543210','priyanka@example.com','ACTIVE'),('AD1018','password','ADMIN','Sonia Kapoor','7654321098','sonia@example.com','ACTIVE'),('AD1019','password','ADMIN','Anita Verma','5432109876','anita.verma@example.com','ACTIVE'),('AD1020','password','ADMIN','Sudha Sharma','3210987654','sudha@example.com','ACTIVE'),('AD1021','password','ADMIN','Geeta Gupta','1098765432','geeta@example.com','ACTIVE'),('EM001','password','Expert','Dev Gupta','89898','dg6633@srmist.edu.in','ACTIVE'),('EM002','password','EMPLOYEE','Michael Johnson','7776665554','michael@example.com','ACTIVE'),('EM1002','password','Admin','dev','123456','qssw','ACTIVE'),('EX3001','password','EXPERT','DemoUser','4444444','expert@admin.com','DEACTIVATE'),('EX3002','password','EXPERT','Jane Smith','8887776665','jane@example.com','ACTIVE'),('EX3003','password','EXPERT','David Brown','5554443332','david@example.com','ACTIVE'),('EX3004','password','EXPERT','Robert Taylor','3332221110','robert@example.com','ACTIVE'),('EX3005','password','EXPERT','William Martinez','1110009998','william@example.com','ACTIVE'),('EX3006','password','EXPERT','James Rodriguez','9998887776','james@example.com','ACTIVE'),('EX3007','password','EXPERT','Rahul Singh','8765432109','rahul.singh@example.com','ACTIVE'),('EX3008','password','EXPERT','Pooja Sharma','6543210987','pooja@example.com','ACTIVE'),('EX3009','password','EXPERT','Kiran Mishra','4321098765','kiran@example.com','ACTIVE'),('EX3010','password','EXPERT','Neeraj Kumar','2109876543','neeraj@example.com','ACTIVE'),('EX3011','password','EXPERT','Ravi Singh','0987654321','ravi@example.com','ACTIVE'),('EX3012','password','EXPERT','Meera Gupta','8765432109','meera@example.com','ACTIVE'),('EX3013','password','EXPERT','Preeti Patel','6543210987','preeti@example.com','ACTIVE'),('EX3014','password','EXPERT','Rina Sharma','4321098765','rina@example.com','ACTIVE'),('EX3015','password','EXPERT','Kavita Gupta','2109876543','kavita.gupta@example.com','ACTIVE'),('EX3016','password','EXPERT','Manoj Singh','0987654321','manoj@example.com','ACTIVE'),('EX3017','password','EXPERT','Rajat Singh','8765432109','rajat@example.com','ACTIVE'),('EX3018','password','EXPERT','Rajiv Gupta','6543210987','rajiv@example.com','ACTIVE'),('EX3019','password','EXPERT','Alok Singh','4321098765','alok.singh@example.com','ACTIVE'),('EX3020','password','EXPERT','Rajeev Singh','2109876543','rajeev.singh@example.com','ACTIVE'),('EX3021','password','EXPERT','Neeta Sharma','0987654321','neeta@example.com','ACTIVE');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `services`
--

DROP TABLE IF EXISTS `services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `services` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `services`
--

LOCK TABLES `services` WRITE;
/*!40000 ALTER TABLE `services` DISABLE KEYS */;
INSERT INTO `services` VALUES (1,'SERVICE NAME','SERVICE DESCRIPTION'),(2,'app development','Developement of the app '),(3,'Web Design','Design and development of websites'),(4,'Mobile App Development','Development of mobile applications'),(5,'Graphic Design','Creation of visually appealing graphics'),(6,'SEO Optimization','Improvement of search engine rankings'),(7,'Content Writing','Creation of high-quality written content'),(8,'Social Media Management','Management of social media accounts'),(9,'E-commerce Development','Development of online shopping platforms'),(10,'Digital Marketing','Promotion of products/services through digital channels'),(11,'UI/UX Design','Design of user interfaces and user experiences'),(12,'IT Consulting','Consultation on IT solutions and strategies'),(13,'Data Analysis','Analysis of data to gain insights'),(14,'Cloud Computing','Utilization of cloud-based technologies'),(15,'Cybersecurity','Protection of computer systems and data from theft or damage'),(16,'Software Testing','Testing and quality assurance of software applications'),(17,'Database Management','Management and optimization of databases'),(18,'Network Setup and Maintenance','Setup and maintenance of computer networks'),(19,'IT Support','Technical support for hardware and software issues'),(20,'Video Production','Creation of professional videos'),(21,'Animation Design','Creation of animated visuals'),(22,'Virtual Reality Development','Development of virtual reality experiences'),(23,'Augmented Reality Development','Development of augmented reality applications'),(24,'Game Development','Creation of interactive games'),(25,'Data Science Consulting','Consultation on data science and analytics'),(26,'Business Intelligence Solutions','Creation of BI solutions for data analysis'),(27,'Project Management','Management of projects and team coordination'),(28,'IT Training and Workshops','Training programs and workshops on IT topics'),(29,'Web Design','Design and development of websites'),(30,'Mobile App Development','Development of mobile applications'),(31,'Graphic Design','Creation of visually appealing graphics'),(32,'SEO Optimization','Improvement of search engine rankings'),(33,'Content Writing','Creation of high-quality written content'),(34,'Social Media Management','Management of social media accounts'),(35,'E-commerce Development','Development of online shopping platforms'),(36,'Digital Marketing','Promotion of products/services through digital channels'),(37,'UI/UX Design','Design of user interfaces and user experiences'),(38,'IT Consulting','Consultation on IT solutions and strategies'),(39,'Data Analysis','Analysis of data to gain insights'),(40,'Cloud Computing','Utilization of cloud-based technologies'),(41,'Cybersecurity','Protection of computer systems and data from theft or damage'),(42,'Software Testing','Testing and quality assurance of software applications'),(43,'Database Management','Management and optimization of databases'),(44,'Network Setup and Maintenance','Setup and maintenance of computer networks'),(45,'IT Support','Technical support for hardware and software issues'),(46,'Video Production','Creation of professional videos'),(47,'Animation Design','Creation of animated visuals'),(48,'Virtual Reality Development','Development of virtual reality experiences'),(49,'Augmented Reality Development','Development of augmented reality applications'),(50,'Game Development','Creation of interactive games'),(51,'Data Science Consulting','Consultation on data science and analytics'),(52,'Business Intelligence Solutions','Creation of BI solutions for data analysis'),(53,'Project Management','Management of projects and team coordination'),(54,'IT Training and Workshops','Training programs and workshops on IT topics');
/*!40000 ALTER TABLE `services` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-13 16:22:03
