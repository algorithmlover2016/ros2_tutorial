<?xml version="1.0"?>
<?xml-model href="http://download.ros.org/schema/package_format3.xsd" schematypens="http://www.w3.org/2001/XMLSchema"?>
<package format="3">
  <name>py_srvcli</name>
  <version>0.0.0</version>
  <description>a python demo of service/client</description>
  <maintainer email="yubo.upt@gmail.com">yubo</maintainer>
  <license>Apache License 2.0</license>

  <depend>rclpy</depend>
  <depend>example_interfaces</depend>
  <depend>tutorial_interfaces</depend>

  <test_depend>ament_copyright</test_depend>
  <test_depend>ament_flake8</test_depend>
  <test_depend>ament_pep257</test_depend>
  <test_depend>python3-pytest</test_depend>

  <export>
    <build_type>ament_python</build_type>
  </export>
</package>
