from setuptools import setup

setup(name='sendmail',
      version='1.0.0',
      description='Simplified Email Sender',
      long_description="Gives simplified acess to Python's built-in module for sending email over SMTP servers",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Intended Audience :: Developers',
          'Topic :: Communications :: Email',
      ],
      keywords='email smtp',
      url='http://github.com/dimaba/sendmail',
      author='dimaba',
      author_email='dimaba14@gmail.com',
      license='MIT',
      packages=['sendmail'],
      zip_safe=True)

