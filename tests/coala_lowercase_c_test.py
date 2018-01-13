pytest_plugins = ['errbot.backends.test']

extra_plugin_dir = 'plugins'

def test_cloudcv_lowercase(testbot):
    testbot.assertCommand('what is cloudcv?',
                          'cloudcv is always written with a lower case c')

def test_cep(testbot):
    testbot.assertCommand('what is a CEP?',
                          'cEP is always written with a lower case c')
