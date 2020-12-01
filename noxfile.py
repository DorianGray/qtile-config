import nox


nox.options.sessions = ['lint']
nox.options.stop_on_first_error = True
nox.options.reuse_existing_virtualenvs = True
nox.options.pythons = ['pypy3']


@nox.session()
def test(session):
    session.install('xcffib')
    session.install('-r', 'pip/requirements-test.txt')
    session.run('pytest')

@nox.session()
def lint(session):
    session.install('xcffib')
    session.install('-r', 'pip/requirements-lint.txt')
    session.run('flake8', 'qtile_config')
