import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app


class TestBase(TestCase):

	def create_app(self):
		config_name = "testing"
		#app.config.update(SQLALCHEMY_DATABASE_URI="mysql+pymysql://"+str(getenv("MYSQL_USER"))+":"+str(getenv("MYSQL_PASSWORD"))+"@"+str(getenv("MYSQL_HOST"))+"/"+str(getenv("MYSQL_DB_TEST")))
		return app

	def setUp(self):
		pass

	def tearDown(self):
		pass

class Test_app(TestBase):

	def test_home_page_view(self):
		#response = self.client.post(url_for("getSequence"))
		#self.assertEqual(response.status_code, 200)
		pass
