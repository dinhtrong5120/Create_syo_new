-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: db_new_prj_final
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `comment_column`
--

DROP TABLE IF EXISTS `comment_column`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment_column` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `comment_name` varchar(45) NOT NULL,
  PRIMARY KEY (`comment_id`),
  UNIQUE KEY `comment_name_UNIQUE` (`comment_name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment_column`
--

LOCK TABLES `comment_column` WRITE;
/*!40000 ALTER TABLE `comment_column` DISABLE KEYS */;
/*!40000 ALTER TABLE `comment_column` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `config`
--

DROP TABLE IF EXISTS `config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `config` (
  `config_id` int(11) NOT NULL AUTO_INCREMENT,
  `config_name` varchar(45) NOT NULL,
  PRIMARY KEY (`config_id`),
  UNIQUE KEY `config_nảme_UNIQUE` (`config_name`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `config`
--

LOCK TABLES `config` WRITE;
/*!40000 ALTER TABLE `config` DISABLE KEYS */;
/*!40000 ALTER TABLE `config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `device`
--

DROP TABLE IF EXISTS `device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `device` (
  `device_name` varchar(255) NOT NULL,
  `device_group` varchar(255) NOT NULL,
  PRIMARY KEY (`device_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device`
--

LOCK TABLES `device` WRITE;
/*!40000 ALTER TABLE `device` DISABLE KEYS */;
/*!40000 ALTER TABLE `device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `device_details`
--

DROP TABLE IF EXISTS `device_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `device_details` (
  `device_details_id` int(11) NOT NULL AUTO_INCREMENT,
  `device_name` varchar(255) NOT NULL,
  `device_details_name` varchar(255) NOT NULL,
  `group_detail` varchar(255) DEFAULT NULL,
  `option_detail` varchar(500) DEFAULT NULL,
  `auto_detail` varchar(255) DEFAULT NULL,
  `group_key_map` varchar(255) NOT NULL DEFAULT 'default_key',
  `default` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`device_details_id`),
  UNIQUE KEY `device_details_name_UNIQUE` (`device_details_name`,`device_name`),
  KEY `fk_device_details_device1_idx` (`device_name`),
  CONSTRAINT `fk_device_details_device1` FOREIGN KEY (`device_name`) REFERENCES `device` (`device_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=757 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device_details`
--

LOCK TABLES `device_details` WRITE;
/*!40000 ALTER TABLE `device_details` DISABLE KEYS */;
/*!40000 ALTER TABLE `device_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `information_project`
--

DROP TABLE IF EXISTS `information_project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `information_project` (
  `parameter_name` varchar(255) NOT NULL,
  `group_infor` varchar(255) DEFAULT NULL,
  `keyword` varchar(255) DEFAULT NULL,
  `auto_infor` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`parameter_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `information_project`
--

LOCK TABLES `information_project` WRITE;
/*!40000 ALTER TABLE `information_project` DISABLE KEYS */;
/*!40000 ALTER TABLE `information_project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lot`
--

DROP TABLE IF EXISTS `lot`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lot` (
  `lot_id` int(11) NOT NULL AUTO_INCREMENT,
  `lot_name` varchar(45) NOT NULL,
  PRIMARY KEY (`lot_id`),
  UNIQUE KEY `lot_name_UNIQUE` (`lot_name`)
) ENGINE=InnoDB AUTO_INCREMENT=1520 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lot`
--

LOCK TABLES `lot` WRITE;
/*!40000 ALTER TABLE `lot` DISABLE KEYS */;
/*!40000 ALTER TABLE `lot` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `optioncode`
--

DROP TABLE IF EXISTS `optioncode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `optioncode` (
  `config_id` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  `optioncode_value` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`config_id`,`project_id`),
  KEY `fk_config_has_project_project1_idx` (`project_id`),
  KEY `fk_config_has_project_config1_idx` (`config_id`),
  CONSTRAINT `fk_config_has_project_config1` FOREIGN KEY (`config_id`) REFERENCES `config` (`config_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_config_has_project_project1` FOREIGN KEY (`project_id`) REFERENCES `project` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `optioncode`
--

LOCK TABLES `optioncode` WRITE;
/*!40000 ALTER TABLE `optioncode` DISABLE KEYS */;
/*!40000 ALTER TABLE `optioncode` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project` (
  `project_id` int(11) NOT NULL AUTO_INCREMENT,
  `project_name` varchar(45) NOT NULL,
  PRIMARY KEY (`project_id`),
  UNIQUE KEY `project_name_UNIQUE` (`project_name`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project`
--

LOCK TABLES `project` WRITE;
/*!40000 ALTER TABLE `project` DISABLE KEYS */;
/*!40000 ALTER TABLE `project` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_device`
--

DROP TABLE IF EXISTS `project_device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_device` (
  `device_name` varchar(255) NOT NULL,
  `project_id` int(11) NOT NULL,
  PRIMARY KEY (`device_name`,`project_id`),
  KEY `fk_device_has_project_project1_idx` (`project_id`),
  KEY `fk_device_has_project_device1_idx` (`device_name`),
  CONSTRAINT `fk_device_has_project_device1` FOREIGN KEY (`device_name`) REFERENCES `device` (`device_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_device_has_project_project1` FOREIGN KEY (`project_id`) REFERENCES `project` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_device`
--

LOCK TABLES `project_device` WRITE;
/*!40000 ALTER TABLE `project_device` DISABLE KEYS */;
/*!40000 ALTER TABLE `project_device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_device_comment`
--

DROP TABLE IF EXISTS `project_device_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_device_comment` (
  `project_id` int(11) NOT NULL,
  `device_details_id` int(11) NOT NULL,
  `comment_id` int(11) NOT NULL,
  `comment_detail` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`project_id`,`device_details_id`,`comment_id`),
  KEY `fk_Project_device_comment_device_details1_idx` (`device_details_id`),
  KEY `fk_Project_device_comment_project1_idx` (`project_id`),
  KEY `fk_Project_device_comment_comment_column1` (`comment_id`),
  CONSTRAINT `fk_Project_device_comment_comment_column1` FOREIGN KEY (`comment_id`) REFERENCES `comment_column` (`comment_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Project_device_comment_device_details1` FOREIGN KEY (`device_details_id`) REFERENCES `device_details` (`device_details_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Project_device_comment_project1` FOREIGN KEY (`project_id`) REFERENCES `project` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_device_comment`
--

LOCK TABLES `project_device_comment` WRITE;
/*!40000 ALTER TABLE `project_device_comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `project_device_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status_config_device_detail`
--

DROP TABLE IF EXISTS `status_config_device_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `status_config_device_detail` (
  `device_details_id` int(11) NOT NULL,
  `config_id` int(11) NOT NULL,
  `project_id` int(11) NOT NULL,
  `status` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`device_details_id`,`config_id`,`project_id`),
  KEY `fk_status_config_device_detail_config1_idx` (`config_id`),
  KEY `fk_status_config_device_detail_project1_idx` (`project_id`),
  CONSTRAINT `fk_status_config_device_detail_config1` FOREIGN KEY (`config_id`) REFERENCES `config` (`config_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_status_config_device_detail_device_details1` FOREIGN KEY (`device_details_id`) REFERENCES `device_details` (`device_details_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_status_config_device_detail_project1` FOREIGN KEY (`project_id`) REFERENCES `project` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status_config_device_detail`
--

LOCK TABLES `status_config_device_detail` WRITE;
/*!40000 ALTER TABLE `status_config_device_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `status_config_device_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status_lot_config`
--

DROP TABLE IF EXISTS `status_lot_config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `status_lot_config` (
  `project_id` int(11) NOT NULL,
  `config_id` int(11) NOT NULL,
  `lot_id` int(11) NOT NULL,
  `status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`project_id`,`config_id`,`lot_id`),
  KEY `fk_status_lot_config_project1_idx` (`project_id`),
  KEY `fk_status_lot_config_lot1_idx` (`lot_id`),
  KEY `fk_status_lot_config_config1` (`config_id`),
  CONSTRAINT `fk_status_lot_config_config1` FOREIGN KEY (`config_id`) REFERENCES `config` (`config_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_status_lot_config_lot1` FOREIGN KEY (`lot_id`) REFERENCES `lot` (`lot_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_status_lot_config_project1` FOREIGN KEY (`project_id`) REFERENCES `project` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status_lot_config`
--

LOCK TABLES `status_lot_config` WRITE;
/*!40000 ALTER TABLE `status_lot_config` DISABLE KEYS */;
/*!40000 ALTER TABLE `status_lot_config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `permission` varchar(45) DEFAULT NULL,
  `project` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f','master','ALL'),(2,'staff','ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f','admin','ADMIN');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `value_inf`
--

DROP TABLE IF EXISTS `value_inf`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `value_inf` (
  `project_id` int(11) NOT NULL,
  `config_id` int(11) NOT NULL,
  `parameter_name` varchar(255) NOT NULL,
  `value` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`project_id`,`config_id`,`parameter_name`),
  KEY `fk_Value_inf_config1_idx` (`config_id`),
  KEY `fk_Value_inf_project1_idx` (`project_id`),
  KEY `fk_Value_inf_information_project` (`parameter_name`),
  CONSTRAINT `fk_Value_inf_config1` FOREIGN KEY (`config_id`) REFERENCES `config` (`config_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Value_inf_information_project` FOREIGN KEY (`parameter_name`) REFERENCES `information_project` (`parameter_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_Value_inf_project1` FOREIGN KEY (`project_id`) REFERENCES `project` (`project_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `value_inf`
--

LOCK TABLES `value_inf` WRITE;
/*!40000 ALTER TABLE `value_inf` DISABLE KEYS */;
/*!40000 ALTER TABLE `value_inf` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-17 10:51:04
