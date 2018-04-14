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

INSERT INTO twitter_users (account_name, bot_score, is_bot)
VALUES ('@barackobama', 0.60, false);

INSERT INTO twitter_users (account_name, bot_score, is_bot)
VALUES ('@washingtonpost', 0.50, false);

INSERT INTO twitter_users (account_name, bot_score, is_bot)
VALUES ('@justdiedbot', 0.51, true);

CREATE TABLE IF NOT EXISTS sentiment_scores (
    id INT unique AUTO_INCREMENT,
    company_ticker VARCHAR(45),
    company_name VARCHAR(45),
    alpha_score FLOAT(3,2),
    twitter_score VARCHAR(8),
    sample_tweet VARCHAR(280),
    score_date DATETIME
);

INSERT INTO sentiment_scores (company_ticker, company_name, alpha_score, 
			      twitter_score, sample_tweet, score_date)
VALUES ('TSLA', 'Tesla', 0.08, 'positive', 'dude why would Tesla not make the model 3 That s the whole point of business Ur logo everywhere It s shiny', NOW())



