CREATE DATABASE  IF NOT EXISTS `qlstkdb` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `qlstkdb`;
-- MySQL dump 10.13  Distrib 5.6.17, for Win32 (x86)
--
-- Host: localhost    Database: qlstkdb
-- ------------------------------------------------------
-- Server version	5.6.21-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `qlsotietkiem_phieu`
--

DROP TABLE IF EXISTS `qlsotietkiem_phieu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `qlsotietkiem_phieu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `so_tiet_kiem_id` int(11) NOT NULL,
  `khach_hang_id` int(11) NOT NULL,
  `loai_phieu` varchar(3) NOT NULL,
  `ngay_lap_phieu` datetime NOT NULL,
  `so_tien` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `qlsotietkiem_phieu_364c1723` (`so_tiet_kiem_id`),
  KEY `qlsotietkiem_phieu_25a88016` (`khach_hang_id`),
  CONSTRAINT `khach_hang_id_refs_id_374f8c16` FOREIGN KEY (`khach_hang_id`) REFERENCES `qlsotietkiem_khachhang` (`id`),
  CONSTRAINT `so_tiet_kiem_id_refs_id_96e85a8f` FOREIGN KEY (`so_tiet_kiem_id`) REFERENCES `qlsotietkiem_sotietkiem` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qlsotietkiem_phieu`
--

LOCK TABLES `qlsotietkiem_phieu` WRITE;
/*!40000 ALTER TABLE `qlsotietkiem_phieu` DISABLE KEYS */;
/*!40000 ALTER TABLE `qlsotietkiem_phieu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-11-24  7:35:39
