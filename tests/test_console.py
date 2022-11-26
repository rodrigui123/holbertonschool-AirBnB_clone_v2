#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
from models.base_model import BaseModel
from models import storage
import console
from unittest.mock import patch
from io import StringIO
import os


class test_console(unittest.TestCase):
    """ Class to test the console"""

    def test_emptyline(self):
        console_test = console.HBNBCommand
        self.assertTrue(console_test("\n"), 'pass')
