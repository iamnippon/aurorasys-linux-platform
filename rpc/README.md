
# RPC Module

**Lightweight JSON-Based Remote Procedure Call System**

---

## 1. Overview

The RPC module implements a minimal distributed communication layer using TCP sockets and a structured JSON protocol.

It demonstrates how remote procedure calls can be executed across processes in a client-server architecture.

The system supports:

* Remote method invocation
* Parameter serialization
* Structured response handling
* Concurrent client connections

This module models the foundational principles behind distributed systems communication frameworks.

---

## 2. Architecture

```
+-------------+        TCP        +-------------+
|   Client    |  ──────────────►  |   Server    |
| (client.py) |  ◄──────────────  | (server.py) |
+-------------+                   +-------------+
         JSON Request/Response Protocol
```

The client sends a JSON request containing:

* Method name
* Parameter list

The server:

1. Parses the request
2. Dispatches to a registered procedure
3. Returns a structured JSON response

---

## 3. Implemented Procedures

The server registers the following example methods:

| Method     | Description            |
| ---------- | ---------------------- |
| `ping`     | Connectivity check     |
| `add`      | Integer addition       |
| `multiply` | Integer multiplication |

Additional procedures can be registered dynamically.

---

## 4. Protocol Specification

### Request Format

```json
{
  "method": "add",
  "params": [5, 3]
}
```

### Successful Response

```json
{
  "status": "success",
  "result": 8
}
```

### Error Response

```json
{
  "status": "error",
  "message": "Method not found"
}
```

This structured protocol ensures predictable client-server interaction.

---

## 5. Concurrency Model

The server uses:

* Thread-per-connection model
* Independent client handling
* Safe request isolation

This allows multiple clients to issue RPC calls simultaneously.

---

## 6. Requirements

* Python 3.10+
* No external dependencies (standard library only)

---

## 7. Usage

### Start the Server

```bash
python3 server.py
```

Server output:

```
[INFO] RPC Server running on 127.0.0.1:5000
```

---

### Call from Client

```bash
python3 client.py ping
```

```bash
python3 client.py add 10 25
```

```bash
python3 client.py multiply 4 6
```

---

## 8. Observations

This module demonstrates:

* Request serialization
* Network-based execution
* Remote computation
* Error propagation
* Distributed process interaction

It reflects the architectural foundation of:

* gRPC
* REST-based services
* Microservices
* Distributed computing systems

---

## 9. Design Considerations

* JSON chosen for simplicity and readability
* TCP sockets for reliable transport
* Threading for concurrency
* Dynamic method registration for extensibility

The system prioritizes clarity and architectural transparency over production-level scalability.

---

## 10. Extension Opportunities

Future enhancements may include:

* Persistent connections
* Request framing for streaming
* Authentication layer
* TLS encryption
* gRPC or REST conversion
* Load balancing simulation

---

# Summary

The RPC module provides a practical demonstration of remote method invocation using a structured protocol and concurrent client handling.

It illustrates how distributed systems abstract network communication into callable procedures while maintaining predictable response semantics.

