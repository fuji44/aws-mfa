from setuptools import setup

setup(
    name = 'aws-mfa',
    version = '0.1.0',
    url = 'https://github.com/fuji44/aws-mfa',
    license = 'MIT',
    author = 'fuji44',
    description = 'A CLI tool for configuring temporary access keys using MFA.',
    install_requires = ['setuptools', 'click'],
    packages = ['awsmfa'],
    entry_points = {
        'console_scripts': [
            'aws-mfa = awsmfa.aws_mfa:aws_mfa'
        ]
    }
)