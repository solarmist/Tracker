from nose import with_setup
from nose.tools import eq_
from bs4 import BeautifulSoup as BS
from self_quant import tracker
from py_w3c.validators.html.validator import HTMLValidator

app = tracker.app.test_client()
templates = ['main.html', 'layout.html']
tidy_options = {'numeric-entities': True,
                'markup': False,
                'show-warnings': True,
                'show-errors': 2}


def setup_func():
    """Setup test fixtures"""
    pass


def teardown_func():
    """Tear down test fixtures"""
    pass


@with_setup(setup_func, teardown_func)
def test_index():
    rv = app.get('/')
    page = BS(rv.data)
    eq_(page.title.text, 'Dietzilla:graph',
        'Wrong page')


def test_templates():
    for template in templates:
        yield check_template, template

def check_template(name):
    rv = app.get('/template/%s' % name)
    HV = HTMLValidator()
    HV.validate_fragment(rv.data)
    errors = [e['message'] for e in HV.errors]
    warnings = [w['message'] for w in HV.warnings]

    eq_(len(errors), 0,
        msg='%s contained errors:\n%s' % (name, '\n'.join(errors)))
    eq_(len(warnings), 0,
        msg='%s contained warnings:\n%s' % (name, '\n'.join(warnings)))


if __name__ == '__main__':
    nose.runmodule()
