#!/usr/bin/env python3
"""testing module for GithubOrgClient in client.py"""

from unittest import TestCase
from unittest.mock import Mock, patch
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import json
from unittest import TestCase


class TestGithubOrgClient(TestCase):
    """class for testing GithubOrgClient class"""

    @parameterized.expand([
        ("googel", {"name": "google"}),
        ("abc", {"name": "abc"}),
    ])
    @patch('client.get_json')
    def test_org(self, org, res, mock_get_json):
        """test org method"""
        mock_get_json.return_value = Mock(return_value=res)
        github_client = GithubOrgClient(org)
        self.assertEqual(github_client.org(), res)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, exptected):
        """test has_license method"""
        github_client = GithubOrgClient("my org")
        client_has_license = github_client.has_license(repo, license_key)
        self.assertEqual(client_has_license, exptected)

@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(TestCase):
    """ Class for Integration test of fixtures """

    @classmethod
    def setUpClass(cls):
        """A class method called before
        tests in an individual class are run"""

        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)

        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """ Integration test: public repos"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """ Integration test for
        public repos with License """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """A class method called after
        tests in an individual class have run"""
        cls.get_patcher.stop()