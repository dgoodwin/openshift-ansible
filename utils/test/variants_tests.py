# pylint: disable=missing-docstring
"""
Tests for the variants module.
"""

from test.oo_config_tests import OOInstallFixture
from ooinstall import variants

class VersionDocsUrlTests(OOInstallFixture):

    def test_version_docs_url(self):
        ose30 = variants.OSE.versions[0]
        expected = variants.DOCS_BASE_URL + '/enterprise/3.0/admin_guide/install/prerequisites.html'
        self.assertEquals(expected,
                          ose30.get_docs_url('admin_guide/install/prerequisites.html'))
        self.assertEquals(expected,
                          ose30.get_docs_url('/admin_guide/install/prerequisites.html'))

