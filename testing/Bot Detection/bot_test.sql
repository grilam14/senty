CREATE DATABASE IF NOT EXISTS project;

USE project;

CREATE TABLE IF NOT EXISTS twitter_users (
    user_id INT unique AUTO_INCREMENT,
    account_id BIGINT,
    account_name VARCHAR(16),
    bot_score float(3,2),
    is_bot BOOL,
    PRIMARY KEY (user_id)
);

INSERT INTO twitter_users (account_name, account_id, bot_score, is_bot)
VALUES ('@BossHoggHazzard', 3057886001, 0.38, false);

INSERT INTO twitter_users (account_name, bot_score, is_bot)
VALUES ('@EggRetweet', 4776757226, 0.46, true);