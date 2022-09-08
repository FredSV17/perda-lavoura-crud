CREATE DATABASE loss_db;
USE loss_db;
CREATE TABLE `loss_db`.`loss`(
    `id` INT NOT NULL AUTO_INCREMENT,
    `producer_name` VARCHAR(255),
    `producer_email` VARCHAR(255),
    `producer_cpf` VARCHAR(255),
    `crop_local` VARCHAR(255),
    `harvest_date` datetime,
    `crop_type` VARCHAR(255),
    `event_type` VARCHAR(255),
    PRIMARY KEY(ID)
);
