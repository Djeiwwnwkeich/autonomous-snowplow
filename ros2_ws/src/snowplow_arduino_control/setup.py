from setuptools import find_packages, setup

package_name = 'snowplow_arduino_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name],
        ),
        (
            'share/' + package_name,
            ['package.xml'],
        ),
    ],
    install_requires=[
        'setuptools',
        'pyserial',
    ],
    zip_safe=True,
    maintainer='Djeiwwnwkeich',
    maintainer_email='your_email@example.com',
    description='ROS 2 control package for the snowplow actuator system.',
    license='MIT',
    entry_points={
        'console_scripts': [
            'snowplow_arduino_control = '
            'snowplow_arduino_control.snowplow_arduino_control:main',
        ],
    },
)
