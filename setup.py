from setuptools import find_packages, setup

package_name = 'piece_identifier'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, [package_name + '/cobot_best.pt']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zachc',
    maintainer_email='zachchampion79@gmail.com',
    description='TODO: Package description',
    license='GPL-3.0-only',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'piece_identifier = piece_identifier.piece_identifier:main'
        ],
    },
)
