from PyLTSpice import SpiceEditor

se = SpiceEditor("rc_example.asc")

se.set_component_value('R1', 11000)
se.set_component_value('C1', 1.1E-6)
se.set_component_value('V1', 11)

se.run()