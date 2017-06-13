'''
Created on May 2, 2017

@author: mkowkab
'''
import unittest

from discoveryTest import DiscoveryMicroserviceTest
from scpTest import SCPMicroserviceTest
from serverInventoryTest import ServerInventoryMicroserviceTest
from powerThermalTest import PowerThermalMicroserviceTest
from chassisInventoryTest import ChassisInventoryMicroserviceTest

class microservicesSuite:        
        
        discoverySuite = unittest.TestLoader().loadTestsFromTestCase(DiscoveryMicroserviceTest)
        scpSuite = unittest.TestLoader().loadTestsFromTestCase(SCPMicroserviceTest)
        serverInventorySuite = unittest.TestLoader().loadTestsFromTestCase(ServerInventoryMicroserviceTest)
        powerThermalSuite = unittest.TestLoader().loadTestsFromTestCase(PowerThermalMicroserviceTest) 
        chassisInventorySuite = unittest.TestLoader().loadTestsFromTestCase(ChassisInventoryMicroserviceTest) 
        allTestsSuite = unittest.TestSuite([discoverySuite, scpSuite, serverInventorySuite, powerThermalSuite, chassisInventorySuite])

        unittest.TextTestRunner(verbosity=2).run(allTestsSuite)