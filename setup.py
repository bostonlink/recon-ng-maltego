from setuptools import setup, find_packages

setup(
    name='recon-ng-maltego',
    author='David Bressler (@bostonlink), GuidePoint Security, LLC.',
    version='1.0',
    author_email='david.bressler@guidepointsecurity.com',
    description='Recon-ng Maltego local transform pack',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    package_data={
        '' : [ '*.gif', '*.png', '*.conf', '*.mtz', '*.machine' ] # list of resources
    },
    install_requires=[
        'canari'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)
