-- MySQL dump 10.13  Distrib 5.5.42, for osx10.6 (i386)
--
-- Host: localhost    Database: quixotic_etl
-- ------------------------------------------------------
-- Server version	5.5.42

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
-- Table structure for table `event`
--

DROP TABLE IF EXISTS `event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start` datetime NOT NULL,
  `end` datetime DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `detail` varchar(255) DEFAULT NULL,
  `tags` varchar(255) DEFAULT NULL,
  `features` varchar(255) DEFAULT NULL,
  `relevant` tinyint(4) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `redaction` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `dedupe` (`start`,`title`,`tags`)
) ENGINE=InnoDB AUTO_INCREMENT=130440 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `events_by_day`
--

DROP TABLE IF EXISTS `events_by_day`;
/*!50001 DROP VIEW IF EXISTS `events_by_day`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `events_by_day` (
  `event_count` tinyint NOT NULL,
  `tags` tinyint NOT NULL,
  `event_day` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `events_by_day2`
--

DROP TABLE IF EXISTS `events_by_day2`;
/*!50001 DROP VIEW IF EXISTS `events_by_day2`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `events_by_day2` (
  `event_count` tinyint NOT NULL,
  `tags` tinyint NOT NULL,
  `event_day` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `events_by_hour`
--

DROP TABLE IF EXISTS `events_by_hour`;
/*!50001 DROP VIEW IF EXISTS `events_by_hour`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `events_by_hour` (
  `event_count` tinyint NOT NULL,
  `tags` tinyint NOT NULL,
  `event_hour` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `events_by_hour2`
--

DROP TABLE IF EXISTS `events_by_hour2`;
/*!50001 DROP VIEW IF EXISTS `events_by_hour2`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `events_by_hour2` (
  `event_count` tinyint NOT NULL,
  `tags` tinyint NOT NULL,
  `event_hour` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `settings`
--

DROP TABLE IF EXISTS `settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `settings` (
  `user_id` int(11) NOT NULL,
  `show_deleted` tinyint(4) DEFAULT NULL,
  `show_personal` tinyint(4) DEFAULT NULL,
  `show_fluff` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `timeblock`
--

DROP TABLE IF EXISTS `timeblock`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `timeblock` (
  `start` datetime NOT NULL,
  `end` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  `verified` tinyint(4) DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL,
  `billable` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`start`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `timeline`
--

DROP TABLE IF EXISTS `timeline`;
/*!50001 DROP VIEW IF EXISTS `timeline`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `timeline` (
  `id` tinyint NOT NULL,
  `start` tinyint NOT NULL,
  `end` tinyint NOT NULL,
  `title` tinyint NOT NULL,
  `detail` tinyint NOT NULL,
  `tags` tinyint NOT NULL,
  `features` tinyint NOT NULL,
  `relevant` tinyint NOT NULL,
  `user_id` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `name` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Final view structure for view `events_by_day`
--

/*!50001 DROP TABLE IF EXISTS `events_by_day`*/;
/*!50001 DROP VIEW IF EXISTS `events_by_day`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `events_by_day` AS select count(`event`.`id`) AS `event_count`,`event`.`tags` AS `tags`,date_format(`event`.`start`,'%Y-%m-%d') AS `event_day` from `event` group by date_format(`event`.`start`,'%Y-%m-%d'),`event`.`tags` order by date_format(`event`.`start`,'%Y-%m-%d') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `events_by_day2`
--

/*!50001 DROP TABLE IF EXISTS `events_by_day2`*/;
/*!50001 DROP VIEW IF EXISTS `events_by_day2`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `events_by_day2` AS select count(`event`.`id`) AS `event_count`,`event`.`tags` AS `tags`,str_to_date(date_format(`event`.`start`,'%Y-%m-%d'),'%Y-%m-%d %H:00:00') AS `event_day` from `event` group by str_to_date(date_format(`event`.`start`,'%Y-%m-%d'),'%Y-%m-%d %H:00:00'),`event`.`tags` order by str_to_date(date_format(`event`.`start`,'%Y-%m-%d'),'%Y-%m-%d %H:00:00') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `events_by_hour`
--

/*!50001 DROP TABLE IF EXISTS `events_by_hour`*/;
/*!50001 DROP VIEW IF EXISTS `events_by_hour`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `events_by_hour` AS select count(`event`.`id`) AS `event_count`,`event`.`tags` AS `tags`,(date_format(`event`.`start`,'%Y-%m-%d %H:00:00') + interval if((minute(`event`.`start`) < 30),0,1) hour) AS `event_hour` from `event` group by (date_format(`event`.`start`,'%Y-%m-%d %H:00:00') + interval if((minute(`event`.`start`) < 30),0,1) hour),`event`.`tags` order by (date_format(`event`.`start`,'%Y-%m-%d %H:00:00') + interval if((minute(`event`.`start`) < 30),0,1) hour) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `events_by_hour2`
--

/*!50001 DROP TABLE IF EXISTS `events_by_hour2`*/;
/*!50001 DROP VIEW IF EXISTS `events_by_hour2`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `events_by_hour2` AS select count(`event`.`id`) AS `event_count`,`event`.`tags` AS `tags`,str_to_date((date_format(`event`.`start`,'%Y-%m-%d %H:00:00') + interval if((minute(`event`.`start`) < 30),0,1) hour),'%Y-%m-%d %H:00:00') AS `event_hour` from `event` group by str_to_date((date_format(`event`.`start`,'%Y-%m-%d %H:00:00') + interval if((minute(`event`.`start`) < 30),0,1) hour),'%Y-%m-%d %H:00:00'),`event`.`tags` order by str_to_date((date_format(`event`.`start`,'%Y-%m-%d %H:00:00') + interval if((minute(`event`.`start`) < 30),0,1) hour),'%Y-%m-%d %H:00:00') */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `timeline`
--

/*!50001 DROP TABLE IF EXISTS `timeline`*/;
/*!50001 DROP VIEW IF EXISTS `timeline`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `timeline` AS select `event`.`id` AS `id`,`event`.`start` AS `start`,`event`.`end` AS `end`,`event`.`title` AS `title`,`event`.`detail` AS `detail`,`event`.`tags` AS `tags`,`event`.`features` AS `features`,`event`.`relevant` AS `relevant`,`event`.`user_id` AS `user_id` from `event` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-05-05 14:54:33
