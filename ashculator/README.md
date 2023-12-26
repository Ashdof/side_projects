# ASHCULATOR
ASHCulator is a console-based application that performs simple arithmetic computations: addition, subtraction, multiplication, division and modulo. This program does not implement any shell-based command.

## Process
The application executes in a loop. It presents the *ashculator,* **ashculate ?>** to the user for input. When provided with the correct input values, it prints the results **:) <value>** of the computation on the next line. It exits when the user enters **exit**.

## Flowchart
The following image shows the high level execution process for the application
<br /><img src="img/ashculator_flowchart.png" alt="ashculator flowchart"><br />

## Execution Demonstration
The screenshot below shows the **ASHCulator** in use to perform basic arithmetic computations.
<br /><img src="img/ashculate_process.png" alt="ashculate process"><br />

## Issues
ASHCulator has minor issue with subtraction operation. In a typical subtraction operation of a double digit number with a floating point value as the second operand after the operator leaves the application suspended as shown below:
<br /><img src="img/ashculate_suspension.png" alt="ashculate suspension"><br />
