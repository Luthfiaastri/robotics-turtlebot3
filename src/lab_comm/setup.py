import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'lab_comm'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Daftarkan launch file ke direktori install
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Luthfiaastri',
    maintainer_email='luthfiaastrinuraini2006@mail.ugm.ac.id',
    description='Praktikum Komunikasi ROS 2',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor_publisher = lab_comm.sensor_publisher:main',
            'sensor_subscriber = lab_comm.sensor_subscriber:main',
            'processing_node = lab_comm.processing_node:main',
            'reset_service = lab_comm.reset_service:main',
            'motion_action_server = lab_comm.motion_action_server:main',
        ],
    },
)
