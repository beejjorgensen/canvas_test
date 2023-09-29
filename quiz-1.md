{
    "quiz": {
        "title": "Quiz 1",
        "description": "Test Quiz Description",
        "shuffle_answers": true
    }

    "questions": [
        "q": {
            "title": "Question 1",
            "points": 10,
            "type": "multiple choice",
            "text": "What is the air speed of an unladen swallow?",

            "correct": [
                "African or European swallow?"
            ],

            "incorrect": [
                "10 m/s",
                "20 m/s",
                "I don't know that."
            ]
        }
    ]
}

TITLE=Quiz 1
DESC=Description of quiz 1
SHUFFLE=true

[Q|Question 1|10|mc] The correct order for socket calls to set up a server is:

[C] socket, bind, listen, accept

[IC] socket, bind, connect

[IC] socket, bind, connect, accept

[IC] socket, listen, connect


[Question 2|10|mc] The correct order for socket calls to set up a client connection is:

socket, connect

socket, listen

socket, accept

socket, close

---

[5 points]

The IPv6 address space is _________ than the IPv4 address space.

Larger

Smaller

---

The Internet Protocol (IP) is responsible for:

Routing

Message integrity

Message reconstruction

Web servers

---

The Transmission Control Protocol (TCP) is responsible for:

Message integrity, message ordering, and packet reassembly

Routing

The electrical signals that get sent out on the wire

Web servers

---

The HyperText Transport Protocol (HTTP) is responsible for:

Web requests and responses

Message integrity, message ordering, and packet reassembly

Routing

The electrical signals that get sent out on the wire

---

In TCP and UDP, ports are sent as 16-bit unsigned numbers, which means they range from:

0-65535

0-32767

0-16384

0-255

---

In IPv4, the IP address is stored as a four byte number and is printed with each byte separated by a period. The maximum range of each individual number is:

0-255

0-65536

0-8

0-999

---

Why would someone use TCP over UDP?

They need the data to arrive intact and in order.

They need to be able to get the most performance and are OK with losing a few packets.

They want the lowest overhead possible.

They need a simpler protocol implementation.

---

A fully-encapsulated HTTP packet might be wrapped up by protocols in which order:

Ethernet, IP, TCP, HTTP

Ethernet, TCP, IP, HTTP

IP, Ethernet, TCP, HTTP

Ethernet, HTTP, IP, TCP

---

The following is an example of a MAC address:

8c:85:90:63:3c:ef

2001:db8::8a2e:370:7334

198.51.100.52

555-2368

---

In the Internet model, which layer is responsible for data integrity?

Transport

Application

Link

Internet

---

I've written my own custom chat client and server, and defined my own protocol for them to communicate. On which layer of the Internet model would this protocol live?

Application

Transport

Link

Internet

---
