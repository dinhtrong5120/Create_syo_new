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
INSERT INTO `comment_column` VALUES (1,'comment_1'),(2,'comment_2'),(3,'comment_3'),(4,'comment_4');
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
INSERT INTO `config` VALUES (1,'conf-001'),(2,'conf-002'),(3,'conf-003'),(4,'conf-004'),(5,'conf-005'),(6,'conf-006');
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
INSERT INTO `device` VALUES ('2ND ROW SEAT','X03_SEAT'),('2ND ROW STORAGE','X04_INTERIOR_TRIM_&_STORAGE'),('3rd ROW SEAT','X03_SEAT'),('ACCESS','X08_EXTERIOR'),('ADAS COMFORT','X11_SAFETY_SECURITY'),('ADAS PARKING','X11_SAFETY_SECURITY'),('ADAS SAFETY','X11_SAFETY_SECURITY'),('AIR CONDITIONING AND HEATING','X06_AIR_CONDITIONER'),('AIR QUALITY MANAGEMENT','X06_AIR_CONDITIONER'),('AIRBAGS','X11_SAFETY_SECURITY'),('AMBIENT LIGHTING','X04_INTERIOR_TRIM_&_STORAGE'),('AMENITY','X05_AMENITY'),('ASSIST SEAT','X03_SEAT'),('AUDIO & NAVIGATION','X07_AUDIO_NAVIGATION_CCS'),('BRAKING','X09_MECHANISM'),('CHARGER','X14_EV_PHEV_HEV'),('COMBI METER','X02_COCKPIT'),('DRIVER SEAT','X03_SEAT'),('DRIVING MODE','X09_MECHANISM'),('EV DEDICATED FEATURES','X14_EV_PHEV_HEV'),('GEAR SHIFT','X02_COCKPIT'),('GLASSES','X01_VISIBILITY'),('HMI','X02_COCKPIT'),('LIGHTING','X01_VISIBILITY'),('LOGO & EMBLEM','X08_EXTERIOR'),('NVH MANAGEMENT','X07_AUDIO_NAVIGATION_CCS'),('OPENING','X08_EXTERIOR'),('OTHER','X12_OTHER'),('PARKING BRAKE','X02_COCKPIT'),('PEDALS AND FOOT-REST','X02_COCKPIT'),('PHYSICAL SWITCHES','X02_COCKPIT'),('REAR VIEW MIRROR / CAMERA','X01_VISIBILITY'),('SEAT BELT','X11_SAFETY_SECURITY'),('SIDE VIEW MIRROR / CAMERA','X01_VISIBILITY'),('SOUND BUBBLE','X07_AUDIO_NAVIGATION_CCS'),('SPARE WHEEL','X10_WHEELS_&_TIRES'),('SPEAKERS','X07_AUDIO_NAVIGATION_CCS'),('STEERING','X02_COCKPIT'),('SUN VISOR','X02_COCKPIT'),('TIRES','X10_WHEELS_&_TIRES'),('TRIM','X03_SEAT'),('UNKNOW_device','UNKNOW_device_group'),('WARNING & ALERT','X11_SAFETY_SECURITY'),('WHEELS & WHEEL COVERS','X10_WHEELS_&_TIRES'),('WINDOW OPENING','X02_COCKPIT');
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
  PRIMARY KEY (`device_details_id`),
  UNIQUE KEY `device_details_name_UNIQUE` (`device_details_name`),
  KEY `fk_device_details_device1_idx` (`device_name`),
  CONSTRAINT `fk_device_details_device1` FOREIGN KEY (`device_name`) REFERENCES `device` (`device_name`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=757 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device_details`
--

LOCK TABLES `device_details` WRITE;
/*!40000 ALTER TABLE `device_details` DISABLE KEYS */;
INSERT INTO `device_details` VALUES (1,'UNKNOW_device','電装OPT','XX4AIO','Full OPT,OPT無し',''),(2,'UNKNOW_device','3RD ROW SEAT HEATER AND COOLER','XX4EMC','ALL',''),(3,'UNKNOW_device','Accel Pedal KD(キックダウン)','XR2コントロール','',''),(4,'UNKNOW_device','AC-INV','XP4EVシステム','ｗ',''),(5,'UNKNOW_device','ADDITIONAL HEATER FOR PASSENGERS','XX4EMC','ALL',''),(6,'UNKNOW_device','ADDITIONAL REAR AIR CONDITIONING','XX4EMC','ALL',''),(7,'UNKNOW_device','ASL','UE2動力運転性,XP4EVシステム','w',''),(8,'UNKNOW_device','ATシフトデバイス','XR2コントロール','','アクセルペダルを踏み込んだ時のクリック感（踏みすぎ防止）'),(9,'UNKNOW_device','AUDIO VISUAL','XX4EMC','ALL',''),(10,'UNKNOW_device','AUTO COMPASS','XX4EMC','ALL',''),(11,'UNKNOW_device','AUTO LEVELIZER','XR6視界','',''),(12,'UNKNOW_device','BD-EPS(ベルトドライブEPS)','XQ4機構','',''),(13,'UNKNOW_device','BLACK BOX','XX4EMC','W/ EVENT DATA RECORDER',''),(14,'UNKNOW_device','Brake type','XJBVDC,XQ2VDC','',''),(15,'UNKNOW_device','CAB違い','XQ2VDC','',''),(16,'UNKNOW_device','CHARGE WARNING LAMP','XX4EMC','ALL',''),(17,'UNKNOW_device','CLUTCH CONTROL TYPE','XX4EMC','ALL',''),(18,'UNKNOW_device','CLUTCH_UNIT','XR2コントロール','',''),(19,'UNKNOW_device','COLD STARTING ASSISTANCE','XX4EMC','ALL',''),(20,'UNKNOW_device','Cross bar','XR5風音','',''),(21,'UNKNOW_device','DAS','XQ5Failsafe','w,w/o','DAS(ダイレクトアダプティブステアリング)'),(22,'UNKNOW_device','DAS(ダイレクトアダプティブステアリング)','XQ4機構','',''),(23,'UNKNOW_device','DCDC','XX4NH電動車','ALL',''),(24,'UNKNOW_device','DIRECT ADAPTIVE STEERING','XX4PT','ｗ',''),(25,'UNKNOW_device','DP-EPS(デュアルピニオンEPS)','XQ4機構','',''),(26,'UNKNOW_device','DRIVING ASSISTANCE','XX4EMC','ALL',''),(27,'UNKNOW_device','DYNAMIC TURN INDICATOR','XX4TurnLamp','w',''),(28,'UNKNOW_device','ECO DRIVING COACHING','XX4EMC','ALL',''),(29,'UNKNOW_device','ECU付電動センサーストレージボックス','XX4MCS','ALL',''),(30,'UNKNOW_device','ELECTRIC TOLL COLLECTION','XX4EMC','ALL',''),(31,'UNKNOW_device','EMERGENCY STOP SIGNAL','XX4EMC','ALL',''),(32,'UNKNOW_device','ENERGY SMART MANAGEMENT','XX4EMC','ALL',''),(33,'UNKNOW_device','ENG','XR2燃料','Gasoline,Diesel',''),(34,'UNKNOW_device','ENGINE REV COUNTER','XX4EMC','ALL',''),(35,'UNKNOW_device','e-releace','XX4メカトロS45','w',''),(36,'UNKNOW_device','ESCL','XX4BCM','w,w/o','電子ステアリング コラム ロック'),(37,'UNKNOW_device','ETC 2.0(ELECTRIC TOLL COLLECTION)','XX4WH','Ｗ',''),(38,'UNKNOW_device','EV CHARGE CONN TYPE','XX4EMC','ALL',''),(39,'UNKNOW_device','EVSE','XX4EMC','ALL',''),(40,'UNKNOW_device','Exh.仕様','XR5冷熱','ALL',''),(41,'UNKNOW_device','FR BMPR-type','XR6内外装','ALL',''),(42,'UNKNOW_device','RR BMPR-type','XR6内外装','ALL',''),(43,'UNKNOW_device','FR Grill-type','XR6内外装','ALL',''),(44,'UNKNOW_device','FR:Multi\nRR:5link','XR2シャシー','w',''),(45,'UNKNOW_device','FR:Multi\nRR:LEAF','XR2シャシー','w',''),(46,'UNKNOW_device','FR:Multi\nRR:QI2','XR2シャシー','w',''),(47,'UNKNOW_device','FR:STRUT\nRR:3Link','XR2シャシー','w',''),(48,'UNKNOW_device','FR:STRUT\nRR:HT Beam','XR2シャシー','w',''),(49,'UNKNOW_device','FR:STRUT\nRR:Prarell','XR2シャシー','w',''),(50,'UNKNOW_device','FR:STRUT\nRR:QI2','XR2シャシー','w',''),(51,'UNKNOW_device','FR:STRUT\nRR:RM2','XR2シャシー','w',''),(52,'UNKNOW_device','FR:STRUT\nRR:TC','XR2シャシー','w',''),(53,'UNKNOW_device','HANDS FREE POWER DOOR','XX4PSD','w',''),(54,'UNKNOW_device','HDC','XQ2VDC','w',''),(55,'UNKNOW_device','HEPS(油圧電動パワステ)','XQ4機構','',''),(56,'UNKNOW_device','HEV/PHEV ENERGY MODE','XX4EMC','ALL',''),(57,'UNKNOW_device','Hood visor','XR5風音','',''),(58,'UNKNOW_device','IDM(ｲﾝﾃﾘｼﾞｪﾝﾄ ﾀﾞｲﾅﾐｸｽｺﾝﾄﾛｰﾙ ﾓｼﾞｭｰﾙ)','XQ4機構','',''),(59,'UNKNOW_device','IONIZER','XX4EMC','ALL',''),(60,'UNKNOW_device','IVC','XX4リモート','',''),(61,'UNKNOW_device','KEY SET','XX4EMC','ALL',''),(62,'UNKNOW_device','LIGHTS-ON WARNING','XX4EMC','ALL',''),(63,'UNKNOW_device','LUGGAGE HOOK','XR2車体信頼','ｗ',''),(64,'UNKNOW_device','Max C.W.\nTotal','XR2車体信頼','ｗ',''),(65,'UNKNOW_device','Max C.W.\nFR','XR2車体信頼','ｗ',''),(66,'UNKNOW_device','Max C.W.\nRR','XR2車体信頼','ｗ',''),(67,'UNKNOW_device','MANUAL LEVELIZER','XR6視界','',''),(68,'UNKNOW_device','MAP LAMP','XR6内外装','w,w/o',''),(69,'UNKNOW_device','MEDIA','XM6アンテナ','AM/FM,DTV,SXM,DAS',''),(70,'UNKNOW_device','MUD GUARD','XR6内外装','w,w/o',''),(71,'UNKNOW_device','MICROPHONE','XX4EMC','ALL',''),(72,'UNKNOW_device','OFF ROAD','XX4EMC,XQ2操安','ALL',''),(73,'UNKNOW_device','PATH CONTROL','XX4EMC','ALL',''),(74,'UNKNOW_device','PCU','XX4リモート','',''),(75,'UNKNOW_device','REGENERATIVE BRAKE FOR EV','XX4EMC','ALL',''),(76,'UNKNOW_device','REGENERATIVE BRAKING TYPE','XX4EMC','ALL',''),(77,'UNKNOW_device','REMOTE ENGINE STARTER','XX4BCM,XX4GN1ラジオノイズ','w,w/o',''),(78,'UNKNOW_device','REMOTE ENGINE STARTER (STAND ALONE)','XX4EMC','ALL',''),(79,'UNKNOW_device','REMOTE ENGINE STARTER WITH KEY','XX4EMC','ALL',''),(80,'UNKNOW_device','RES','XP4EVシステム','ｗ',''),(81,'UNKNOW_device','Roof rack','XR5風音','',''),(82,'UNKNOW_device','Roof rail','XR5風音,XR6内外装','w,w/o',''),(83,'UNKNOW_device','ROOF RAIL AND CROSS BAR','XR2車体信頼','ｗ',''),(84,'UNKNOW_device','RR POWER SLIDE  DOOR','XX4WH','Ｗ',''),(85,'UNKNOW_device','REAR SPOILER','XR6内外装','w,w/o',''),(86,'UNKNOW_device','RR SPOILER','XL7外装','',''),(87,'UNKNOW_device','RVI CRUISE CONTROL','XX4EMC','ALL',''),(88,'UNKNOW_device','SEAT HEATER AND COOLER','XX4EMC','ALL',''),(89,'UNKNOW_device','Side visor','XR5風音','',''),(90,'UNKNOW_device','SP1','XM6音質','2phm,4ohm',''),(91,'UNKNOW_device','SP2','XM6音質','Bose,Klipsch,Panasonic,6SP,4SP,2SP',''),(92,'UNKNOW_device','SPEED CUT','XX4EMC','ALL',''),(93,'UNKNOW_device','STATIONARY HEATER','XX4EMC','ALL',''),(94,'UNKNOW_device','STOP AND START','XX4EMC','ALL',''),(95,'UNKNOW_device','Sunroof visor','XR5風音','',''),(96,'UNKNOW_device','SUSPENSION CONTROL','XJBVDC','',''),(97,'UNKNOW_device','SUSPENSION CONTROL VARIABLE DAMPING','XX4PT,XX4EMC','w,w/o',''),(98,'UNKNOW_device','TELEMATIC','XX4GN1ラジオノイズ','w,w/o',''),(99,'UNKNOW_device','TELEMATIC DOORS LOCK','XX4EMC','ALL',''),(100,'UNKNOW_device','TELEMATIC SYSTEM HYPOTHES','XX4EMC','ALL',''),(101,'UNKNOW_device','TELEMATICS\n(EMERGENCY CALL SW)','XX4EMC','ALL',''),(102,'UNKNOW_device','TRACTION CONTROL SYSTEM','XX4EMC','ALL',''),(103,'UNKNOW_device','TRUNK','XX4PTL','POWER OPEN/CLOSE',''),(104,'UNKNOW_device','TSA','XQ2VDC','w',''),(105,'UNKNOW_device','TYPE OF CONTROL','XX4EMC','ALL',''),(106,'UNKNOW_device','VEHICLE DYNAMICS CONTROL','XX4EMC','ALL',''),(107,'UNKNOW_device','WELCOME & GOODBYE SEQUENCE','XX4EMC','ALL',''),(108,'UNKNOW_device','WITH TIMER CHARGER','XX4EMC','ALL',''),(109,'UNKNOW_device','ウインチ','XQA商品性','','winch'),(110,'UNKNOW_device','コラムEPS','XQ4機構','',''),(111,'UNKNOW_device','サスペンション','XX4ALARM','ALL',''),(112,'UNKNOW_device','トーイング','XQA商品性,XQ2操安','','towing'),(113,'UNKNOW_device','REAR TOWING DEVICE','XR2車体信頼','ｗ',''),(114,'UNKNOW_device','TOWING CAPACITY','XQE電動車,XR2車体信頼','最大仕様',''),(115,'UNKNOW_device','バッテリー','XX4ALARM','AFD,HE',''),(116,'UNKNOW_device','バッテリヒータ','XP4充電','w',''),(117,'UNKNOW_device','バッテリクーラ','XP4充電','w',''),(118,'UNKNOW_device','AC INV\n(V2L_inside)','XP4充電','w',''),(119,'UNKNOW_device','マニュアルトランスミッション','XQA商品性','',''),(120,'UNKNOW_device','車体色','XD2材料','黒若しくはダーク色',''),(121,'UNKNOW_device','跳ね上げフード','XR6歩行者保護','with,without',''),(122,'UNKNOW_device','冷却仕様','XR5冷熱','ALL',''),(123,'UNKNOW_device','PRE CRASH','XX4プリクラッシュ','w',''),(124,'UNKNOW_device','FR SUSP形式違い','XQ5保安防災','ALL',''),(125,'UNKNOW_device','RR SUSP形式違い','XQ5保安防災','ALL',''),(126,'UNKNOW_device','アンダーカバー','XQ5保安防災','',''),(127,'UNKNOW_device','外装違い\nナロー/ワイド、2/3ROW','XQ5保安防災','',''),(128,'UNKNOW_device','キャニスタ ORVR 追加','XQ5保安防災','',''),(129,'UNKNOW_device','強電BAT MD/Cell違い','XQ5保安防災','',''),(130,'UNKNOW_device','強電BAT 容量違い','XQ5保安防災','',''),(131,'UNKNOW_device','グリルシャッター','XQ5保安防災','',''),(132,'UNKNOW_device','姿勢違い','XQ5保安防災','',''),(133,'UNKNOW_device','内装違い','XQ5保安防災','',''),(134,'UNKNOW_device','SUSPENSION TYPE','XQ5車両信頼性,XJBVDC','ALL',''),(135,'UNKNOW_device','フロントサイドメンバ構造','XR8XTF','',''),(136,'UNKNOW_device','フロントピラー構造','XR8XTF','',''),(137,'UNKNOW_device','センターピラー構造','XR8XTF','',''),(138,'UNKNOW_device','シル構造','XR8XTF','',''),(139,'UNKNOW_device','ルーフサイド構造','XR8XTF','',''),(140,'UNKNOW_device','シートベルトアンカ位置','XR8XTF','',''),(141,'UNKNOW_device','エアバッグシステム','XR8XTF','',''),(142,'UNKNOW_device','燃料供給方式','XR8XTF','',''),(143,'UNKNOW_device','フューエルタンク形状','XR8XTF','',''),(144,'UNKNOW_device','フューエルタンクの材質','XR8XTF','',''),(145,'UNKNOW_device','フューエルタンクの取り付け方式','XR8XTF','',''),(146,'UNKNOW_device','フューエルタンク搭載位置','XR8XTF','',''),(147,'UNKNOW_device','ウィンドシールド取付構造','XR8XTF','',''),(148,'UNKNOW_device','ウィンドシールド形状','XR8XTF','',''),(149,'UNKNOW_device','エンジンフード形状','XR8XTF','',''),(150,'UNKNOW_device','フードヒンジ構造','XR8XTF','',''),(151,'UNKNOW_device','乗員H.P.','XR8XTF','',''),(152,'UNKNOW_device','フィラーチューブ','XR8XTF','',''),(153,'UNKNOW_device','燃料配管','XR8XTF','',''),(154,'UNKNOW_device','燃料系部品取り付け構造','XR8XTF','',''),(155,'UNKNOW_device','リア・サイド・メンバー / リア・サイド・フレームの形状','XR8XTF','',''),(156,'UNKNOW_device','後輪懸架装置','XR8XTF','',''),(157,'UNKNOW_device','フロントフェンダ外形','XR8XTF','',''),(158,'UNKNOW_device','ヘッドランプ外形','XR8XTF','',''),(159,'UNKNOW_device','ワイパ外形','XR8XTF','',''),(160,'UNKNOW_device','バンパ仕様','XR8XTF','',''),(161,'UNKNOW_device','エネルギー\n吸収材仕様','XR8XTF','',''),(162,'UNKNOW_device','unknow_ 1','','',''),(163,'LIGHTING','3RD BRAKE LIGHT / HIGH MOUNT STOP LAMP','XX4ABC','ALL',''),(164,'LIGHTING','ADB(ADAPTIVE DRIVING BEAM)','AAAA','ｗ,w/o',''),(165,'LIGHTING','GLARE FREE HIGH BEAM STANDARD / ADAPTIVE DRIVING BEAM (ADB)','BBBB','w/o',''),(166,'LIGHTING','ADJUSTMENT OF HEADLIGHTS','CCCC','ALL',''),(167,'LIGHTING','ADAPTIVE FRONT LIGHTING SYSTE(AFS)','EEEEE','w',''),(168,'LIGHTING','ALS(Auto Light Sensor)','FFFFF','w,w/o',''),(169,'LIGHTING','AUTO LIGHT (ALS)','XX4オートライト','w,w/o',''),(170,'LIGHTING','AUTO EXTENTION LIGHT','XX4EMC','ALL',''),(171,'LIGHTING','Auto light','XX4BCM','w/o,LINタイプ,ハードウェアタイプ','自動車のボディ制御に使われる通信プロトコル「LIN」'),(172,'LIGHTING','AUTO LIGHT SYSTEM','XX4EMC','ALL',''),(173,'LIGHTING','AUTO WIPER AND AUTO LIGHT','XX4EMC','ALL',''),(174,'LIGHTING','Brake lamp','XX4BCM','LED,Bulb',''),(175,'LIGHTING','BULB REAR LAMP','XX4GN1ラジオノイズ','w',''),(176,'LIGHTING','DAYTIME HEADLIGHTS','XX4EMC','ALL',''),(177,'LIGHTING','DAYTIME RUNNING LIGHT','XX7USM','with',''),(178,'LIGHTING','DAYTIME RUNNING LIGHT (DRL)','XR6視界,XX4EMC','w,ALL',''),(179,'LIGHTING','DAYTIME RUNNING LIGHTS','XX4EMC,XX4WH','ALL',''),(180,'LIGHTING','Delay Timer','XX4BCM','w,w/o',''),(181,'LIGHTING','DRL','XX4BCM','w,w/o',''),(182,'LIGHTING','FOG LIGHTS','XX4EMC','ALL',''),(183,'LIGHTING','FR FOG LAMP','XL7外装','W',''),(184,'LIGHTING','FR FOG LAMP(HAROGEN)','XX4WH','W',''),(185,'LIGHTING','FR FOG LAMP(LED)','XX4WH','W',''),(186,'LIGHTING','Front Fog','XX4BCM','w,w/o',''),(187,'LIGHTING','FRONT FOG LAMP','XX7USM,XX4GN1ラジオノイズ,XX4EMC','LED,HALOGEN,w,all',''),(188,'LIGHTING','FRONT FOG LAMP\nフロントフォグランプ','XR6視界','',''),(189,'LIGHTING','FRONT ILLUMINATION LIGHT','XX4EMC','ALL',''),(190,'LIGHTING','FRONT LIGHT','XX4EMC','ALL',''),(191,'LIGHTING','FRONT LIGHT\nヘッドランプ','XR6視界','',''),(192,'LIGHTING','FRONT LIGHT/HEAD LAMP','XX4WH','ALL',''),(193,'LIGHTING','GROUND ILLUMINATION','XX4EMC','ALL',''),(194,'LIGHTING','HALOGEN HEADLAMP','XX4GN1ラジオノイズ','w',''),(195,'LIGHTING','HBA(HIGH BEAM ASSIST)','XX4ADB,XX4HBA','w/o,w',''),(196,'LIGHTING','HEAD LAMP LEVELIZER','XX7USM','Manual  LEVELIZER,AUTO   LEVELIZER,AirSUS LEVELIZER,ALL',''),(197,'LIGHTING','HEAD LAMPS TYPE','XX4EMC','ALL',''),(198,'LIGHTING','HEADLAMP CLEANER','XX7USM,XX4EMC','with,ALL',''),(199,'LIGHTING','HEADLAMP TYPE','XX7USM','LED ,HALOGEN',''),(200,'LIGHTING','HEADLIGHT WASHER','XX4EMC','ALL',''),(201,'LIGHTING','HEADLIGHT WIPERS','XX4EMC','ALL',''),(202,'LIGHTING','HIGH BEAM ASSIST','XX4GN1ラジオノイズ,XX4EMC','w,w/o',''),(203,'LIGHTING','HIGH MOUNTED STOP LAMP','XX4EMC','',''),(204,'LIGHTING','LED HEADLAMP','XX4GN1ラジオノイズ','w',''),(205,'LIGHTING','LED LB','XX4LEDHead','w',''),(206,'LIGHTING','LED REAR LAMP','XX4GN1ラジオノイズ','w',''),(207,'LIGHTING','PUDDLE LAMP','XX4EMC','ALL',''),(208,'LIGHTING','RAISED BRAKE LIGHT','XX4EMC','ALL',''),(209,'LIGHTING','REAR  LAMP','XX4EMC','ALL',''),(210,'LIGHTING','Rear Fog','XX4BCM','LED,Bulb,w/o',''),(211,'LIGHTING','RR FOG LAMP','XL7外装','W',''),(212,'LIGHTING','REAR FOG LAMP','XX4GN1ラジオノイズ,XX4WH,XX4EMC','w,ALL',''),(213,'LIGHTING','REAR FOG LAMP\nリアフォグランプ','XR6視界','',''),(214,'LIGHTING','REAR LIGHT','XX4EMC','ALL',''),(215,'LIGHTING','REAR LIGHT\nリアライト\nリアコンビランプ','XR6視界','',''),(216,'LIGHTING','RLS(Rain Light Sensor)','XX4オートライト,レインセンサ','w,w/o',''),(217,'LIGHTING','SIDE LIGHTS','XX4EMC','ALL',''),(218,'LIGHTING','SIDE MARKER LAMP','XX4EMC','ALL','前後フェンダーの標識ランプ'),(219,'LIGHTING','SIDE TURN SIGNAL','XX4EMC','ALL',''),(220,'LIGHTING','TURN SIGNAL','XX4EMC','ALL',''),(221,'LIGHTING','TURN SIGNAL LAMP','XX4EMC','ALL',''),(222,'LIGHTING','コーナリングランプ','XR6視界','',''),(223,'LIGHTING','フロントサイドマーカ','XR6視界','',''),(224,'LIGHTING','ヘッドランプウオッシャー\n（HLC)','XR6視界','',''),(225,'LIGHTING','リヤサイドマーカー','XR6視界','',''),(226,'LIGHTING','外装イルミランプ','XX4BCM','Coutesy lamp,Puddle lamp,w/o','ドアの開閉に伴って点灯・消灯し、乗降者の足元を照らす'),(227,'LIGHTING','足元ランプ（ミラー付け）','XR6視界','',''),(228,'LIGHTING','Lighting_ 1','','',''),(229,'GLASSES','Auto Wiper','XX4BCM','w,w/o',''),(230,'GLASSES','FRONT WINDSCREEN HEATER','XX4GN1ラジオノイズ','w,w/o',''),(231,'GLASSES','FRONT WINDSCREEN HEATER / HEATED FRONT SCREEN','XM6アンテナ','w,w/o',''),(232,'GLASSES','FRONT WINDSCREEN WIPER SP','XX4EMC','ALL',''),(233,'GLASSES','HEATED SCREEN','XX4WH','Ｗ',''),(234,'GLASSES','Heating windscreen','XX4BCM','w,w/o',''),(235,'GLASSES','RAIN SENSITIVE','XX4オートライト,レインセンサ','w,w/o',''),(236,'GLASSES','REAR SCREEN','XX4EMC','DEFOGGER',''),(237,'GLASSES','REAR SCREEN SF','XX4EMC','DEFOGGER',''),(238,'GLASSES','REAR SCREEN WIPER','XX4EMC','ALL',''),(239,'GLASSES','REAR WINDOW','XX4EMC','W/ TIMER',''),(240,'GLASSES','REAR WINDOW WIPER','XX4EMC','ALL',''),(241,'GLASSES','REAR WIPERS\nリアワイパー','XR6視界','',''),(242,'GLASSES','WINDOWS COLOUR','XX4EMC','WIPER DE-ICER',''),(243,'GLASSES','WINDSCREEN','XX4EMC','WIPER DE-ICER,HEATING WINDSCREEN',''),(244,'GLASSES','WINDSCREEN HEATER','XX4EMC','ALL',''),(245,'GLASSES','WINDSCREEN WIPERS','XX4EMC','ALL',''),(246,'GLASSES','WINDSCREEN WIPERS\nフロントワイパー','XR6視界','',''),(247,'GLASSES','WIPER DEICER','XX4WH','Ｗ',''),(248,'GLASSES','ワイパーデアイサー','XR6視界','','ワイパーの部分の電熱線が温まり、凍っていたワイパーが動くようになる'),(249,'SIDE VIEW MIRROR / CAMERA','Automatically folding mirror','XX4BCM','w,w/o',''),(250,'SIDE VIEW MIRROR / CAMERA','EXTERIOR MIRRORS RETRACTI','XX4EMC','ALL',''),(251,'SIDE VIEW MIRROR / CAMERA','EXTERIOR REAR VIEW MIRROR','XX4EMC','ALL',''),(252,'SIDE VIEW MIRROR / CAMERA','OUTSIDE MIRROR','XX4EMC,XX4スイッチ','Electrrical Adjustment + Manual Folding,Electrrical Adjustment + Manual Folding + Heated,Electrrical Adjustment + Manual Folding + Heated + Memory,Electrrical Adjustment + Automatically Folding,Electrrical Adjustment + Automatically Folding + Heated,Electrrical Adjustment + Automatically Folding + Reverse Dr & As side,Electrrical Adjustment + Automatically Folding + Heated + Reverse Dr & As side',''),(253,'SIDE VIEW MIRROR / CAMERA','OUTSIDE MIRROR ADJUST','XX4EMC','ALL',''),(254,'SIDE VIEW MIRROR / CAMERA','OUTSIDE MIRROR\nアウトサイドミラー','XR6視界','',''),(255,'SIDE VIEW MIRROR / CAMERA','OUTSIDE MIRROR MEMORY','XX4PMU','w',''),(256,'SIDE VIEW MIRROR / CAMERA','直前直左鏡','XR6視界','','サイドアンダーミラー'),(257,'REAR VIEW MIRROR / CAMERA','INSIDE MIRROR\nインサイドミラー','XR6視界','',''),(258,'REAR VIEW MIRROR / CAMERA','INTERIOR REAR VIEW MIRROR','XX4EMC','ALL',''),(259,'REAR VIEW MIRROR / CAMERA','ROOM MIRROR','XX4EMC,XQ4実車','ALL',''),(260,'REAR VIEW MIRROR / CAMERA','ROOM MIRROR / REAR VISIBILITY','XX4EMC,XQ4車体','ALL',''),(261,'REAR VIEW MIRROR / CAMERA','ROOM MIRROR－AUTO DIMMING','XX4GN1ラジオノイズ','w',''),(262,'REAR VIEW MIRROR / CAMERA','ROOM MIRROR－SMART REAR VIEW MIRROR','XX4GN1ラジオノイズ','w',''),(263,'REAR VIEW MIRROR / CAMERA','SMART REAR VIEW MIRROR','XX4WH','ALL',''),(264,'REAR VIEW MIRROR / CAMERA','SRVM','XR6視界,XX4SC,XM6camera,XM6アンテナ','',''),(265,'REAR VIEW MIRROR / CAMERA','リアアンダーミラー','XR6視界','',''),(266,'REAR VIEW MIRROR / CAMERA','リアカメラウオッシャー','XR6視界','',''),(267,'COMBI METER','COMBI METER','XX4CANGateway','FULL TFT,ANALOG SPEED+TACHO + TFT,ALL',''),(268,'COMBI METER','Head Up Display','XX4SV','w,w/o',''),(269,'COMBI METER','HEAD UP DISPLAY (HUD)','XX4EMC,XX4WH,XX4CANGateway','ALL',''),(270,'COMBI METER','HUD','XR4HMI,XX4GN1ラジオノイズ,XM6メータ,XX4AD','w,w/o',''),(271,'COMBI METER','Meter','XX4BCM,XX4AD','Full TFT,Display,Segment',''),(272,'COMBI METER','Meter Display Size','XX4SV,XX4AD','7inch,12.3inch,14inch',''),(273,'COMBI METER','METER UNIT','XX4EMC','ALL',''),(274,'COMBI METER','SETTINGS OF COMBI METER','XX4EMC,XR6シートベルト','ALL',''),(275,'COMBI METER','SIZE OF COMBI METER SCREEN','XX4EMC,XM6メータ,XR6シートベルト','ALL,14.3\" DISPLAY',''),(276,'COMBI METER','SPEED METER UNIT','XX4EMC','ALL',''),(277,'COMBI METER','TYPE OF COMBI METER','XX4EMC,XR6シートベルト','ALL,FULL TFT',''),(278,'HMI','IN-CAR COMMUNICATION','XX4EMC','ALL',''),(279,'HMI','OUTSIDE TEMPERATURE METER','XX4EMC','ALL',''),(280,'HMI','OUTSIDE THERMO METER','XX4EMC','ALL',''),(281,'HMI','VOICE VEHICLE CONTROL','XX4EMC','ALL',''),(282,'PHYSICAL SWITCHES','ENGINE START / POWER ON','XX4EMC','ALL',''),(283,'PHYSICAL SWITCHES','ENGINE START TYPE','XX7USM,XX4EMC','with,ALL',''),(284,'PHYSICAL SWITCHES','Start Engine  type','XX4BCM','I-key,CKC',''),(285,'PHYSICAL SWITCHES','Start Engine  type  1','','',''),(286,'STEERING','COMBINATION SWITCH','XX4EMC','ALL',''),(287,'STEERING','PADDLE Shift','XX4BCM','w,w/o',''),(288,'STEERING','PADDLE SHIFT LEVER','XX4GN1ラジオノイズ,XX4EMC','w,ALL',''),(289,'STEERING','POWER STEERING','XX4EMC','ALL',''),(290,'STEERING','STEERING','XX4EMC','ELECTRIC POWERED',''),(291,'STEERING','STEERING WHEEL','XQ4実車','ALL',''),(292,'STEERING','STEERING SWITCH','','ALL',''),(293,'STEERING','STEERING SWITCHES','XX4EMC','ALL',''),(294,'STEERING','STEERING WHEEL ADJUSTMENT','XX4EMC,XQ4車体','ALL',''),(295,'STEERING','STEERING WHEEL HEATER','XX4EMC,XX4WH','ALL',''),(296,'STEERING','STRG Heater','XR5空調,XX4AD','w,w/o',''),(297,'STEERING','ＳＴＲＧ固定式パドル','XR2コントロール','',''),(298,'STEERING','VR','XX4BCM','w,w/o','VOICE RECOGNITION'),(299,'STEERING','油圧PS(パワステ)','XQ4機構,XR5冷熱','w',''),(300,'STEERING','PS','XQ2操安','With',''),(301,'PEDALS AND FOOT-REST','金属製フットレスト','XR2コントロール','',''),(302,'GEAR SHIFT','GEAR SHIFT AT','XX4EMC','ALL',''),(303,'GEAR SHIFT','GEAR SPEED CONTROL TYPE','XX4EMC','ALL',''),(304,'GEAR SHIFT','ギアシフト','XX4BCM','Shift by wire,コラムシフト',''),(305,'PARKING BRAKE','ELECTRIC PARKING BRAKE','XQ5保安防災','',''),(306,'PARKING BRAKE','EPKB','XR2コントロール','',''),(307,'PARKING BRAKE','PARKING BRAKE TYPE AND ASSIST','XX4EMC','ALL',''),(308,'PARKING BRAKE','PARKING BRAKE TYPE','XJBVDC','','mechanical, electric両方'),(309,'PARKING BRAKE','PKB hand,foot','XR2コントロール','',''),(310,'PARKING BRAKE','TYPE OF PARK BRAKE','XX4EMC','ALL',''),(311,'WINDOW OPENING','FRONT  WINDOW OPENING SYS','XX4EMC','ALL',''),(312,'WINDOW OPENING','FRONT DOOR WINDOW OPENING','XX4EMC','ALL',''),(313,'WINDOW OPENING','FRONT DOOR WINDOW OPENING2','XX4スイッチ','POWERED FR WINDOW LIFT ✚ AUTO REVERSE ✚ DRIVER ONE TOUCH ✚ TIMER ✚ ALL WINDOW CONTROL PANEL',''),(314,'WINDOW OPENING','Powerwindow','XX4BCM','4席アンチピンチあり, 4席アンチピンチなし','SPに4APと記載'),(315,'WINDOW OPENING','REAR DOOR WINDOW OPENING','XX4EMC','ALL',''),(316,'WINDOW OPENING','REAR DOOR WINDOW OPENING2','XX4スイッチ','POWERED REAR WINDOW LIFT ✚ TIMER,POWERED REAR WINDOW LIFT',''),(317,'WINDOW OPENING','REAR WINDOW OPENING SYSTE','XX4EMC','ALL',''),(318,'WINDOW OPENING','TYPE OF DOOR-OPENER REMOT','XX4EMC','ALL',''),(319,'SUN VISOR','SUN VISOR LED LIGHT','XR6内外装','w,w/o',''),(320,'DRIVER SEAT','3rd Seat','XR3シート,XQ2乗心地性能,XL4シート','w,w/o',''),(321,'DRIVER SEAT','2nd Seat\n3rd Seat','XQ2乗心地性能','w/o',''),(322,'DRIVER SEAT','CENTER CONSOLE','XX4EMC','ALL',''),(323,'DRIVER SEAT','DR HEATED SEAT','XX4SC','w,w/o',''),(324,'DRIVER SEAT','DR SEAT COMFORT FEATURE','XX4EMC','ALL',''),(325,'DRIVER SEAT','DR SEAT HEATER AND COOLER','XX4EMC','ALL',''),(326,'DRIVER SEAT','DR SEAT TYPE AND ADJUSTMENT','XX4EMC','ALL',''),(327,'DRIVER SEAT','DR SEAT TYPE AND ADJUSTMENT.','XR6シートベルト','POWER,MANUAL',''),(328,'DRIVER SEAT','FR SEAT HEATER','XX4WH','Ｗ',''),(329,'DRIVER SEAT','Fr Heater Seat','XR5空調','with',''),(330,'DRIVER SEAT','FR SEAT HEATER AND COOLER','XX4WH','Ｗ',''),(331,'DRIVER SEAT','Fr 空調シート(Heater ＋ Cooler Seat)','XR5空調','with',''),(332,'DRIVER SEAT','FRONT SEATS TYPE','XX4EMC,XR2車体信頼','ALL',''),(333,'DRIVER SEAT','MASSAGE STANDARD\n(2nd seat)','XX4SPCU','w',''),(334,'DRIVER SEAT','MASSAGE STANDARD\n(3rd seat)','XX4SPCU','w',''),(335,'DRIVER SEAT','MASSAGE STANDARD\n(FR seat)','XX4SPCU','w',''),(336,'DRIVER SEAT','POWER SEAT','XX4GN1ラジオノイズ','w,w/o',''),(337,'DRIVER SEAT','Seat adjustment','XX4BCM','メモリーあり,メモリーなし',''),(338,'DRIVER SEAT','SEAT HEATER','XX4GN1ラジオノイズ,XR6乗員判別','w,w/o',''),(339,'DRIVER SEAT','SEAT HEATING','XX4EMC','ALL',''),(340,'DRIVER SEAT','SEAT TYPE','XQ5保安防災','手動、自動',''),(341,'DRIVER SEAT','TYPE OF DRIVER SEAT ADJUS','XX4EMC','ALL',''),(342,'DRIVER SEAT','Ventilated(Heater&Cooler) Seat','XR6乗員判別','w,w/o',''),(343,'DRIVER SEAT','空調シート','XR3シート,XL4シート','w',''),(344,'DRIVER SEAT','シート機構','XL4シート','8WP,6WM,4WP,4WM',''),(345,'DRIVER SEAT','オットマン','XL4シート','ｗ',''),(346,'DRIVER SEAT','スポーツシート','XR3シート','',''),(347,'DRIVER SEAT','スライドシート','XR3シート','',''),(348,'ASSIST SEAT','AS HEATED SEAT','XX4SC','w,w/o',''),(349,'ASSIST SEAT','AS SEAT HEATER','XR6乗員判別','w,w/o',''),(350,'ASSIST SEAT','AS SEAT COMFORT FEATURE','XX4EMC','ALL',''),(351,'ASSIST SEAT','AS SEAT HEATER AND COOLER','XX4EMC','ALL',''),(352,'ASSIST SEAT','AS SEAT TYPE AND ADJUSTMENT','XX4EMC','ALL',''),(353,'ASSIST SEAT','AS SEAT TYPE AND ADJUSTMENT.','XR6シートベルト','POWER,MANUAL',''),(354,'ASSIST SEAT','FRONT PASSENGER SEAT(S)','XX4EMC','ALL',''),(355,'ASSIST SEAT','OCCUPANT MONITORING / CHILD PRESENCE DETECTION DIRECT','XR6乗員判別','',''),(356,'ASSIST SEAT','OCCUPANT MONITORING / CHILD PRESENCE DETECTION INDIRECT','XR6乗員判別','',''),(357,'ASSIST SEAT','助手席SEN仕様','XR6シートベルト','歪み式,静電容量式,簡易マット式',''),(358,'2ND ROW SEAT','2nd row armrest','XD2材料','w',''),(359,'2ND ROW SEAT','2ND ROW HEATED SEAT','XX4SC','w,w/o',''),(360,'2ND ROW SEAT','2ND ROW SEAT COMFORT FEATURE','XX4EMC','ALL',''),(361,'2ND ROW SEAT','2ND ROW SEAT HEATER AND COOLER','XX4EMC','ALL',''),(362,'2ND ROW SEAT','2ND ROW SEAT TYPE AND ADJUSTMENT','XX4EMC','ALL',''),(363,'2ND ROW SEAT','2ND ROW SEAT TYPE AND ADJUSTMENT.','XR6シートベルト','BENCH,SPRIT',''),(364,'2ND ROW SEAT','REAR SEAT','XR2車体信頼','ALL',''),(365,'2ND ROW SEAT','CENTER CONSOLE 2ND ROW','XX4EMC','2ND SUPER MULTI CONSOLE with RCP',''),(366,'2ND ROW SEAT','REAR SEAT ALERT','XR6乗員判別,XX4EMC','ALL',''),(367,'2ND ROW SEAT','RR SEAT HEATER','XX4WH','Ｗ',''),(368,'2ND ROW SEAT','Rr Heater Seat','XR5空調','with',''),(369,'2ND ROW SEAT','RR SEAT HEATER AND COOLER','XX4WH','Ｗ',''),(370,'2ND ROW SEAT','Rr 空調シート(Heater ＋ Cooler Seat)','XR5空調','with',''),(371,'2ND ROW SEAT','後席ODS仕様','XR6シートベルト','with,without',''),(372,'2ND ROW SEAT','後席シートスライド','XR6シートベルト','with,without',''),(373,'2ND ROW SEAT','後席シートリクライニング','XR6シートベルト','with,without',''),(374,'3rd ROW SEAT','3RD ROW SEAT TYPE AND ADJUSTMENT','XR6シートベルト','ALL',''),(375,'TRIM','SEAT LINING','XR6乗員判別,XQ4実車','ALL',''),(376,'TRIM','SEAT LINING.','XR6シートベルト','PUBLIC,SYNTHETIC LEATHER A,SYNTHETIC LEATHER B,SYNTHETIC LEATHER C',''),(377,'TRIM','シート材質','XR3シート,XX4ALARM,XD2材料','Cloth,Leather',''),(378,'2ND ROW STORAGE','2ND now  1','','',''),(379,'AMBIENT LIGHTING','Ambient lighting','XX4BCM','マルチカラー,モノかラー',''),(380,'AMBIENT LIGHTING','Ambient light','XX4ESS49','Mono color ambient,Multi color',''),(381,'AMBIENT LIGHTING','ZONES OF AMBIENT LIGHTING','XX4EMC','ALL',''),(382,'AMENITY','SOCKET ACCESSORY','XX4EMC','ALL',''),(383,'AMENITY','USB AND POWER SUPPLY','XX4NH電動車BATTERY HEATING','w_1500W,wo_1500W',''),(384,'AMENITY','USB AND POWER SUPPLY 2ND ROW','XX4EMC','ALL',''),(385,'AMENITY','USB AND POWER SUPPLY 3RD ROW','XX4EMC','ALL',''),(386,'AMENITY','USB AND POWER SUPPLY FR','XX4EMC','ALL',''),(387,'AMENITY','USB AND POWER SUPPLY LUGGAGE','XX4EMC','ALL',''),(388,'AMENITY','WIRELESS PHONE CHARGE','XX4EMC','ALL',''),(389,'AIR CONDITIONING AND HEATING','AIR CONDITIONER','XR5空調,XX4SC','AUTO A/C,ALL',''),(390,'AIR CONDITIONING AND HEATING','AIR CONDITIONING AND HEATING TYPE','XX4NH電動車,XX4EMC,XX4WH','ALL',''),(391,'AIR CONDITIONING AND HEATING','AIR CONDITIONING AND HEATING SYSTEM','XX4EMC,XQE電動車','ALL',''),(392,'AIR CONDITIONING AND HEATING','AIR CONTIONING AND HEATIN','XX4EMC','ALL',''),(393,'AIR CONDITIONING AND HEATING','BATTERY HEATING','XX4NH電動車,XQ5保安防災','(Water PTC),w',''),(394,'AIR CONDITIONING AND HEATING','HEATER FOR EV','XX4NH電動車','(AIR PTC)',''),(395,'AIR CONDITIONING AND HEATING','HEATER FOR EV / ADDITIONAL HEATER','XX4EMC','ALL',''),(396,'AIR CONDITIONING AND HEATING','PTC Heater','XX4BCM','w,w/o',''),(397,'AIR CONDITIONING AND HEATING','FULL AUTO A/C (TOUCH PANEL TYPE)','XX4EMC','ALL',''),(398,'AIR CONDITIONING AND HEATING','HEAT PUMP','XR5空調','w,w/o',''),(399,'AIR QUALITY MANAGEMENT','AIR TREATMENT','XX4EMC','ALL',''),(400,'AUDIO & NAVIGATION','-','XM6音質','Bose,Klipsch,Panasonic',''),(401,'AUDIO & NAVIGATION','ANTENNA','XM6アンテナ','200mm ROD,300mm ROD,800mm ROD,PILLAR,COWL TOP,SHARK FIN,ON GLASS\n(SIDE),ON GLASS\n(REAR),ON GLASS\n(BACK DOOR)',''),(402,'AUDIO & NAVIGATION','AUDIO','XM6音質,XX4AD','IVI,DA,レス',''),(403,'AUDIO & NAVIGATION','AUDIO & NAVIGATION','XX4WH','ALL',''),(404,'AUDIO & NAVIGATION','AUDIO & NAVIGATION / TYPES OF RADIOS','XM6アンテナ','ALL',''),(405,'AUDIO & NAVIGATION','AUDIO LESS','XX4GN1ラジオノイズ','w',''),(406,'AUDIO & NAVIGATION','Audio Navigation','XX4SV','GAS NAVI,DA',''),(407,'AUDIO & NAVIGATION','CCS2','XM6E2E','w',''),(408,'AUDIO & NAVIGATION','DISPLAY AUDIO','XX4GN1ラジオノイズ,XR4HMI','w',''),(409,'AUDIO & NAVIGATION','GALASS ANTENNA','XX4GN1ラジオノイズ','w',''),(410,'AUDIO & NAVIGATION','IVI','XX4BCM,XM6IVI,XR4HMI','w,w/o',''),(411,'AUDIO & NAVIGATION','IVI（NAVI/DA）','XM6メータ','NAVI,DA,Less',''),(412,'AUDIO & NAVIGATION','LOCAL NAVI','XX4GN1ラジオノイズ','w',''),(413,'AUDIO & NAVIGATION','NAVI','XX4GN1ラジオノイズ','w',''),(414,'AUDIO & NAVIGATION','Navi-size','XR6内外装','ALL',''),(415,'AUDIO & NAVIGATION','REAR VIDEO SCREENS','XX4EMC','ALL',''),(416,'AUDIO & NAVIGATION','ROD ANTENNA','XX4GN1ラジオノイズ','w',''),(417,'AUDIO & NAVIGATION','SHARK FIN ANTENNA','XX4GN1ラジオノイズ','w',''),(418,'AUDIO & NAVIGATION','TYPE OF HEAD UNIT HARDWARE & CCS SF','XX4EMC','ALL',''),(419,'AUDIO & NAVIGATION','HEAD UNIT','XM6アンテナ','NAVI,AUDIO,AUDIO LESS,NAVI READY',''),(420,'AUDIO & NAVIGATION','TYPES OF RADIOS','XX4CANGateway,XX4EMC','DA,NAVI,GAS NAVI,ALL',''),(421,'AUDIO & NAVIGATION','VIDEO SCREENS','XX4EMC','ALL',''),(422,'SPEAKERS','SPEAKER','XM6音質','ALL',''),(423,'SPEAKERS','BOSE','XX4GN1ラジオノイズ','w,w/o',''),(424,'SPEAKERS','BOSE SPEAKER','XX4WH','Ｗ',''),(425,'SPEAKERS','AUDIO SYSTEM','XX4HF-VR-ETC','BOSE,non-BOSE,Klipsch 24SP,Klipsch 14SP,Klipsch 12SP,SP Ω違い,CCS2.0 GAS,CCS2.0 non-GAS,DA2(CCS2 DA),A-IVI2 Ph1,CCS1.5 DA,LowDA (Plus),N18,P-IVI ST2.1/ST3.1\nA-IVI ST2.1/ST3.1',''),(426,'SOUND BUBBLE','sound bubble','XM6音質','ALL',''),(427,'NVH MANAGEMENT','ANC (ACTIVE NOISE CANCELLATION)','XX4EMC','ALL',''),(428,'NVH MANAGEMENT','ANC','XQ4実車','ALL',''),(429,'NVH MANAGEMENT','ANC / ACTIVE NOISE CANCELLATION / DRIVING SOUND CONTROL','XM6音質','ALL',''),(430,'NVH MANAGEMENT','ACTIVE SOUND CONTROL','XQ4実車','ALL',''),(431,'ACCESS','Central door locking','XX4スイッチ','central door lock SW (DR)',''),(432,'ACCESS','DOOR SAFETY','XX4EMC','ALL',''),(433,'ACCESS','FLUSH DOOR HANDLE','XX4メカトロS45','w',''),(434,'ACCESS','Flush handle','XX4BCM','w,w/o',''),(435,'ACCESS','I-KEY','XX4EMC','ALL',''),(436,'ACCESS','I-KEY (BADGE)','XX4EMC','ALL',''),(437,'ACCESS','Panic Alarm','XX4BCM','w,w/o',''),(438,'ACCESS','SAFETY ACCESS FUNCTIONS','XX4EMC','ALL',''),(439,'ACCESS','Speed sensing lock','XX4BCM','w,w/o',''),(440,'ACCESS','Touch Sensor  (I-key)','XX4BCM','w,w/o',''),(441,'ACCESS','通常のグリップ型アウトサイドハンドル、マニュアルヒドゥンハンドル','XX4Flush','',''),(442,'ACCESS','電動格納式フラッシュアウトサイドハンドル付','XX4Flush','',''),(443,'OPENING','AUTO CLOSER','XX4バックドアクロージャ―','ｗ',''),(444,'OPENING','E-DIMMING','XX4Sunroof','',''),(445,'OPENING','ELECTRICAL SIDE DOOR OPENING AND CLOSING','XX4EMC','ALL',''),(446,'OPENING','HAND FREE','XX4KickSensor','w','Kick Sensor'),(447,'OPENING','Kick Sensor','XX4BCM','w,w/o',''),(448,'OPENING','PBD','XX4BCM','w,w/o','Power Back Door'),(449,'OPENING','POWER BACK DOOR','XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ','w,w/o',''),(450,'OPENING','TAILGATE/TRUNK OPENING POWER OPEN/CLOSE','XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ','w,w/o',''),(451,'OPENING','TAILGATE/TRUNK OPENING POWER OPEN/CLOSE ✚ HANDS FREE','XX4GN1ラジオノイズ,XX4WH,XR3ドアクロ','w,w/o',''),(452,'OPENING','Power Back Door(PBD)','XX4メカトロS46','w',''),(453,'OPENING','Power Slide Door','XR3ドアクロ','',''),(454,'OPENING','Power Trunk','XR3ドアクロ','',''),(455,'OPENING','REAR DOOR OPENING','XX4EMC','ALL',''),(456,'OPENING','REAR GATE OPENING','XX4EMC','ALL',''),(457,'OPENING','ROOF / SUNROOF','XX4EMC,XR6乗員判定','ALL,Sun Roof,Glass Roof,Normal Roof',''),(458,'OPENING','ROOF','XQ4実車','ALL',''),(459,'OPENING','ROOF OPENING','XR2車体信頼','Sun Roof,Glass Roof,Normal Roof',''),(460,'OPENING','SUNROOF','XR3ドアクロ,XR5風音,XQ5保安防災,XX4ALARM,XX4BCM,XX4WH,XR6乗員判別','',''),(461,'OPENING','Sunshade','XX4BCM','E-sunshade,basic,w/o',''),(462,'OPENING','TAILGATE/TRUNK OPENING','XX4EMC','ALL',''),(463,'OPENING','TAILGATE/TRUNK OPENING\nPOWER OPEN/CLOSE','XX4PBD','w',''),(464,'OPENING','サンルーフ','XD2材料','w',''),(465,'LOGO & EMBLEM','Illumination BI','XL7外装','',''),(466,'BRAKING','ANTI-LOCK BRAKING SYSTEM','XX4EMC','ALL',''),(467,'BRAKING','BRAKING ASSISTANCE','XX4EMC','ALL',''),(468,'BRAKING','EMERGENCY BRAKE ASSIST (EBA / BA)','XX4EMC','ALL',''),(469,'BRAKING','RR BRAKE UNIT','XR2コントロール','',''),(470,'BRAKING','VDC','XX4EMC','ALL',''),(471,'BRAKING','VDC(ﾋﾞｰｸﾙ ﾀﾞｲﾅﾐｸｽ ｺﾝﾄﾛｰﾙ)','XQ4機構','',''),(472,'DRIVING MODE','Driving mode','XX4BCM','LINタイプ,ハードウェアタイプ','どちらか不明、自動車のボディ制御に使われる通信プロトコル「LIN」'),(473,'DRIVING MODE','DRIVING MODE 2WD','XX4EMC','ALL',''),(474,'DRIVING MODE','DRIVING MODE 4WD','XX4EMC','ALL',''),(475,'DRIVING MODE','DRIVING MODE CONTROL','XX4EMC','ALL',''),(476,'DRIVING MODE','ECONOMIC DRIVING','XX4EMC','ALL',''),(477,'TIRES','TIRE','XJBVDC,XX4ALARM,XQ2操安','',''),(478,'TIRES','TIRE PRESSURE MONITOR','XX4EMC','ALL',''),(479,'TIRES','TIRE PRESSURE MONITORING SYSTEM (TPMS)','XX4EMC','ALL',''),(480,'TIRES','TIRE TYPE','','',''),(481,'TIRES','TIRE SIZE','XQ5保安防災','',''),(482,'TIRES','TYPE OF TIRES FR','XR2車体信頼','ALL',''),(483,'TIRES','TYPE OF TIRES RR','XR2車体信頼','ALL',''),(484,'WHEELS & WHEEL COVERS','Wheel材質','XR2シャシー,XQ4車体','AL Wheel,Steel Wheel',''),(485,'WHEELS & WHEEL COVERS','Wheelサイズ','XR2シャシー,XQ4車体','ALL',''),(486,'WHEELS & WHEEL COVERS','WHEEL TYPE,SIZE','XQ4実車','ALL',''),(487,'WHEELS & WHEEL COVERS','Wheel Cover','XR2シャシー','with & 全種類',''),(488,'WHEELS & WHEEL COVERS','WHEEL COVERS-size','XR6内外装','ALL',''),(489,'SPARE WHEEL','SPARE WHEEL','XR2車体信頼','w',''),(490,'ADAS COMFORT','AD','XR6視界,XP4EVシステム','w',''),(491,'ADAS COMFORT','AD(AUTONOMOUS DRIVING)','XX4WH','ALL',''),(492,'ADAS COMFORT','AD1','XX4GN1ラジオノイズ','w,w/o',''),(493,'ADAS COMFORT','AD2','XJBVDC,XQ5Failsafe,XX4GN1ラジオノイズ,XM6アンテナ,XX4AD','w,w/o',''),(494,'ADAS COMFORT','ADAPTIVE CRUISE CONTROL (ACC)','XX4EMC,XX4WH','ALL,w',''),(495,'ADAS COMFORT','ASCD','UE2動力運転性,XP4EVシステム','w','オートスピードコントロール'),(496,'ADAS COMFORT','AUTONOMOUS DRIVING','XX4EMC,XM6メータ,UE2燃費,XX4EMC,XQ3AD,XX4CANGateway,XX4BCM,XX4EMC,XX4PT,XX4SV,XX4EMC,XX4PT','ALL,w/o,AD1,AD2',''),(497,'ADAS COMFORT','AUTONOMOUS DRIVING SF','XX4EMC','AD2 ✚ INFORMATION SUPPORT LIGHT AD LINK',''),(498,'ADAS COMFORT','CRUISE CONTROL','XX4EMC','ALL',''),(499,'ADAS COMFORT','CRUISE CONTROL/SPEED LIMI','XQ3AD','',''),(500,'ADAS COMFORT','CRUISE CONTROL/SPEED LIMITER','XX4EMC','ALL',''),(501,'ADAS COMFORT','DRIVING ASSITANCE','XX4EMC','ALL',''),(502,'ADAS COMFORT','ICC','XJBVDC','w,w/o',''),(503,'ADAS COMFORT','ICC(ｲﾝﾃﾘｼﾞｪﾝﾄ ｸﾙｰｽﾞ ｺﾝﾄﾛｰﾙ)','XQ4機構','',''),(504,'ADAS COMFORT','SPEED LIMITER','XX4EMC','ALL',''),(505,'ADAS COMFORT','プロパイロット','XQA商品性','','AD1,AD2'),(506,'ADAS COMFORT','Safety Driving','XX4AD','ACC,ICC,AD1,AD1e,AD1+Navilink,AD1e+Navilink',''),(507,'ADAS SAFETY','ADAPTIVE DRIVING BEAM (ADB)','XR6視界,XX4LEDHead','w,w/o',''),(508,'ADAS SAFETY','AFS','XR6視界','','アダプティブフロントライティングシステム'),(509,'ADAS SAFETY','AUTOMATIC EMERGENCY BRAKING SYSTEM  (AEBS)','XX4EMC','ALL',''),(510,'ADAS SAFETY','AUTONOMOUS EMERGENCY STEERING','XX4EMC','ALL',''),(511,'ADAS SAFETY','AUTONOMOUS EMERGENCY STEERING (AES)','XX4EMC','ALL',''),(512,'ADAS SAFETY','BACKWARD COLLISION PREVEN','XX4EMC','ALL',''),(513,'ADAS SAFETY','BLIND SPOT DETECTION','XX4EMC','ALL',''),(514,'ADAS SAFETY','BLIND SPOT INTERVENTION (BSI)','XQ3AD','',''),(515,'ADAS SAFETY','BLIND SPOT WARNING (BSW)','XQ3AD','',''),(516,'ADAS SAFETY','CITY ✚ REAR CROSS TRAFFIC ALERT (RCTA)','XQ3AD','',''),(517,'ADAS SAFETY','DRIVE EVENT RECORDER','XX4EMC','ALL',''),(518,'ADAS SAFETY','DRIVE RECORDER','XX4GN1ラジオノイズ,XX4CANGateway','w,w/o',''),(519,'ADAS SAFETY','DRIVER MONITORING','XX4EMC','ALL',''),(520,'ADAS SAFETY','driver monitoring by steering','XQ3AD','',''),(521,'ADAS SAFETY','DVR','XR6視界,XX4DVR','','ドライブレコーダー'),(522,'ADAS SAFETY','EMERGENCY ASSIST FOR PEDAL MISAPPLICATION','XQ3AD,XX4EMC','ALL',''),(523,'ADAS SAFETY','emergency steering assist/support (esa/ess)','XQ3AD','',''),(524,'ADAS SAFETY','ESS','XR6視界','','EMERGENCY STEERING ASSIST/SUPPORT (ESA/ESS)'),(525,'ADAS SAFETY','FORWARD COLLISION WARNING','XX4EMC','ALL',''),(526,'ADAS SAFETY','predictive forward collision warning (pfcw)','XQ3AD','',''),(527,'ADAS SAFETY','FORWARD EMERGENCY BRAKING','XQ3AD,XX4EMC,XX4AD','ALL',''),(528,'ADAS SAFETY','FRONT COLLISION WARNING','XQ3AD','',''),(529,'ADAS SAFETY','LANE DEPARTURE PREVENTION (LDP)','XQ3AD','',''),(530,'ADAS SAFETY','LANE DEPARTURE WARNING (LDW)','XQ3AD','',''),(531,'ADAS SAFETY','LANE KEEP','XQ3AD,XX4EMC','ALL',''),(532,'ADAS SAFETY','LATERAL SUPPORT SYSTEM','XX4EMC','ALL',''),(533,'ADAS SAFETY','OCCUPANT MONITORING','XX4EMC','ALL',''),(534,'ADAS SAFETY','OCCUPANTS SAFE EXIT','XX4EMC','ALL',''),(535,'ADAS SAFETY','REAR AEB','XQ3AD','',''),(536,'ADAS SAFETY','SCENE RECORDER','XX4EMC','ALL',''),(537,'ADAS SAFETY','TRAFFIC SIGN RECOGNITION','XX4EMC','ALL',''),(538,'ADAS SAFETY','TRAFFIC SIGN RECOGNITION (TSR)','XQ3AD','',''),(539,'ADAS SAFETY','TRAFFIC SIGN RECOGNITION / SPEED LIMITATION INFORMATION','XX4EMC','ALL',''),(540,'ADAS PARKING','AROUND VIEW MONITOR','XX4EMC,XQ3AD,XX4GN1ラジオノイズ,XX4WH,XM6camera','ALL,w',''),(541,'ADAS PARKING','AROUND VIEW MONITOR\n（AVM）','XR6視界','ALL',''),(542,'ADAS PARKING','AUTO PARKING REMOTE CONTROL','XX4GN1ラジオノイズ','w,w/o',''),(543,'ADAS PARKING','FAP（フルオートパーク）','UI6EV','w',''),(544,'ADAS PARKING','FR CAMERA','XL7外装,XR6内外装','w,w/o',''),(545,'ADAS PARKING','FR RADAR','XL7外装','',''),(546,'ADAS PARKING','FR SIDE RADAR','XL7外装','',''),(547,'ADAS PARKING','FR SIDE CAMERA','XL7外装','',''),(548,'ADAS PARKING','FR SONAR','XL7外装','',''),(549,'ADAS PARKING','MOVING OBJECT DETECTION (MOD)','XQ3AD','',''),(550,'ADAS PARKING','OUTSIDE CAMERA','XX4EMC','ALL',''),(551,'ADAS PARKING','PARK ASSIST','XX4EMC','ALL',''),(552,'ADAS PARKING','PARKING ALERTS','XX4EMC','ALL',''),(553,'ADAS PARKING','PARKING ASSIST SYSTEM','XQ3AD,XX4EMC','ALL',''),(554,'ADAS PARKING','Full FlanK Protection(FKP)','XX4SONAR','w',''),(555,'ADAS PARKING','PROXIMITY RADAR','XX4EMC','ALL',''),(556,'ADAS PARKING','REAR CAMERA','XX4GN1ラジオノイズ','w',''),(557,'ADAS PARKING','REAR VIEW CAMERA','XX4EMC,XM6camera','ALL',''),(558,'ADAS PARKING','REAR VIEW MONITOR\n（RVM）','XR6視界','ALL',''),(559,'ADAS PARKING','REMOTE PARKING','XX4BCM,XX4EMC','w,w/o,ALL',''),(560,'ADAS PARKING','RR CAMERA','XL7外装,XR6内外装','w,w/o',''),(561,'ADAS PARKING','RR SIDE RADAR','XL7外装','',''),(562,'ADAS PARKING','RR SONAR','XL7外装','',''),(563,'ADAS PARKING','SONER','XX4EMC','ALL',''),(564,'ADAS PARKING','プロパイロットパーク','XQA商品性','',''),(565,'WARNING & ALERT','Alarm type','XX4BCM','Perimeric,Volmatric',''),(566,'WARNING & ALERT','ANTI-THEFT DEVICES','XX7USM,XX4EMC','with,ALL',''),(567,'WARNING & ALERT','AUTO HAZARD','XR6視界','',''),(568,'WARNING & ALERT','DRIVER ATTENTION ALERT','XX4EMC,XQ3AD','ALL',''),(569,'WARNING & ALERT','EMERGENCY CALL AND BREAKDOWN','XX4EMC','ALL',''),(570,'WARNING & ALERT','EMERGENCY SIGNAL','XX4EMC','ALL',''),(571,'WARNING & ALERT','LEAD CAR DEPARTURE NOTIFICATION','XX4EMC','ALL',''),(572,'WARNING & ALERT','LEAD CAR DEPARTURE NOTIFICATION (LCDN)','XX4EMC','ALL',''),(573,'WARNING & ALERT','POST COLLISION AND BREAKDOWN','XX4EMC','ALL',''),(574,'AIRBAGS','AIRBAG CANCEL','XX4EMC','ALL',''),(575,'AIRBAGS','DRIVER\'S AIRBAG','XX4EMC','ALL',''),(576,'AIRBAGS','FAR SIDE AIRBAG','XX4EMC','ALL',''),(577,'AIRBAGS','FRONT AIRBAG','XX4EMC','ALL',''),(578,'AIRBAGS','FRONT KNEE AIRBAGS','XX4EMC','ALL',''),(579,'AIRBAGS','FRONT SIDE AIRBAG','XX4EMC','ALL',''),(580,'AIRBAGS','PASSENGER AIRBAG','XX4EMC','ALL',''),(581,'AIRBAGS','SIDE AIRBAG','XX4EMC','ALL',''),(582,'AIRBAGS','SIDE CURTAIN AIRBAG','XX4EMC','ALL',''),(583,'SEAT BELT','FRONT SEAT BELT','XX4EMC,XR6シートベルト','ALL',''),(584,'SEAT BELT','FRONT SEAT BELT REMINDER','XX4EMC,XR6シートベルト','ALL',''),(585,'SEAT BELT','FRONT SEAT BELT PRETENSIONER','XX4EMC','ALL',''),(586,'SEAT BELT','FRONT SEAT BELT PRE-TENSIONER','XX4EMC','ALL',''),(587,'SEAT BELT','FRONT SEAT BELT ADJUSTMEN','XX4EMC','ALL',''),(588,'SEAT BELT','SEAT BELT REMINDER','XX4EMC','ALL',''),(589,'SEAT BELT','2ND ROW SEAT BELT','XX4EMC,XR6シートベルト','ALL',''),(590,'SEAT BELT','2ND ROW SEAT BELT REMINDER','XX4EMC,XR6シートベルト','ALL',''),(591,'SEAT BELT','2ND ROW SEAT BELT REMINDER OCS','XR6シートベルト','w.w/o',''),(592,'SEAT BELT','REAR SEATS BELT','XX4EMC','ALL',''),(593,'SEAT BELT','REAR CNTER SEAT BELT','XX4EMC','ALL',''),(594,'SEAT BELT','REAR SEAT BELT PRETENSIONER','XX4EMC','ALL',''),(595,'SEAT BELT','ASSISTANT SEAT BELT','XX4EMC','ALL',''),(596,'SEAT BELT','3RD ROW SEAT BELT','XX4EMC,XR6シートベルト','ALL',''),(597,'SEAT BELT','3RD ROW SEAT BELT REMINDER','XX4EMC','ALL',''),(598,'SEAT BELT','SEAT BELT NOT SECURED WAR','XX4EMC','ALL',''),(599,'SEAT BELT','前席ELR仕様','XR6シートベルト','LLA,LLD,PSB','Emergency Locking Retractorチャイルドシート用'),(600,'SEAT BELT','Lapプリテン装備','XR6シートベルト','with,without','運転席プリテンショナ'),(601,'SEAT BELT','後席プリテン装備','XR6シートベルト','with,without',''),(602,'OTHER','HORN','XR6視界','',''),(603,'OTHER','UNIVERSAL GARAGE DOOR OPENER','XX4GN1ラジオノイズ','w,w/o',''),(604,'OTHER','UNIVERSAL GARAGE DOOR OPE','XX4EMC','ALL',''),(605,'CHARGER','AC 120V or 240V 1500W OUTLET','XX4WH','Ｗ',''),(606,'CHARGER','AC CHARGER','XX4EMC','',''),(607,'CHARGER','AC PLUG STANDARD','XX4EMC,XX4NH電動車','MODE 2 CABLE\n100V/120V,MODE 2 CABLE\n200V /230V/240V,MODE 3 CABLE',''),(608,'CHARGER','Battery Charger For ELEC. VEH','UE2燃費','ALL',''),(609,'CHARGER','CHARGER','XX4NH電動車','SINGLE,3PHASE',''),(610,'CHARGER','DC CHARGER','XX4EMC','',''),(611,'CHARGER','PLUG AND CHARGE','XX4EMC','',''),(612,'CHARGER','REVERSIBLE CHARGER','XX4NH電動車,XX4EMC','VEHICLE TO LOAD (V2L) OUTSIDE',''),(613,'CHARGER','VEHICLE TO LOAD (V2L) OUTSIDE','XP4充電','w',''),(614,'CHARGER','三相(AC3)','XX4HF-VR-ETC','AC3',''),(615,'CHARGER','単相(AC1)','XX4HF-VR-ETC','AC1',''),(616,'EV DEDICATED FEATURES','EV SOUND FOR PEDESTRIANS','XX4EMC','ALL',''),(617,'EV DEDICATED FEATURES','ONE PEDAL FUNCTION WITH STOP','XX4EMC','ALL',''),(618,'EV DEDICATED FEATURES','Vehicle_ 1','','',''),(619,'EV DEDICATED FEATURES','VEHICLE SOUND FOR PEDESTRIANS','XX7USM','with','');
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
INSERT INTO `information_project` VALUES ('AXLE','','',''),('BODY','','',''),('CCM','XQA商品性','',''),('ENGINE','XX4PT','KH1T',''),('GRADE','','',''),('HANDLE','','',''),('INTAKE','XX4NH電動車,XX4PT','BATTERY (MIDDLE),DIESEL,FFV,HEV/E-PWR,','FFV:Flexible-fuel vehicle混合燃料車'),('NUMBER','','',''),('SEAT','','',''),('TRANS','XX4PT,XX4AD','CVT,7AT/9AT,DCT,ATM (for EV)',''),('YEAR','','',''),('ZONE','','','');
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
INSERT INTO `lot` VALUES (3,'DC-lot'),(1,'DS-lot'),(4,'PFC-lot');
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

-- Dump completed on 2024-06-28 10:59:01
