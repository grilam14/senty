import bot_detect
import unittest

class bot_detectTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_check_db(self):
    	detecto = bot_detect.BotDetector()

    	user_id = 3057886001 # id for twitter user @BossHoggHazzard, present in db
    	result = detecto.check_db(user_id)
    	self.assertEqual(result[1], 0, "check_db() does not return values correctly for found account")
    	
    	user_id = 11111111 # fake twitter user id, should not be found in db
    	result = detecto.check_db(user_id)
    	self.assertEqual(result, None, "check_db() does not return correct value for account unfound account")


    def test_bot_check(self):
    	detecto = bot_detect.BotDetector()

    	user_id = 25073877 # @realdonaldtrump, not in db, should be identified as human
    	user = detecto.get_user(user_id)
    	result = detecto.bot_check(user)
    	self.assertEqual(result, False, "bot_check() does not identify known human account")

    	user_id = 3057886001 # @BossHoggHazzard, in db, not a bot
    	user = detecto.get_user(user_id)
    	result = detecto.bot_check(user)
    	self.assertEqual(result, False, "bot_check() does not identify human account from db")

    	user_id = 4776757226 # @EggRetweet, present in db, is a bot
    	user = detecto.get_user(user_id)
    	result = detecto.bot_check(user)
    	self.assertEqual(result, True, "bot_check() does not identify bot accounts from db")


if __name__ == '__main__':
	unittest.main()
