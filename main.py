from brownie import *
from brownie.project.TokenProject import *
p = project.load()
p.load_config()

# Uses the brownie TokenProject library
network.connect('development')

