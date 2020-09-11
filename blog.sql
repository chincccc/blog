/*
 Navicat Premium Data Transfer

 Source Server         : chin
 Source Server Type    : MySQL
 Source Server Version : 80017
 Source Host           : localhost:3306
 Source Schema         : blog

 Target Server Type    : MySQL
 Target Server Version : 80017
 File Encoding         : 65001

 Date: 11/09/2020 20:47:11
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `article_id` varchar(20) NOT NULL,
  `article_title` varchar(100) NOT NULL,
  `article_text` text,
  `article_summary` varchar(255) DEFAULT NULL,
  `article_read_cnt` int(11) DEFAULT NULL,
  `article_sc` int(11) DEFAULT NULL,
  `article_pl` int(11) DEFAULT NULL,
  `article_date` datetime DEFAULT NULL,
  `article_url` text,
  `article_type` varchar(10) DEFAULT NULL,
  `article_author` varchar(20) DEFAULT NULL,
  `user_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`article_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of article
-- ----------------------------
BEGIN;
INSERT INTO `article` VALUES ('2020061100000002', '12122', '<p>222</p>', '222', 33, 10, 1, '2020-06-11 17:56:23', 'https://pan.chincc.tk/nn.png', '科技区', 'admin', '2020061100000003');
INSERT INTO `article` VALUES ('2020061200000003', ' 测试', '<p>测试测试</p>', '测试测试', 19, 10, 4, '2020-06-12 08:07:20', 'https://pan.chincc.tk/38c871985574fba3.jpg', '科技区', 'chin', '2020061100000002');
INSERT INTO `article` VALUES ('2020061200000004', '服服服', '<p>saassss111a</p>', 'saassss111a', 30, 1, 2, '2020-06-12 08:45:40', 'https://pan.chincc.tk/38c871985574fba3.jpg', '生活区', 'admin', '2020061100000003');
INSERT INTO `article` VALUES ('2020061200000005', 'tttt', '<p>saasa</p>', 'saasa', 1, 0, 0, '2020-06-12 08:55:25', 'https://pan.chincc.tk/nn.png', '生活区', 'admin', '2020061100000003');
INSERT INTO `article` VALUES ('2020061200000006', '11554', '<p>2wqwqw</p>', '2wqwqw', 1, 0, 0, '2020-06-12 08:56:24', 'https://pan.chincc.tk/38c871985574fba3.jpg', '生活区', 'admin', '2020061100000003');
INSERT INTO `article` VALUES ('2020061200000007', 'ttttssasasas', '<p>sasaasasasas</p>', 'sasaasasasas', 0, 0, 0, '2020-06-12 10:41:32', 'https://pan.chincc.tk/38c871985574fba3.jpg', '生活区', 'chincc', '2020061200000004');
INSERT INTO `article` VALUES ('2020061200000008', 'dsfsfsff', '<p>fsfsfs</p>', 'fsfsfs', 3, 0, 1, '2020-06-12 10:54:01', 'https://pan.chincc.tk/38c871985574fba3.jpg', '科技区', 'admin', '2020061100000003');
INSERT INTO `article` VALUES ('2020061800000015', '121222121', '<p>2121</p>', '2121', 1, 0, 0, '2020-06-18 20:03:11', 'https://pan.chincc.tk/38c871985574fba3.jpg', '科技区', 'hhhh', '20200611000000012');
INSERT INTO `article` VALUES ('2020061800000016', 'wqwqqw', '<p>eewewew</p>', 'eewewew', 0, 0, 0, '2020-06-18 20:03:27', 'https://pan.chincc.tk/38c871985574fba3.jpg', '科技区', 'hhhh', '20200611000000012');
INSERT INTO `article` VALUES ('2020061900000019', '打发打发地方', '<p>地方的</p>', '地方的', 0, 0, 0, '2020-06-19 14:52:32', 'https://pan.chincc.tk/38c871985574fba3.jpg', '科技区', 'chin', '2020061100000002');
COMMIT;

-- ----------------------------
-- Table structure for comment
-- ----------------------------
DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `comment_id` varchar(20) NOT NULL,
  `comment_text` text,
  `comment_date` datetime DEFAULT NULL,
  `article_id` varchar(20) NOT NULL,
  `comment_name` varchar(30) DEFAULT NULL,
  `comment_support` int(11) DEFAULT NULL,
  `comment_oppose` int(11) DEFAULT NULL,
  `user_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of comment
-- ----------------------------
BEGIN;
INSERT INTO `comment` VALUES ('2020061200000003', '<p>222</p>', '2020-06-12 08:31:10', '2020061200000003', 'test', 0, 0, NULL);
INSERT INTO `comment` VALUES ('2020061200000004', '<p>啥啥啥</p>', '2020-06-12 08:37:23', '2020061200000003', 'xjcc', 0, 0, NULL);
INSERT INTO `comment` VALUES ('2020061200000005', '<p>辅导辅导</p>', '2020-06-12 12:00:48', '2020061200000004', '风景好看', 1, 7, NULL);
INSERT INTO `comment` VALUES ('2020061800000004', '<p>sssss</p>', '2020-06-18 13:07:58', '2020061200000004', '', 0, 0, NULL);
INSERT INTO `comment` VALUES ('2020061800000005', '<p>我问问v</p>', '2020-06-18 15:32:40', '2020061100000002', '许家草草', 0, 0, NULL);
INSERT INTO `comment` VALUES ('2020061800000006', '<p>2111212</p>', '2020-06-18 15:37:10', '2020061200000003', '许家草草', 0, 0, '2020061100000002');
INSERT INTO `comment` VALUES ('2020061800000007', '<p>好久好久好久好久</p>', '2020-06-18 15:38:44', '2020061200000003', '许家草草', 1, 0, '2020061100000002');
INSERT INTO `comment` VALUES ('2020062000000009', '<p>2.5</p>', '2020-06-20 12:39:08', '2020062000000020', '辅导辅导', 0, 0, '2020061100000003');
COMMIT;

-- ----------------------------
-- Table structure for commparam
-- ----------------------------
DROP TABLE IF EXISTS `commparam`;
CREATE TABLE `commparam` (
  `param_name` varchar(10) NOT NULL,
  `param_value` int(11) DEFAULT NULL,
  `param_text` varchar(100) DEFAULT NULL,
  `param_stat` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`param_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of commparam
-- ----------------------------
BEGIN;
INSERT INTO `commparam` VALUES ('article', 20, NULL, '0');
INSERT INTO `commparam` VALUES ('comment', 9, NULL, '0');
INSERT INTO `commparam` VALUES ('task', 7, NULL, '0');
INSERT INTO `commparam` VALUES ('user', 13, NULL, '0');
COMMIT;

-- ----------------------------
-- Table structure for task
-- ----------------------------
DROP TABLE IF EXISTS `task`;
CREATE TABLE `task` (
  `task_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `task_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `start_dt` datetime DEFAULT NULL,
  `content` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `stat` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `user_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`task_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of task
-- ----------------------------
BEGIN;
INSERT INTO `task` VALUES ('2020061200000003', '111', '2020-06-12 00:00:00', '<p>wqwqw</p>', '已完成', '2020061100000003');
INSERT INTO `task` VALUES ('2020061200000004', 'sasa', '2020-06-12 00:00:00', '<p>sasaasa</p>', '已完成', '2020061100000003');
INSERT INTO `task` VALUES ('2020061800000005', '吃饭', '2020-06-18 00:00:00', '<p>今天下午吃饭</p>', '已完成', '2020061100000002');
INSERT INTO `task` VALUES ('2020062000000007', '情人玩一天我去过的v啊就好康师傅的', '2020-06-20 00:00:00', '', '进行中', '20200611000000012');
COMMIT;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user_id` varchar(20) NOT NULL,
  `user_name` varchar(30) DEFAULT NULL,
  `nickname` varchar(40) DEFAULT NULL,
  `sex` varchar(4) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `birthdate` date DEFAULT NULL,
  `user_crt_dt` datetime DEFAULT NULL,
  `attention_cnt` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `nickname` (`nickname`),
  UNIQUE KEY `user_name` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES ('20200611000000012', 'hhhh', '啥', '女', 21, 'pbkdf2:sha256:50000$U6wC1dHn$18e9e6e119d23647c5e75c665e69438f098c9812a13b78adb8552630b898fbea', 'chin1111111.cc@qq.com', '2020-06-06', '2020-06-18 19:57:00', 0);
INSERT INTO `user` VALUES ('2020061100000002', 'chin', '许家草草', '男', 20, 'pbkdf2:sha256:50000$Fi9zCdcV$78388a0d9970e07ec29558c0b55350252cbf73ddc4408be77bd108a645681754', 'chin.cc@chincc.tk', '1999-10-01', '2020-06-18 00:18:06', 0);
INSERT INTO `user` VALUES ('2020061100000003', 'admin', '辅导辅导', '男', 22, 'pbkdf2:sha256:50000$9ZEulUL6$04f49cfbec341337c32d78988aff174283a75a19e9487cd02c892310a9fa89ef', 'chin.cc@outlook.in', '1999-11-01', '2020-06-14 10:32:00', 0);
INSERT INTO `user` VALUES ('2020061200000004', 'chincc', 'v方法', '女', 23, 'pbkdf2:sha256:50000$Y7TRO7qr$fd07b8a1b1474c38bbb15f10bb201ad1730fbd0ecb642b7a68ba06e7c2f100d9', 'chin.cc@qq.com', '1991-10-01', '2020-06-16 19:44:40', 0);
INSERT INTO `user` VALUES ('2020061200000005', 'pppp', '费工夫', '男', 21, 'pbkdf2:sha256:50000$nXMIx0bO$0fc659d11bb2f2da87ed2311ffdf2017b30fe9fffe9e6c9394a0500483b5c452', 'chincc@qq.com', '1999-12-01', '2020-06-17 23:18:00', 0);
INSERT INTO `user` VALUES ('2020061200000008', '111111', '二二', '男', 12, 'pbkdf2:sha256:50000$yLnc1MSm$4437e1f19842442da689e11944b1f449b376a500ad493f7cdb3149a745f101b5', '74111444015@qq.com', '1979-10-01', '2020-06-18 00:18:00', 0);
INSERT INTO `user` VALUES ('2020061200000009', '22222', 'VC', '女', 122, 'pbkdf2:sha256:50000$gp90URBN$4deb21f786433b80d93059ad61d10b9cf25a077a2930e70c1393af2a679320e5', '7411444015@qq.com', '1999-10-21', '2020-06-18 00:18:00', 0);
INSERT INTO `user` VALUES ('2020061200000010', 'chin111111', '啥味', '女', 45, 'pbkdf2:sha256:50000$vuCiB4qO$be1091002eceb474ad4542423921dc29134113d87986441b924142f1d6e6e774', '17411444015@qq.com', '1999-10-11', '2020-06-18 00:18:00', 0);
INSERT INTO `user` VALUES ('2020061200000011', 'chin12', '二', '男', 55, 'pbkdf2:sha256:50000$Lsm37AMA$eef35299521897435d0de6f2ef0a76d1068817916717ac18f7ee3be6fdca6d62', '11117411444015@qq.com', '1999-05-01', '2020-06-17 22:18:00', 0);
INSERT INTO `user` VALUES ('2020061700000012', 'user2', '最小值', '男', 66, 'pbkdf2:sha256:50000$j0TEp3KN$bd5b24c5af492af4bb1d253aea04e2996e2748558a42f16ea698a34c47e42948', '123@111.com', '1999-10-07', '2020-06-18 00:14:00', 0);
INSERT INTO `user` VALUES ('2020061800000010', 'qqq11', 'wwww', '女', 14, 'pbkdf2:sha256:50000$uOE8ne0p$2810e01934313fab33e86cd63d3397fe1e4a12ccb47cf388af50ed4f83fad513', 'qqq1q1123@111.com', '2010-06-06', '2020-06-18 00:18:00', 0);
INSERT INTO `user` VALUES ('2020061800000011', 'uuuu', '啥色玩', '女', 11, 'pbkdf2:sha256:50000$7zHGArvL$6677247dd953672cea2e2b4d62c5a4e60ee2abaf1029603749dc2c9206018b51', '111111123@111.com', '2020-06-06', '2020-06-18 15:56:00', 0);
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
