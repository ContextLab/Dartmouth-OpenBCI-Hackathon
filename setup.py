from distutils.core import setup
setup(name='openbci',
      version='1.0',
      py_modules=['openbci'],
      install_requires=['numpy', 'scipy', 'nibabel', 'nilearn' , 'seaborn', 'mne', 'matplotlib', 'ipython', 'pandas', 'sympy', 'nose', 'theano']
      )
