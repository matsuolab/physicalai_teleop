from setuptools import find_packages, setup

package_name = 'physicalai_teleop'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'moveit_py'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='tatsukamijo@icloud.com',
    description='Teleoperation package for CRANE+ V2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop_keyboard = physicalai_teleop.teleop_keyboard:main',
        ],
    },
)
