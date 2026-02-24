# Week 8 – Object-Oriented Programming Essentials

## Lab Exercise 1: Secure User Authentication System

This exercise demonstrates object-oriented principles with secure encapsulation.

### Features
- Private password handling
- Login attempt tracking
- Account lock after 3 failed attempts
- Admin unlock functionality
- Activity logging
- Role-based access control

### Concepts Used
- Encapsulation (private attributes)
- Methods for controlled access
- Role-based privilege validation
- Logging with timestamps


---

## Lab Exercise 2: IoT Device Management System

This system models IoT devices with security validation and access control.

### Features
- Device class with private attributes
- Compliance check (30-day security scan rule)
- Firmware update (admin only)
- Device quarantine (admin only)
- Owner-based access control
- Central DeviceManager
- Security report generation

### Concepts Used
- OOP (classes & objects)
- Encapsulation
- Access control logic
- State validation
- Role separation (Admin vs Standard User)


---

## How to Run

```bash
cd week8
python user_auth.py
python iot_system.py