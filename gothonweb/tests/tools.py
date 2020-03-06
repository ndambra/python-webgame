from nose.tools import *
import re

def assert_response(resp, contains=None, matches=None, headers=None, status="200"):

    assert status in resp.status, "Expected response {} not in {}".format(status, resp.status)

    if status == "200":
        assert resp.data, "Response data is empty."

    if contains:
        contains = contains.encode()
        assert contains in resp.data, "Response does not contain {}".format(contains)

    if matches:
        reg = re.compile(matches)
        assert reg.matches(resp.data), "Response does not match {}".format(matches)

    if headers:
        assert_equal(resp.headers, headers)
