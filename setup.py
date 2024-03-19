from setuptools import find_packages, setup

package_name = 'qsr'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools',
                      package_name + 'src.custom_package',
                      package_name + 'src.qsrrep_hmms',
                      package_name + 'src.qsrrep_lib',
                      package_name + 'src.qsrrep_pf',
                      package_name + 'src.qsrrep_ros',
                      package_name + 'src.qsrrep_utils',],
    zip_safe=True,
    maintainer='alex',
    maintainer_email='giang.nht108201@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts':[
            'test_node = qsr.test_node:main',
        ],
    },
)
