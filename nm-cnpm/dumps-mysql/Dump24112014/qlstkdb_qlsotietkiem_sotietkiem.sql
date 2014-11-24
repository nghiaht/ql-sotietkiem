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
-- Table structure for table `qlsotietkiem_sotietkiem`
--

DROP TABLE IF EXISTS `qlsotietkiem_sotietkiem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `qlsotietkiem_sotietkiem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `khach_hang_id` int(11) NOT NULL,
  `loai_tiet_kiem_id` int(11) NOT NULL,
  `ngay_mo` datetime NOT NULL,
  `tien_gui` double NOT NULL,
  `tinh_trang` varchar(5) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `qlsotietkiem_sotietkiem_25a88016` (`khach_hang_id`),
  KEY `qlsotietkiem_sotietkiem_60f4dde9` (`loai_tiet_kiem_id`),
  CONSTRAINT `khach_hang_id_refs_id_afc71910` FOREIGN KEY (`khach_hang_id`) REFERENCES `qlsotietkiem_khachhang` (`id`),
  CONSTRAINT `loai_tiet_kiem_id_refs_id_93d8614a` FOREIGN KEY (`loai_tiet_kiem_id`) REFERENCES `qlsotietkiem_loaitietkiem` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `qlsotietkiem_sotietkiem`
--

LOCK TABLES `qlsotietkiem_sotietkiem` WRITE;
/*!40000 ALTER TABLE `qlsotietkiem_sotietkiem` DISABLE KEYS */;
INSERT INTO `qlsotietkiem_sotietkiem` VALUES (1,2,2,'2014-11-21 04:26:57',585000,'MO');
/*!40000 ALTER TABLE `qlsotietkiem_sotietkiem` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-11-24  7:35:31
