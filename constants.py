db_name = "TakeNote"
host="localhost"
user="root"
password="password"


note_table = "NOTES"
user_table="USERS"

YES="YES"
NO="NO"
create_note_table = """
    USE `%s`;
    CREATE TABLE IF NOT EXISTS `%s` (
    `id_note` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `athour` VARCHAR(50) COLLATE utf8_general_ci NOT NULL,
    `description` TEXT(100) COLLATE utf8_general_ci NOT NULL,
    `content` TEXT COLLATE utf8_general_ci NOT NULL,
    `created_at` DATE NOT NULL,
    `updated_at` DATE NOT NULL,
PRIMARY KEY (`id_note`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci AUTO_INCREMENT=1 ;
""" % (db_name, note_table)

crate_db_note = """
    CREATE DATABASE IF NOT EXISTS `%s`
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;""" % db_name


create_users_table = """
    USE `%s`;
    CREATE TABLE IF NOT EXISTS `%s` (
    `id_user` INT UNSIGNED NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(50) COLLATE utf8_general_ci NOT NULL,
    `password` VARCHAR(50) COLLATE utf8_general_ci NOT NULL,
    `created_at` DATE NOT NULL,
    `updated_at` DATE NOT NULL,
    `isLoggedIn` VARCHAR(10) NOT NULL,
PRIMARY KEY (`id_user`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci AUTO_INCREMENT=1 ;
""" % (db_name, user_table)

