# Self-service printing system
A team project for the Logical Design Project course at HCMUT involving a system to make printing more accessible, allowing printers to operate independently. Some key deliverables include: a dashboard device and a web application implemented on an
embedded computer for file uploading, online payment, and in-person order pickup.

## GUI Architecture
Based on the detailed interface design (High-fidelity Wireframe), my team implemented the printer control GUI using Python Tkinter. Users will interact with the interface through the touch screen of the control panel. Considering the described interface requirements and interactions, my team proposes a layered model for the application's objects as follows:

- **Widgets:** Objects built directly from the tkinter library, with specific adjustments in configuration to meet interface requirements.

- **Objects:** A group of Widgets with customized behaviors that depend on each other, enhancing user interaction with the system.

- **Frames:** Specific interface frames for the application, responsible for fixing the position of each display partition on the screen while providing methods to efficiently utilize Widgets and Objects for higher-level application layers.

- **Pages:** The displayed pages of the application containing content necessary for users, as well as methods to help users interact with the system.

- **Flows:** A group of Pages and Frames with related content and interdependent behaviors, controlled by a specific logic mechanism.

- **System:** The complete application system comprising Flows and a Logic mechanism controlling interactions, and managing the operation of the file uploading server.

## File uploading Web Server
To provide a user interface for sending files to the GUI application, my team built a web server running on the Raspberry Pi:
- The **ExpressJS** framework is used to built the server.
- The **express-fileupload** middleware is used to implement the file upload feature.
- **EJS templates** are used to facilitate communication between the NodeJS backend program and the HTML, CSS code on the frontend of the web page, serving the key-based connection verification process.

In addition, my team established a connection between the interface program and the web server by creating a TCP connection between the two programs using the **net** module of NodeJS and the **socket** module of Python.

## Payment checking
- With the necessary information of the system owner (bank account number, name of their bank), customer's file (number of pages, paper size, number of side printiv ng), and system configuration (price per printed page), we utilize **VietQR Quick Link** tool to generate a QR Code for customers to scan and pay for their orders.
- To verify the payment, we use the **Mighty Text** application to forward the system owner's phone messages to our system and check for payment information (contained in messages sent from the bank of the system's owner).

The project documents are:
- Detailed report (in Vietnamese): [here](https://github.com/NhatKhai352528/NightPanther/blob/main/doc/%5BCO3091%5D%20B%C3%A1o%20c%C3%A1o%20nghi%E1%BB%87m%20thu.pdf).
- Brief overview with Google Slide (in Vietnamese): [here](https://github.com/NhatKhai352528/NightPanther/blob/main/doc/%5BCO3091%5D%20Slide%20thuy%E1%BA%BFt%20tr%C3%ACnh.pdf)

## Final product
![image](https://github.com/NhatKhai352528/NightPanther/assets/87921251/6af321ce-f2f6-4227-9304-99c3c2bfb6c1)


