import unittest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import Sequences


class TestBase(TestCase):

	def create_app(self):
		config_name = "testing"
		app.config.update(SQLALCHEMY_DATABASE_URI="mysql+pymysql://"+str(getenv("MYSQL_USER"))+":"+str(getenv("MYSQL_PASSWORD"))+"@"+str(getenv("MYSQL_HOST"))+"/"+str(getenv("MYSQL_DB_TEST")))
		return app

	def setUp(self):
		db.drop_all()
		db.create_all()

		db.session.commit()

	def tearDown(self):
		db.session.remove()
		db.drop_all()


class Test_app(TestBase):

	def test_home_page_view(self):
		response = self.client.get(url_for("home"))
		self.assertEqual(response.status_code, 200)

	def test_coverage_page_view(self):
		response = self.client.get(url_for("coverage"))
		self.assertEqual(response.status_code, 200)

	def test_getPrize_page_view(self):
		response = self.client.get(url_for("button1"))
		self.assertEqual(response.status_code, 200)

	def test_database_insert(self):
		sequence_dummy = "7asdf34trg89"
		sequence_db = Sequences( sequence=sequence_dummy, submitted=0 )
		db.session.add(sequence_db)
		db.session.commit()

		sequence_entry = Sequences.query.filter_by( sequence=sequence_dummy ).first()
		self.assertEqual(sequence_dummy, sequence_entry.sequence)

	def test_database_update(self):
		sequence_dummy = "7a3desdf34trg89"
		sequence_dummy2 = "7a3de4dfdf34df45s9"
		sequence_db = Sequences( sequence=sequence_dummy, submitted=0 )
		db.session.add(sequence_db)
		db.session.commit()

		sequence_entry = Sequences.query.filter_by( sequence=sequence_dummy ).first()
		sequence_entry.sequence = sequence_dummy2
		db.session.commit()

		sequence_entry = Sequences.query.filter_by( sequence=sequence_dummy2 ).first()
		self.assertEqual(sequence_dummy2, sequence_entry.sequence)
