# Socket Programming

Sockets are the interface between the transport layer and application layer of the internet protocol stack.

## UDP

Unreliable datagram; no "connection" between the client and the server.UDP provides unreliable transfer of group of bytes (datagrams) between the client and the server process. No handshaking before sending the data. The sender explicitly attaches the IP destination address and port number to each packet. The receiver extracts sender IP address and port number from received packets. Transmitted data may be lost or received out of order.

## TCP

TCP is connection oriented. Client must contact server first before communication can take place. Server process must firstbe running and created a socket that welcomes the client's contact.

TCP provides a reliable, in-order byte-stream transfer between client and server process. Server creates a "listening" socket for welcoming clients but it's not the socket used for communication (flow of data).

Client contacts server by creating a TCP socket, specifying IP address and port number of the server process. When client creates a TCP socket, it establishes a connection to the server process. When contacted by client, server creates a new socket for communication with that particular client. This allows server to be able to communicate with multiple clients. Source port numbers are used to distinguish client.

